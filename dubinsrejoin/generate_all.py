import os
import glob

with open("nnenum_details.txt") as fp:
    wcl = sum(1 for line in fp)

for i in range(wcl-2):
    os.system(f"python generate_properties.py {i}")


# Now make the instances.csv
files = glob.glob("specs/*.vnnlib")
network = "model.onnx"
with open("instances.csv", "w") as fp:
    for f in files:
        fn = os.path.basename(f)
        fp.write(f"{fn},{network}\n")

