from vh_fst import FST
from vh_patterns_dataset import vh_dataset
from processors import preprocess, postprocess, convert_chars_to_unicode
from unicode_variable_repr import *


def test_convert_chars_to_unicode():
    lst = ["R_P_VL", "i", "F_M_R_NT", "z", "l", "b", "Long_F_H_R_T"]
    lst = convert_chars_to_unicode(lst)
    assert lst == ['ʈ', 'i', 'œ', 'z', 'l', 'b', 'yː']
