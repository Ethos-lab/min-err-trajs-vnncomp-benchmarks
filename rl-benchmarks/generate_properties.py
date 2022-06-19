import argparse
import os
import random
import math


def write_vnnlib_file(env, specdir, case_n, result, state, targets, noise_frac):
    tab = "\t"

    name = env['name']
    num_inputs = env['num_inputs']
    num_commands = env['num_commands']
    spec_type = env['spec_type']

    with open(os.path.join(specdir, name+"_case_"+str(case_n))+".vnnlib", 'w') as fp:

        fp.write(f"; {name} property " + str(case_n))
        fp.write('\n\n')

        for i in range(num_inputs):
            fp.write(f"(declare-const X_{i} Real)\n")
        fp.write('\n')

        for i in range(num_commands):
            fp.write(f"(declare-const Y_{i} Real)\n")
        fp.write('\n')

        # Now the input noise_frac
        for i in range(num_inputs):
            x_min = state[i] - noise_frac
            x_max = state[i] + noise_frac
            # TODO FOR THE ANGLES, WRAP AROUND 2PI
            fp.write(f"; Input {i}\n")
            fp.write(f"(assert (<= X_{i} {x_max}))\n")
            fp.write(f"(assert (>= X_{i} {x_min}))\n")
            fp.write('\n')


        # Now the unsafe spec
        fp.write(f"; unsafe if command is {targets} (spec type {spec_type}) \n")
        
        if spec_type == "minimal":
            targets = targets[0]
            if num_commands == 2:
                i = targets ^ 1
                spec = "(assert \n"
                spec = spec + f"(and (>= Y_{i} Y_{targets}))\n"
            else:
                for i in range(num_commands):
                    if targets == i: continue
                    spec = "(assert \n"
                    spec = spec + f"(and (>= Y_{i} Y_{targets}))\n"
                spec = spec + ")\n"
                    
        elif spec_type == "maximal":
            targets = targets[0]
            if num_commands == 2:
                i = targets ^ 1
                spec = "(assert \n"
                spec = spec + f"(<= Y_{i} Y_{targets})\n" 
            else:
                for i in range(num_commands):
                    if targets == i: continue
                    
                    spec = "(assert \n"
                    spec = spec + f"(<= Y_{i} Y_{targets})\n" 
            spec = spec + ")\n"
            

        elif spec_type == "disjunct":
            # just hardcode it here 
            spec = "(assert (or \n"
 
            for target in targets:
                target_j = target // 4
                target_k = target % 4   
 
                spec += tab + "(and "

                for j in range(4):
                    if target_j == j:  continue
                    spec_j = f"(<= Y_{j} Y_{target_j})"
                    spec += spec_j
                 
                for k in range(4,8):
                    if target_k + 4 == k:  continue
                    spec_k = f"(<= Y_{k} Y_{target_k+4})" 
                    spec += spec_k
                spec += ")\n"
            spec += "))\n"

        else:
            raise NotImplementedError("unnknown spec_type " + str(spec_type))

        fp.write(spec)

def add_to_instances(env, filename, model_file, timeout):
    with open("instances.csv", "a") as fp:
        fp.write(f"{model_file},{env}_case_{filename}.vnnlib,{timeout}\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Specification Generrator: vnnlib format')
    parser.add_argument('seed', type = int, help='seed is used for random noise limit and timeout for each instance')
    args = parser.parse_args()

    specdir = "specs"

    envs = [
        {'name': 'cartpole', 'num_inputs': 4, 'num_commands': 2, 'spec_type': 'maximal'},
        {'name': 'lunarlander', 'num_inputs': 8, 'num_commands': 4, 'spec_type': 'maximal'},
        {'name': 'dubinsrejoin', 'num_inputs': 8, 'num_commands': 8, 'spec_type': 'disjunct'}
        ]


    if not os.path.exists(specdir):
        os.makedirs(specdir)
    
    if os.path.exists("instances.csv"):  os.remove("instances.csv")

    seed = args.seed
    # Use seed for random amount of noise
    random.seed(seed)
    

    for env in envs:

        name = env['name']
        num_inputs = env['num_inputs']
        num_commands = env['num_commands']
        spec_type = env['spec_type']

        # Load csv of all options
        lines = []
        with open(f"cases/{name}_details.txt", "r") as fp:
            for line in fp:
                lines.append(line.strip().split('\t'))


        for i, row in enumerate(lines[1:]):

            state = [float(x) for x in row[3][1:-1].split(',')]

            try:
                commands = [int(row[5])]
            except:
                commands = [int(x) for x in row[5][1:-1].split(',')]

            # Noise-frac: random value based on seed -- what's in details.txt plus a random amount up to 0.5% greater
            noise_frac = float(row[1]) + random.uniform(0, 0.005)
            write_vnnlib_file(env, specdir, row[0]+"_"+str(i), row[0], state, commands, noise_frac)

            # Also add to instances.csv:
            # With a random timeout that's based on seed. Add a random amount that's a multiple of it, up to 400%
            timeout = float(row[2])
            timeout =  random.uniform(1.0, 30.0)*timeout
            timeout = math.ceil(timeout)  # integer
            # But there are many that are just 1 now -- if so, make it random<10:
            # if timeout == 1:  timeout = random.randint(1, 10)

            add_to_instances(name, row[0]+"_"+str(i), f"{name}.onnx", timeout)


