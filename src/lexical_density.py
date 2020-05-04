non_lexical_words = ['to', 'got', 'is', 'have', 'the']


def get_words(input_text):
    words = input_text.split(' ')
    return words


def get_lexical_words(words):
    lexical_words = list(filter(lambda x: x not in non_lexical_words, words))
    return lexical_words


def get_lexical_density(input_text):
    words = get_words(input_text)
    lexical_words = get_lexical_words(words)
    lexical_density = len(lexical_words) / len(words)
    return round(lexical_density, 2)
