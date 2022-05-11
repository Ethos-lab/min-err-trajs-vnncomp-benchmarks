import argparse
import os
import pandas as pd

env = "Dubins"
num_inputs = 8
num_commands = 16
spec_type = "disjunct"


def write_vnnlib_file(case_n, result, state, targets, noise_frac):
    tab = "\t"

    with open(os.path.join("specs", "dubins_case_"+str(case_n))+".spec", 'w') as fp:

        fp.write(f"; {env} Rejoin property " + str(case_n))
        fp.write('\n\n')

        for i in range(num_inputs):
            fp.write(f"(declare-const X_{i} Real)\n")
        fp.write('\n')

        for i in range(num_commands):
            fp.write(f"(declare-const Y_{i} Real\n")
        fp.write('\n')

        # Now the input noise_frac
        for i in range(num_inputs):
            x_min = state[i] - noise_frac
            x_max = state[i] + noise_frac
            # TODO FOR THE ANGLES, WRAP AROUND 2PI
            fp.write(f"; Input {i}\n")
            fp.write(f"(assert <= X_{i} {x_max}\n")
            fp.write(f"(assert >= X_{i} {x_min}\n")
            fp.write('\n')


        # Now the unsafe spec
        fp.write(f"; unsafe if command is {targets} (spec type {spec_type}) \n")
        
        if spec_type == "minimal":
            for i in range(num_commands):
                if target == i: continue
                spec = "(assert \n"
                spec = spec + f"(and (>= Y_{i} Y_{target}))\n"
                    
        elif spec_type == "maximal":
            for i in range(num_commands):
                if target == i: continue
                
                spec = "(assert \n"
                spec = spec + f"(and (<= Y_{i} Y_{target}))\n" 

        elif spec_type == "disjunct":
            # just hardcode it here 
            spec = "(assert or \n"

            for target in targets:
                target_j = target // 4
                target_k = target % 4    

                spec += tab + "( and "
                for j in range(4):
                    if target_j == j:  continue
                    spec_j = f"(<= Y_{j} Y_{target_j}) "
                    spec += spec_j
                
                for k in range(4,8):
                    if target_k + 4 == k:  continue
                    spec_k = f"(<= Y_{k} Y_{target_k}) "
                    spec += spec_k
                spec += tab + ")\n"
            spec += ")\n"

        else:
            raise NotImplementedError("unnknown spec_type " + str(spec_type))

        fp.write(spec)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Specification Generrator: vnnlib format',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--seed',type = int,default= 0, help='seed is selected for image selection')
    args = parser.parse_args()


    idx = args.seed


    # Load csv of all options
    df = pd.read_csv("nnenum_details.txt", sep='\t')

    row = df.iloc[idx]
    state = [float(x) for x in row.STATE[1:-1].split(',')]

    try:
        commands = [int(row.COMMAND)]
    except:
        commands = [int(x) for x in row.COMMAND[1:-1].split(',')]

    write_vnnlib_file(row.RES+"_"+str(idx), row.RES, state, commands, row.NOISE_FRAC)


