#############################################################
#   MOVE THIS FILE TO THE PARENT DIRECTORY BEFORE RUNNING   #
#############################################################

from Victre import Pipeline
from Victre import Constants
import os

seed = 4

results_folder = "example_phantom_JLR"
original_phantom = f"{results_folder}/{seed}/p_{seed}.raw.gz" # results/seed/file
loc_file = original_phantom.replace(".raw.gz", ".loc")

# create loc file with 0,0,0 if not found
# https://github.com/DIDSR/VICTRE_PIPELINE/issues/4
if not os.path.exists(loc_file):

    # Create the content for the .loc file
    loc_content = "0, 0, 0\n0, 0, 0" # two lines to avoid error in cropping stage

    # Write the content to the new .loc file
    with open(loc_file, "w") as file:
        file.write(loc_content)


# pipeline
pline = Pipeline(seed=seed,
                 phantom_file=original_phantom,
                 results_folder=results_folder)

# phantom is already generated, compress now

pline.compress_phantom(thickness=50)

pline.crop()

"""
seed 2 (no .loc file):
Error while compressing, check the output_compression.out file in the results folder
Traceback (most recent call last):
  File "/home/javier/fsg_interfaces/4_deformation/VICTRE_PIPELINE/example_compression_JLR.py", line 20, in <module>
    pline.compress_phantom(thickness=50)
  File "/home/javier/fsg_interfaces/4_deformation/VICTRE_PIPELINE/Victre/Pipeline.py", line 1969, in compress_phantom
    raise Exceptions.VictreError("Compression error")
Victre.Exceptions.VictreError: Compression error

file: output_compression.out
Segmentation fault (core dumped)

seed 3 (empty .loc file):
/home/javier/fsg_interfaces/4_deformation/VICTRE_PIPELINE/Victre/Pipeline.py:364: UserWarning: loadtxt: input contained no data: "example_phantom_JLR/3/p_3.loc"
  locations = np.loadtxt(
Traceback (most recent call last):
  File "/home/javier/fsg_interfaces/4_deformation/VICTRE_PIPELINE/example_compression_JLR.py", line 14, in <module>
    pline = Pipeline(seed=seed,
            ^^^^^^^^^^^^^^^^^^^
  File "/home/javier/fsg_interfaces/4_deformation/VICTRE_PIPELINE/Victre/Pipeline.py", line 392, in __init__
    if not (type(locations[0]) is list or type(locations[0]) is np.ndarray):
                 ~~~~~~~~~^^^
IndexError: index 0 is out of bounds for axis 0 with size 0
"""