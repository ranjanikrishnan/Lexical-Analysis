from .lexical_density import get_lexical_density
from .lexical_density_verbose import get_lexical_density_verbose


def compute_ld(mode, input_text):
    output_data = {}
    if mode:
        lexical_density_verbose = get_lexical_density_verbose(input_text)
        overall_ld = get_lexical_density(input_text)
        output_data['data'] = {
            'sentence_ld': str(lexical_density_verbose),
            'overall_ld': str(overall_ld)}
        return output_data
    else:
        ld = get_lexical_density(input_text)
        output_data['data'] = {'overall_ld': str(ld)}
        return output_data
