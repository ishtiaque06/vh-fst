from vh_fst import FST
from vh_patterns_dataset import vh_dataset
from app import preprocess, postprocess
from unicode_variable_repr import *

def run_test_on_strings(input_list, output_list, object):
    for i in range(len(input_list)):
        preprocessed = preprocess(input_list[i], object)
        assert output_list[i] == postprocess(object.step(preprocessed), object)

def test_kisa_applicative():
    object = FST(1)
    kisa_app = vh_dataset[1]
    assert object.states == kisa_app['states']
    assert object.alphabet == kisa_app['alphabet']
    assert object.transitions == kisa_app['transitions']
    assert object.preprocess_req == kisa_app['preprocess_req']
    assert object.postprocess_req == kisa_app['postprocess_req']
    assert object.left_subseq == kisa_app['left_subseq']
    assert object.name == "Kisa applicative suffix"

    input_list = ["tsomila", "rekela", "bisila", "", "bobisila"]
    output_list = ["tsomelɑ", "rekelɑ", "bisilɑ", "", "bobisilɑ"]
    run_test_on_strings(input_list, output_list, object)

def test_kisa_reversative():
    object = FST(2)
    kisa_rev = vh_dataset[2]
    assert object.states == kisa_rev['states']
    assert object.alphabet == kisa_rev['alphabet']
    assert object.transitions == kisa_rev['transitions']
    assert object.preprocess_req == kisa_rev['preprocess_req']
    assert object.postprocess_req == kisa_rev['postprocess_req']
    assert object.left_subseq == kisa_rev['left_subseq']
    assert object.name == "Kisa reversative suffix"

    input_list = ["", "tsomulo", "ofungula", "rekula"]
    output_list = ["", "tsomolɑ", "ofungulɑ", "rekulɑ"]
    run_test_on_strings(input_list, output_list, object)

def test_sibe_vowel_rounding():
    object = FST(3)
    sibe = vh_dataset[3]
    assert object.states == sibe['states']
    assert object.alphabet == sibe['alphabet']
    assert object.transitions == sibe['transitions']
    assert object.preprocess_req == sibe['preprocess_req']
    assert object.postprocess_req == sibe['postprocess_req']
    assert object.left_subseq == sibe['left_subseq']
    assert object.name == "Sibe vowel rounding harmony"

    input_list = ["", C_H_U_T+"ldukin", "muxuli"]
    output_list = ["", "ɨldɨkin", "muxuly"]
    run_test_on_strings(input_list, output_list, object)

def test_tuvan():
    object = FST(4)
    language = vh_dataset[4]
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Tuvan backness harmony"

    input_list = ["", "ivue", "adegl", "irudoa"]
    output_list = ["", "ivye", "adagl", "iryd"+F_M_R_T+"e"]
    run_test_on_strings(input_list, output_list, object)
