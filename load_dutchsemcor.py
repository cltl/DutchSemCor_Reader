"""
Load DutchSemCor annotations:
-mapping sense ->

Usage:
  load_dutchsemcor.py --input_folder=<input_folder> --output_folder=<output_folder> --prefixes=<prefixes> --verbose=<verbose>

Options:
    --input_folder=<input_folder> folder with xml files from DutchSemCor, i.e.,
    human.annotations.DSC.*.xml
    --output_folder=<output_folder> folder where loaded annotations are stored
    --prefixes=<prefixes> prefixes you want separated by -, e.g., r or d-r
    --verbose=<verbose> 0 --> no stdout 1 --> general stdout 2 --> detailed stdout

Example:
    python load_dutchsemcor.py --input_folder="resources/1.2.1.HUMAN_ANNOTATIONS/" \
    --output_folder="output" --prefixes="r" --verbose="1"
"""
import shutil
import os
import pickle
from docopt import docopt
import utils

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

allowed_prefixes = set(arguments['--prefixes'].split('-'))
verbose = int(arguments['--verbose'])

if os.path.exists(arguments['--output_folder']):
    shutil.rmtree(arguments['--output_folder'])
os.mkdir(arguments['--output_folder'])
output_path = os.path.join(arguments['--output_folder'],
                           'dutchsemcor.json')

sense2annotations = utils.get_sense2token_ids(xml_folder=arguments['--input_folder'],
                                              accepted_prefixes=allowed_prefixes,
                                              verbose=verbose)

with open(output_path, 'wb') as outfile:
    pickle.dump(sense2annotations, outfile)



