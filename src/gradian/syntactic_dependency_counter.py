from collections import Counter


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
