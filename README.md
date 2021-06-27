# GraDiAn
The Grammatical Distribution Analyser (GraDiAn) is used for analysing grammatical distributions; particularly the distributions of popular NLP datasets.

# Usage
Syntactic Dependency Counter from text:
```
from gradian import SDC

sdc = SDC.from_string('This is a test sentence!')
```

Or from a series of texts:
```
from gradian import SDC

sdc = SDC.from_string_arr(['This is a test sentence!', 'This is another sentence',
                           'How about another?')
```
