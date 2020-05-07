import re
from .lexical_density import get_lexical_density


def get_sentences(input_text):
    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', input_text)
    return sentences


def get_lexical_density_verbose(input_text):
    sentences = get_sentences(input_text)
    lexical_density_verbose = list(map(
        lambda x: get_lexical_density(x), sentences))
    return lexical_density_verbose
