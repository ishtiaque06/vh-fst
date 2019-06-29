from utils import spe_to_fst

def test_spe_to_fst_valid():
    alphabet = {'a', 'b', 'c', 'd'}
    states = {0: 'start', 1: 'c', 2: 'ca'}
    transitions = {
        (0, 'a'): ('a': 0), (0, 'b'): ('b', 0), (0, 'd'): ('d', 0),
        (0, 'c': '', 1),
        (1, 'a'): ('': 2), (1, 'b'): ('cb', 0), (1, 'd'): ('cd', 0),
        (1, 'c': 'cc', 1),
        (2, 'a'): ('caa': 0), (2, 'b'): ('cab', 0), (2, 'd'): ('cbd', 0),
        (2, 'c': 'cac', 1)
    }
    object = spe_to_fst('a', 'b', 'c', 'd')
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet
