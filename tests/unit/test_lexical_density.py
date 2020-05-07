from lexical.lexical_density import get_words, get_lexical_words, get_lexical_density


def test_get_words():
    assert(get_words('Kim loves going to the cinema')) == ['kim', 'loves', 'going', 'to', 'the', 'cinema']   


def test_get_lexical_words():
    assert(get_lexical_words(['kim', 'loves', 'going', 'to', 'the', 'cinema'])) == ['kim', 'loves', 'going', 'cinema']


def test_get_lexical_density():
    assert(get_lexical_density('Kim loves going to the cinema')) == 0.67
