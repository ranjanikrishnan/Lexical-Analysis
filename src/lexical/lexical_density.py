from .non_lexicals import non_lexical_words


def get_words(input_text):
    words = input_text.casefold().split(' ')
    return words


def get_lexical_words(words):
    lexical_words = list(filter(lambda x: x not in non_lexical_words, words))
    print('lexical words:', lexical_words)
    return lexical_words


def get_lexical_density(input_text):
    words = get_words(input_text)
    lexical_words = get_lexical_words(words)
    lexical_density = len(lexical_words) / len(words)
    print('lexical_density: ', lexical_density)
    if input_text in ('', 'NULL'):
        return 0
    else:
        return round(lexical_density, 2)

