from lexical.lexical_density_verbose import get_sentences, get_lexical_density_verbose


def test_get_sentences():
    assert(get_sentences('Kim loves going to the cinema. And he loves to eat popcorn there. That\'s what I think.')) == ['Kim loves going to the cinema.', 'And he loves to eat popcorn there.' , 'That\'s what I think.'] 


def test_get_lexical_density_verbose():
    assert(get_lexical_density_verbose('Kim loves going to the cinema. And he loves to eat popcorn there. That\'s what I think.')) == [0.67, 0.57, 1.0]