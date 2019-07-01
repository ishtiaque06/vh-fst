from utils import spe_to_fst

def test_spe_to_fst_a_b_c_d():
    alphabet = {'a', 'b', 'c', 'd'}
    states = {0: '', 1: 'c', 2: 'ca'}
    transitions = {
        (0, '?'): ('?', 0),
        (0, 'a'): ('a', 0),
        (0, 'b'): ('b', 0),
        (0, 'c'): ('c', 1),
        (0, 'd'): ('d', 0),
        (1, '?'): ('?', 0),
        (1, 'a'): ('', 2),
        (1, 'b'): ('b', 0),
        (1, 'c'): ('c', 1),
        (1, 'd'): ('d', 0),
        (2, '?'): ('a?', 0),
        (2, 'a'): ('aa', 0),
        (2, 'b'): ('ab', 0),
        (2, 'c'): ('ac', 1),
        (2, 'd'): ('bd', 0),
    }
    object = spe_to_fst('a', 'b', 'c', 'd')
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet

def test_spe_to_fst_a_b_cd_ef():
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f'}
    states = {0: '', 1: 'c', 2: 'cd', 3: 'cda', 4: 'cdae'}
    transitions = {
        (0, '?'): ('?', 0),
        (0, 'a'): ('a', 0),
        (0, 'b'): ('b', 0),
        (0, 'c'): ('c', 1),
        (0, 'd'): ('d', 0),
        (0, 'e'): ('e', 0),
        (0, 'f'): ('f', 0),
        (1, '?'): ('?', 0),
        (1, 'a'): ('a', 0),
        (1, 'b'): ('b', 0),
        (1, 'c'): ('c', 1),
        (1, 'd'): ('d', 2),
        (1, 'e'): ('e', 0),
        (1, 'f'): ('f', 0),
        (2, '?'): ('?', 0),
        (2, 'a'): ('', 3),
        (2, 'b'): ('b', 0),
        (2, 'c'): ('c', 1),
        (2, 'd'): ('d', 0),
        (2, 'e'): ('e', 0),
        (2, 'f'): ('f', 0),
        (3, '?'): ('a?', 0),
        (3, 'a'): ('aa', 0),
        (3, 'b'): ('ab', 0),
        (3, 'c'): ('ac', 1),
        (3, 'd'): ('ad', 0),
        (3, 'e'): ('', 4),
        (3, 'f'): ('af', 0),
        (4, '?'): ('ae?', 0),
        (4, 'a'): ('aea', 0),
        (4, 'b'): ('aeb', 0),
        (4, 'c'): ('aec', 1),
        (4, 'd'): ('aed', 0),
        (4, 'e'): ('aee', 0),
        (4, 'f'): ('bef', 0),
    }
    object = spe_to_fst('a', 'b', 'cd', 'ef')
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet
