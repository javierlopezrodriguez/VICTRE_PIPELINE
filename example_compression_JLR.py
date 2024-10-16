#############################################################
#   MOVE THIS FILE TO THE PARENT DIRECTORY BEFORE RUNNING   #
#############################################################

from Victre import Pipeline
from Victre import Constants


seed = 1

original_phantom = "example_phantom_JLR/1/p_1.raw.gz" # results/seed/file
results_folder = "example_phantom_JLR"

pline = Pipeline(seed=seed,
                 phantom_file=original_phantom,
                 results_folder=results_folder)

# phantom is already generated, compress now

pline.compress_phantom(thickness=50)

pline.crop()