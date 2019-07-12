from utils import spe_to_fst

def run_test_on_strings(input_list, output_list, object):
    for i in range(len(input_list)):
        assert "".join(object.step(list(input_list[i]))) == output_list[i]

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

    input_list = ["","wqcdpo", "qpcadoi", "cadcadcadcad", "cacacacad"]
    output_list = ["", "wqcdpo", "qpcbdoi", "cbdcbdcbdcbd", "cacacacbd"]

    run_test_on_strings(input_list, output_list, object)

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

    input_list = [  "",
                    "pcqwe",
                    "pcdqwe",
                    "pcdaqwe",
                    "pcdaeqwe",
                    "pcdaeqqwe",
                    "pcdaefqwe",
                    "cdaefcdaef",
                    ]
    output_list = [ "",
                    "pcqwe",
                    "pcdqwe",
                    "pcdaqwe",
                    "pcdaeqwe",
                    "pcdaeqqwe",
                    "pcdbefqwe",
                    "cdbefcdbef",
                    ]

def test_spe_to_fst_a_b_empty_cd():
    alphabet = {'a', 'b', 'c', 'd'}
    states = {0: '', 1: 'a', 2: 'ac'}
    transitions = {
        (0, '?'): ('?', 0),
        (0, 'a'): ('', 1),
        (0, 'b'): ('b', 0),
        (0, 'c'): ('c', 0),
        (0, 'd'): ('d', 0),
        (1, '?'): ('a?', 0),
        (1, 'a'): ('aa', 1),
        (1, 'b'): ('ab', 0),
        (1, 'c'): ('', 2),
        (1, 'd'): ('ad', 0),
        (2, '?'): ('ac?', 0),
        (2, 'a'): ('aca', 1),
        (2, 'b'): ('acb', 0),
        (2, 'c'): ('acc', 0),
        (2, 'd'): ('bcd', 0),
    }
    object = spe_to_fst("a", "b", "", "cd")
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet

    input_list = [
        "",
        "acd",
        "bcd",
        "qwertyuiopacd",
        "awe",
        "acipiqp",
        "qwertyuiop",
        "acdqwertyuiop",
        "acdb",
        "acdqwertyuiop",
    ]
    output_list = [
        "",
        "bcd",
        "bcd",
        "qwertyuiopbcd",
        "awe",
        "acipiqp",
        "qwertyuiop",
        "bcdqwertyuiop",
        "bcdb",
        "bcdqwertyuiop",
    ]
    run_test_on_strings(input_list, output_list, object)

# Added by Travis
def test_spe_to_fst_a_b_empty_d():
    alphabet = {'a', 'b', 'd'}
    states = {0: '', 1: 'a'}
    transitions = {
        (0, 'b'): ('b', 0),
        (0, 'd'): ('d', 0),
        (0, '?'): ('?', 0),
        (0, 'a'): ('', 1),
        (1, 'a'): ('aa', 1),
        (1, 'd'): ('bd', 0),
        (1, 'b'): ('ab', 0),
        (1, '?'): ('a?', 0)
    }
    object = spe_to_fst("a", "b", "", "d")
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet

    input_list = [
        "",
        "ad",
        "abad",
        "adcadc",
        "qwer",
        "qweraddabc",
    ]
    output_list = [
        "",
        "bd",
        "abbd",
        "bdcbdc",
        "qwer",
        "qwerbddabc",
    ]
    run_test_on_strings(input_list, output_list, object)

# Added by Travis
def test_spe_to_fst_a_b_c_empty():
    alphabet = {'a', 'b', 'c'}
    states = {0: '', 1: 'c'}
    transitions = {
        (0, 'a'): ('a', 0),
        (0, 'b'): ('b', 0),
        (0, '?'): ('?', 0),
        (0, 'c'): ('c', 1),
        (1, 'c'): ('c', 1),
        (1, 'a'): ('b', 0),
        (1, 'b'): ('b', 0),
        (1, '?'): ('?', 0)
    }
    object = spe_to_fst("a", "b", "c", "")
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet

def test_spe_to_fst_a_b_cde_empty():
    alphabet = {'a', 'b', 'c', 'd', 'e'}
    states = {0: '', 1: 'c', 2: 'cd', 3: 'cde'}
    transitions = {
        (0, '?'): ('?', 0),
        (0, 'a'): ('a', 0),
        (0, 'b'): ('b', 0),
        (0, 'c'): ('c', 1),
        (0, 'd'): ('d', 0),
        (0, 'e'): ('e', 0),
        (1, '?'): ('?', 0),
        (1, 'a'): ('a', 0),
        (1, 'b'): ('b', 0),
        (1, 'c'): ('c', 1),
        (1, 'd'): ('d', 2),
        (1, 'e'): ('e', 0),
        (2, '?'): ('?', 0),
        (2, 'a'): ('a', 0),
        (2, 'b'): ('b', 0),
        (2, 'c'): ('c', 1),
        (2, 'd'): ('d', 0),
        (2, 'e'): ('e', 3),
        (3, '?'): ('?', 0),
        (3, 'a'): ('b', 0),
        (3, 'b'): ('b', 0),
        (3, 'c'): ('c', 1),
        (3, 'd'): ('d', 0),
        (3, 'e'): ('e', 0),
    }
    object = spe_to_fst("a", "b", "cde", "")
    assert object.states == states
    assert object.transitions == transitions
    assert object.alphabet == alphabet

    input_list = [
        "",
        "caq",
        "cdaq",
        "cdeaq",
        "deaq",
        "eaq",
        "cdacdeacdacac",
    ]
    output_list = [
        "",
        "caq",
        "cdaq",
        "cdebq",
        "deaq",
        "eaq",
        "cdacdebcdacac",
    ]
    run_test_on_strings(input_list, output_list, object)
