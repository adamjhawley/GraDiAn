from typing import List

import spacy


def load_spacy_model(model_name="en_core_web_trf", excludes: List[str] = []):
    try:
        nlp = spacy.load(model_name, exclude=[excludes])
    except OSError as e:
        raise OSError(f"Requested Spacy model not installed. Try installing the "
                      f"model with 'python -m spacy download {model_name}'") from e
    return nlp
