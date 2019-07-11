from vh_fst import FST
from vh_patterns_dataset import vh_dataset
from processors import (
    preprocess,
    postprocess,
    convert_chars_to_unicode,
    split_word_components
    )
from unicode_variable_repr import *


def test_convert_chars_to_unicode():
    lst = ["R_P_VL", "i", "F_M_R_NT", "z", "l", "b", "Long_F_H_R_T"]
    lst = convert_chars_to_unicode(lst)
    assert lst == ['ʈ', 'i', 'œ', 'z', 'l', 'b', 'yː']


def test_split_prefix():
    string = "w o r + d w i"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == ['w', 'o', 'r', '+', 'd', 'w', 'i']
    assert prefix == [['w', 'o', 'r', '+']]
    assert suffix == []
    assert stem == ['d', 'w', 'i']


def test_stem_only():
    string = "w o r d"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == ['w', 'o', 'r', 'd']
    assert prefix == []
    assert suffix == []
    assert stem == word

def test_split_suffix():
    string = "w o r d - w i n"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == ['w', 'o', 'r', 'd', '-', 'w', 'i', 'n']
    assert prefix == []
    assert suffix == [['-', 'w', 'i', 'n']]
    assert stem == ['w', 'o', 'r', 'd']

def test_split_prefix_and_suffix():
    string = "p r e + s t e m - s u f"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == ['p', 'r', 'e', '+', 's', 't', 'e', 'm', '-', 's', 'u', 'f']
    assert prefix == [['p', 'r', 'e', '+']]
    assert stem == ['s', 't', 'e', 'm']
    assert suffix == [['-', 's', 'u', 'f']]

def test_invalid_word_multiple_affixes():
    string = "h e - - l o +"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == []
    assert stem == []
    assert prefix == []
    assert suffix == []

def test_suffix_before_prefix():
    string = "w o r - d h u + s u f"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == []
    assert stem == []
    assert prefix == []
    assert suffix == []

def test_multiple_prefixes():
    string = "w o r + d a n + o t + e a u w p q u a"
    word, prefix, stem, suffix = split_word_components(string)
    assert word == ['w', 'o', 'r', '+', 'd', 'a', 'n', '+', 'o', 't', '+',
                    'e', 'a', 'u', 'w', 'p', 'q', 'u', 'a']
