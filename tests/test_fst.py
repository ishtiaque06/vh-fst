from vh_fst import FST
from vh_patterns_dataset import vh_dataset
from processors import preprocess, postprocess, split_word_components
from unicode_variable_repr import *

def run_test_on_strings(input_list, output_list, object):
    for i in range(len(input_list)):
        string = input_list[i]
        word_as_list, prefix_as_list, stem_as_list, suffix_as_list = \
            split_word_components(string)
        proceed, preprocessed = \
            preprocess(word_as_list, prefix_as_list, stem_as_list, suffix_as_list, object)
        if proceed:
            assert output_list[i] == postprocess(object.step(preprocessed), object)
        else:
            assert output_list[i] == "".join(preprocessed)

def test_kisa_applicative():
    kisa_app = vh_dataset[1]
    object = FST(kisa_app)
    assert object.states == kisa_app['states']
    assert object.alphabet == kisa_app['alphabet']
    assert object.transitions == kisa_app['transitions']
    assert object.name == "Kisa applicative suffix Vlɑ"

    input_list = ["t s o m i l a", "r e k e l a", "b i s i l a", "", "b o b i s i l a"]
    output_list = ["tsomelɑ", "rekelɑ", "bisilɑ", "", "bobisilɑ"]
    run_test_on_strings(input_list, output_list, object)

def test_kisa_reversative():
    kisa_rev = vh_dataset[2]
    object = FST(kisa_rev)
    assert object.states == kisa_rev['states']
    assert object.alphabet == kisa_rev['alphabet']
    assert object.transitions == kisa_rev['transitions']
    assert object.preprocess_req == kisa_rev['preprocess_req']
    assert object.postprocess_req == kisa_rev['postprocess_req']
    assert object.left_subseq == kisa_rev['left_subseq']
    assert object.name == "Kisa reversative suffix Vlɑ"

    input_list = ["", "t s o m u l o", "o f u n g u l a", "r e k u l a"]
    output_list = ["", "tsomolɑ", "ofungulɑ", "rekulɑ"]
    run_test_on_strings(input_list, output_list, object)

def test_sibe_vowel_rounding():
    sibe = vh_dataset[3]
    object = FST(sibe)
    assert object.states == sibe['states']
    assert object.alphabet == sibe['alphabet']
    assert object.transitions == sibe['transitions']
    assert object.preprocess_req == sibe['preprocess_req']
    assert object.postprocess_req == sibe['postprocess_req']
    assert object.left_subseq == sibe['left_subseq']
    assert object.name == "Sibe vowel rounding harmony"

    input_list = ["", C_H_U_T+" l d u k i n", "m u x u l i"]
    output_list = ["", "ɨldɨkin", "muxuly"]
    run_test_on_strings(input_list, output_list, object)

def test_tuvan():
    language = vh_dataset[4]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Tuvan backness harmony"

    input_list = ["", "i v u e", "a d e g l", "i r u d o a"]
    output_list = ["", "ivye", "adagl", "iryd"+F_M_R_T+"e"]
    run_test_on_strings(input_list, output_list, object)

def test_jingulu():
    language = vh_dataset[9]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Jingulu nominal root with non-neuter gender suffix"

    input_list = ["", "w a r k u -rny", "a n k i l a -r n y", "a n k i l a -r a"]
    output_list = ["", "warkurny", "ankilarny", "ankilara"]
    run_test_on_strings(input_list, output_list, object)

def test_hahl():
    language = vh_dataset[8]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Halh (Mongolic) rounding harmony"

    input_list = ["", "o g b a", "o g u b a", "a t u t i"]
    output_list = ["", "ogbo", "ogube", "at"+B_H_R_NT+"ti"]
    run_test_on_strings(input_list, output_list, object)

def test_uyghur_back():
    language = vh_dataset[5]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Uyghur backness harmony"

    input_list = ["", "y d i", "u y d i", "u d i y"]
    output_list = ["", "ydy", "uudu", "udii"]
    run_test_on_strings(input_list, output_list, object)

def test_uyghur_plural():
    language = vh_dataset[6]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Uyghur plural suffix -lVr"

    input_list = ["", "e d y g g g"]
    output_list = ["", "edil"+B_L_U_NT+"r"]
    run_test_on_strings(input_list, output_list, object)

def test_uyghur_dative():
    language = vh_dataset[7]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Uyghur dative suffix -'+U_F_V+'V'

    input_list = ["", "y t a v v", "y t o v v", "u d i v v", "i g o t i l u r"]
    output_list = ["", "ytaga", "yt"+F_M_R_T+"ga", "udi"+U_F_V+B_L_U_NT,
        "igotil"+U_F_V+B_L_U_NT]
    run_test_on_strings(input_list, output_list, object)

def test_kalmyk():
    language = vh_dataset[17]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Kalmyk (Oirat) harmony'

    input_list = ['',
                    't i i m i',
                    't i i m i - t a n',
                    't i m y - t e',
                    't i m y - t o',
                    't o m i m y',
                    't a m - e '+F_M_R_T,
                    't a m + e '+F_M_R_T,
                    'e + t a m - o',
                 ]
    output_list = ['',
                    'tiimi',
                    'tiimit'+F_L_U_T+'n',
                    'timyt'+F_M_R_T,
                    'timyt'+F_M_R_T,
                    'tomimu',
                    'tamoo',
                    'tamoo',
                    'etæmø'
                    ]
    run_test_on_strings(input_list, output_list, object)
