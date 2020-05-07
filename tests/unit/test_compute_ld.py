from lexical.compute_lexical_density import compute_ld


def test_compute_ld():
    given = 'Kim loves going to the cinema. And he loves to eat popcorn there. That\'s what I think.'
    # arrange
    wanted = {
        "data": {
            "overall_ld": "0.71"
        }
    }
    # act
    got = compute_ld(given)
    # assert
    assert wanted == got

    mode = 'verbose'
    wanted = {
        "data": {
            "overall_ld": "0.71",
            "sentence_ld": "[0.67, 0.57, 1.0]"
        }
    }
    got = compute_ld(given, mode)
    assert wanted == got

    given = ''
    wanted = {
        "data": {
            "overall_ld": "0"
        }
    }
    got = compute_ld(given)
    assert wanted == got
