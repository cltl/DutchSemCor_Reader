from lxml import etree
from collections import defaultdict
import inspect
from glob import glob


def get_sense2token_ids(xml_folder, accepted_prefixes, verbose=0):
    """
    obtain mapping from sense -> sentences in which they are tagged
    
    :param str xml_folder: folder with xml files from DutchSemCor, i.e.,
    human.annotations.DSC.*.xml
    :param set accepted_prefixes: options: n | d | r | c
    
    :rtype: dict
    :return: mapping sense -> [token_id, token_id, ..]
    """
    sense2token_ids = defaultdict(set) 
    prefixes = set()

    for path in glob(f'{xml_folder}/*xml'):
        doc = etree.parse(path)
        for token_el in doc.xpath('token'):
            sense = token_el.get('sense')

            prefix = sense.split('_')[0]
            prefixes.add(prefix)

            if prefix in accepted_prefixes:
                sense2token_ids[sense].add(token_el.get('token_id'))
                
    if verbose:
        counts = [len(value) for value in sense2token_ids.values()]
        
        print(f'function {inspect.stack()[0][3]}')
        print(f'{xml_folder}')
        print(f'prefixes: {accepted_prefixes}')
        print(f'number of different senses: {len(sense2token_ids)}')
        print(f'minimum: {min(counts)}')
        print(f'maximum: {max(counts)}')
        print(f'average: {sum(counts) / len(counts)}')
        print(f'total: {sum(counts)}')
    
    return sense2token_ids