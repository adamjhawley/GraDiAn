from compare_tree_counts import compare_distributions
import json
import datasets
from datasets import load_dataset
from count_trees import get_tree_count_arr
from tqdm import tqdm

percent_to_load = 1

tasks = {
    'cb': {'splits': ['train', 'test', 'validation'],
              'atts': ['premise', 'hypothesis'],
               'atts_to_drop': ['label']},
    #'axb': {'splits': ['test'],
            #'atts': ['sentence1', 'sentence2']},
    #'axg': {'splits': ['test'],
            #'atts': ['premise', 'hypothesis']},
    'copa': {'splits': ['train', 'test', 'validation'],
             'atts': ['premise', 'choice1', 'choice2'],
             'atts_to_drop': ['question', 'label']},
    'wsc': {'splits': ['train', 'test', 'validation'],
            'atts': ['text'],
            'atts_to_drop': ['span1_index', 'span2_index', 'span1_text',
                             'span2_text', 'label']},
    'rte': {'splits': ['train', 'test', 'validation'],
            'atts': ['premise', 'hypothesis'],
            'atts_to_drop': ['label']},
    'wic': {'splits': ['train', 'test', 'validation'],
            'atts': ['word', 'sentence1', 'sentence2'],
            'atts_to_drop':['label', 'start1', 'start2', 'end1', 'end2']},
    'boolq': {'splits': ['train', 'test', 'validation'],
              'atts': ['question', 'passage'],
               'atts_to_drop': ['label']},
    'multirc': {'splits': ['train', 'test', 'validation'],
                'atts': ['paragraph', 'question', 'answer'],
                'atts_to_drop': ['label']},
    'record': {'splits': ['train', 'test', 'validation'],
               'atts': ['passage', 'query'],
                'atts_to_drop': ['entities', 'answers']}
}

for k, v in tasks.items():
    tree_counts = list()
    for split in ['test', 'train']:
        print(k, split)
        ri = datasets.ReadInstruction(split, to=percent_to_load, unit='%')
        dataset = datasets.load_dataset('super_glue', k, split=ri)
        sentences_combined = list()
        for attribute in v['atts']:
            sentences = [i[attribute] for i in tqdm(dataset)]
            sentences_combined += sentences
        tree_count = get_tree_count_arr(sentences_combined, attribute='pos')
        tree_counts.append(tree_count)

        with open(f'{k}_{split}_pos_tree_count.json', 'w') as f:
            json.dump(tree_count, f, indent=2)

    res = compare_distributions(tree_counts[0], tree_counts[1])
    file_name = f"temp/{k}_test_train_comparison.json"
    with open(file_name, 'w') as f:
        json.dump(res, f, indent=2) 

