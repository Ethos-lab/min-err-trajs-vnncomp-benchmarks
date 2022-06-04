import argparse
import os
import random
import math

env = "dubins"
num_inputs = 8
num_commands = 8
spec_type = "disjunct"


def write_vnnlib_file(case_n, result, state, targets, noise_frac):
    tab = "\t"

    with open(os.path.join("specs", env+"_case_"+str(case_n))+".vnnlib", 'w') as fp:

        fp.write(f"; {env} LunarLander property " + str(case_n))
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
            if num_commands == 2:
                i = targets ^ 1
                spec = "(assert \n"
                spec = spec + f"(and (<= Y_{i} Y_{targets}))\n" 
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

def add_to_instances(filename, model_file, timeout):
    with open("instances.csv", "a") as fp:
        fp.write(f"{model_file},{env}_case_{filename}.vnnlib,{timeout}\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Specification Generrator: vnnlib format')
    parser.add_argument('seed', type = int, help='seed is used for random noise limit and timeout for each instance')
    args = parser.parse_args()

    if not os.path.exists('specs'):
        os.makedirs('specs')

    seed = args.seed
    # Use seed for random amount of noise
    random.seed(seed)
    

    # Load csv of all options
    lines = []
    with open("nnenum_details.txt", "r") as fp:
        for line in fp:
            lines.append(line.strip().split('\t'))

    if os.path.exists("instances.csv"):  os.remove("instances.csv")


    for i, row in enumerate(lines[1:]):

        state = [float(x) for x in row[3][1:-1].split(',')]

        try:
            commands = [int(row[5])]
        except:
            commands = [int(x) for x in row[5][1:-1].split(',')]

        noise_frac = str(float(row[1]) + random.uniform(0, 0.01))
        write_vnnlib_file(row[0]+"_"+str(i), row[0], state, commands, float(row[1]))

        # Also add to instances.csv:
        # With a random timeout that's based on seed. Add a random amount that's a multiple of it. 
        timeout = float(row[2])
        timeout =  random.uniform(1.0, 1.5)*timeout
        timeout = math.ceil(timeout)
        # But there are many that are just 1 now -- if so, make it random<10:
        if timeout == 1:  timeout = random.randint(1, 10)

        add_to_instances(row[0]+"_"+str(i), "model.onnx", timeout)


