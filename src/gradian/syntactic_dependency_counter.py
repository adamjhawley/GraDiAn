from collections import Counter
from typing import List

import spacy


class SDC(Counter):
    def __init__(self, dependencies=None, **kwargs):
        if dependencies is None:
            self.dependencies = [
                'ROOT', 'acl', 'acomp', 'advcl', 'advmod', 'agent', 'amod', 'appos',
                'attr', 'aux', 'auxpass', 'case', 'cc', 'ccomp', 'compound', 'conj',
                'csubj', 'csubjpass', 'dative', 'dep', 'det', 'dobj', 'expl', 'intj',
                'mark', 'meta', 'neg', 'nmod', 'npadvmod', 'nsubj', 'nsubjpass', 'nummod',
                'oprd', 'parataxis', 'pcomp', 'pobj', 'poss', 'preconj', 'predet', 'prep',
                'prt', 'punct', 'quantmod', 'relcl', 'xcomp'
            ]
        else:
            self.dependencies = dependencies
        super().__init__(**kwargs)

    def update(self, x):
        if x is None:
            return
        if x is dict:
            assert set(x.keys()).issubset(self.dependencies)
        else:
            assert set(x).issubset(self.dependencies)
        super().update(x)

    @classmethod
    def from_string_arr(cls, texts: List[str]):
        # Relies on en_core_web_trf SpaCy model
        try:
            nlp = spacy.load("en_core_web_trf", exclude=['tokenizer', 'tagger',
                                                         'ner', 'lemmatizer',
                                                         'textcat'])
        except OSError as e:
            raise OSError('Try installing the model with "python -m spacy \
                          download en_core_web_trf', e)
        sdc = SDC()
        for doc in nlp.pipe(texts):
            sdc.update([token.dep_ for token in doc]) 
        return sdc

