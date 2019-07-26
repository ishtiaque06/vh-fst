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

def test_jingulu_non_neuter():
    language = vh_dataset[9]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == "Jingulu nominal root with non-neuter gender suffix"

    input_list = ["",
                    "w a r k u -rny",
                    "a n k i l a -r n y",
                    "a n k i l a -r a",
                    "b a - a l i ",
                    "b u a - d i u",
                    "b a u a - i",
                    "b a d a - u i",
                    ]
    output_list = ["",
                    "warku-rny",
                    "ankila-rny",
                    "ankila-ra",
                    "bi-ali",
                    "bui-diu",
                    "baui-i",
                    "bidi-ui"
                    ]
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
                    f'd i b - e d æ b u o g a d ø b y',
                    f'd i b u a - b i y e d ø g æ b u a'
                 ]
    output_list = ['',
                    'tiimi',
                    'tiimi-t'+F_L_U_T+'n',
                    'timy-t'+F_M_R_T,
                    'timy-t'+F_M_R_T,
                    'tomimu',
                    'tam-oo',
                    'tam+oo',
                    'e+tæm-ø',
                    'dib-edæbyøgædøby',
                    'dibua-biuodogabua'
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_turkish():
    language = vh_dataset[14]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Turkish palatal and rounding vowel harmony'

    input_list = ['',
                    't i m e y - i o',
                    f'o d {B_H_U_T} e n + b {B_L_U_NT}',
                 ]
    output_list = ['',
                    'timei-iø',
                    'oduɑn+bɑ',
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_finnish():
    language = vh_dataset[15]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Finnish palatal (front/back) vowel harmony'

    input_list = ['',
                    f'd u d i n u o ɑ b y ø æ',
                    f'd i + n y i ɑ m - o g ɑ',
                 ]
    output_list = ['',
                    'dudinuoɑbuoɑ',
                    'di+nyiæm-øgæ',
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_mongolian():
    language = vh_dataset[16]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Classical Mongolian palatal vowel harmony'

    input_list = ['',
                    f't i + d e ø y d u o a',
                    f't u b o a k y ø e - d a',
                 ]
    output_list = ['',
                    'ti+deøydyøe',
                    'tuboakuoa-da'
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_khalka():
    language = vh_dataset[18]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Khalkha Mongolian harmony'

    input_list = ['',
                    # f't i + d e ø y d u o a',
                    # f't u b o a k y ø e - d a',
                    f'g i + ɔ b - i d ɔ a e d o ʊ e',
                    'g u b i d ʊ u b e g o a ɔ',
                 ]
    output_list = ['',
                    # 'ti+deøydyøe',
                    # 'tuboakuoa-da'
                    f'gi+ɔb-idɔɔɔdɔʊa',
                    'gubiduubegeee',
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_dagur():
    language = vh_dataset[19]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Dagur Mongolian harmony'

    input_list = ['',
                    f'b i ɔ d a - ə u ɔ',
                    f'b u d ə a ɔ'
                 ]
    output_list = ['',
                    'biɔdɔ-ɔɔɔ',
                    'budəəu'
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_tunica():
    language = vh_dataset[20]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Tunica harmony'

    input_list = ['',
                    f'b i ʔ o ɑ d u h ɛ',
                    f'b o h i ʔ e h ɛ d ɔ - i h ɛ',
                    'b o h i h',
                 ]
    output_list = ['',
                    'biʔɛduhɔ',
                    'bohuʔohɔduhɔ',
                    'bohuh',
                    ]
    run_test_on_strings(input_list, output_list, object)
    
def test_yoruba():
    language = vh_dataset[21]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Yoruba ATR harmony'

    input_list = ['',
                    f'p ɛ a l i o + b o d i ɛ',
                    f'p ɛ a l i o + b o d ɛ',
                    f'p e o + a d ɔ ɛ - e',
                 ]
    output_list = ['',
                    'pealio+bodiɛ',
                    'pɛaliɔ+bɔdɛ',
                    'pɛɔ+adoe-e',
                    ]
    run_test_on_strings(input_list, output_list, object)
  
def test_igbo():
    language = vh_dataset[22]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Igbo ATR harmony'

    input_list = ['',
                    f'p I i {B_H_R_NT} u e a {B_M_R_NT} o + e - {B_M_R_NT} o e a {B_H_R_NT} u I i',
                    f'p I + i {B_H_R_NT} u e a {B_M_R_NT} o + e v a - {B_M_R_NT} e u I i + o {B_H_R_NT}',
                    f'p i - I + a v e - + i v I p',
                 ]
    output_list = ['',
                    'piiuueeoo+e-ooeeuuii',
                    'pi+iuueeoo+eva-'+B_M_R_NT+'a'+B_H_R_NT+'II'+B_M_R_NT+B_H_R_NT',
                    'pII+ave-ivip',
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_diolafogny():
    language = vh_dataset[23]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Diola-Fogny ("Jola-Fonyi") ATR harmony'

    input_list = ['',
                    f'I b {F_M_U_NT} d a g {B_M_R_NT} d {B_H_R_NT}',
                    f'i b e d {schwa} g o d u',
                    f'I b e d a g {B_M_R_NT} d {B_H_R_NT}',
                    f'I b {F_M_U_NT} d a g {B_M_R_NT} d u',
                    f'I b + {F_M_U_NT} d a g {B_M_R_NT} - d u',
                 ]
    output_list = ['',
                    'Ib'+F_M_U_NT+'dag'+B_M_R_NT+'d'+B_H_R_NT,
                    'ibed'+schwa+'godu',
                    'ibed'+schwa+'godu',
                    'ibed'+schwa+'godu',
                    'ib+ed'+schwa+'go-du',
                    ]
    run_test_on_strings(input_list, output_list, object)
    

def test_kalenjin():
    language = vh_dataset[24]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Kalenjin ATR harmony'

    input_list = ['',
                    f'g I + b {F_M_U_NT} + m e d i b {Long_C_L_U_T} - k a - d i - b I - {Long_F_M_U_T} - g u',
                    f'g I + b {F_M_U_NT} + u n - k a - d I - k a j - {F_M_U_NT}',
                    f'g I + m a + m {F_M_U_NT} + u g + - k e',
                    
                 ]
    output_list = ['',
                    'gI+b'+F_M_U_NT+'+m'+F_M_U_NT+'+dIb'+Long_C_L_U_NT+'-ka-dI-bI-'+Long_F_M_U_NT+'-g'+B_H_R_NT,
                    'gi+be+un-k'+C_L_U_T+'-di-kaj-'+F_M_U_NT,
                    'gI+ma+me+ug+-ke',
                    
                    ]
    run_test_on_strings(input_list, output_list, object)
    
def test_lena():
    language = vh_dataset[25]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Asturian Lena (Romance) height harmony with inflectional suffixes'

    input_list = ['',
                    f"d a ' b e ' - g i",
                    f"d a ' b e ' - g u",
                    f"d a ' b e ' - g u '",
                    f"d a ' b e - g u b",
                    f"b o ' - d a d h - g u",
                    f"d a ' b ' e - g u",
                    
                 ]
    output_list = ['',
                    "d a ' b e ' - g i",
                    "d a ' b i ' - g u",
                    "d a ' b i ' - g u '",
                    "d e ' b e - g u b",
                    "b u ' - d a d h - g u",
                    "d e ' b ' e - g u",
                    ]
    run_test_on_strings(input_list, output_list, object)
    
def test_pasiego():
    language = vh_dataset[26]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Pasiego vowel harmony (metaphony, raising, and centralization)'

    input_list = ['',
                    f"e j + o d e ' - u",
                    f"e + j o d u e + '",
                    f"e j o ' - d u - e '",
                    f"e d o ' d u e '",
                    
                    
                 ]
    output_list = ['',
                    f"e j + {Cent_B_H_R_T} d {Cent_F_H_U_T} ' - {Cent_B_H_R_T}",
                    f"e + j u d u e + '",
                    f"i j u ' - d u - e '",
                    f"i d u ' d u e '",
                    
                    ]
    run_test_on_strings(input_list, output_list, object)

def test_pulaar():
    language = vh_dataset[27]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Pulaar dialect of Fula (Niger-Congo) ATR harmony'

    input_list = ['',
                    f"{B_M_R_NT} {F_M_U_NT} i d + {F_M_U_NT} o d e - {B_M_R_NT}",
                    f"{B_M_R_NT} {F_M_U_NT} + a + i d {F_M_U_NT} o - d e {B_M_R_NT}",
                    f"{B_M_R_NT} a {B_M_R_NT} d e",
                    
                    
                    
                 ]
    output_list = ['',
                    f"o e i d + {F_M_U_NT} {B_M_R_NT} d {F_M_U_NT} - {B_M_R_NT}",
                    f"{B_M_R_NT} {F_M_U_NT} + a + i d {F_M_U_NT} {B_M_R_NT} - d {F_M_U_NT} {B_M_R_NT}",
                    f"{B_M_R_NT} a o d e",
                    
                    
                    ]
    run_test_on_strings(input_list, output_list, object)
    
def test_maasai():
    language = vh_dataset[28]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Maasai (Eastern Nilotic) ATR harmony'

    input_list = ['',
                    f"i I + u I o - b {B_L_U_NT} - g {F_M_U_NT} {B_M_R_NT} e",
                    f"i I + u I {B_L_U_NT} - b o - g {F_M_U_NT}",
                    f"u I {B_L_U_NT} - b I - b o - g {F_M_U_NT}",
                    
                    
                    
                 ]
    output_list = ['',
                    f"i i + u i o - b o - g e o e",
                    f"i i + u I {B_L_U_NT} - b o - g {F_M_U_NT}",
                    f"u I {B_L_U_NT} - b i - b o - g {F_M_U_NT}",
                    
                    
                    ]
    run_test_on_strings(input_list, output_list, object)
    
def test_kashaya():
    language = vh_dataset[29]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Kashaya (Pomoan) translaryngeal harmony'

    input_list = ['',
                    f"m - i d i {G_P_VL} {Long_C_L_U_NT} q o",
                    f"m a + h e {G_P_VL} {Long_F_H_U_T} {G_P_VL} u h o e",
                    f"q u q {Long_F_H_U_T} q e q o q a d i h {Long_B_M_R_T}",
                    
                    
                    
                 ]
    output_list = ['',
                    f"m - a d u {G_P_VL} {Long_B_H_R_T} q a",
                    f"m a + h a {G_P_VL} {Long_C_L_U_NT} {G_P_VL} a h a a",
                    f"q a q {Long_C_L_U_NT} q a q a q a d u h u",
                    
                    
                    ]
    run_test_on_strings(input_list, output_list, object)
    
def test_stdhungarian():
    language = vh_dataset[30]
    object = FST(language)
    assert object.states == language['states']
    assert object.alphabet == language['alphabet']
    assert object.transitions == language['transitions']
    assert object.preprocess_req == language['preprocess_req']
    assert object.postprocess_req == language['postprocess_req']
    assert object.left_subseq == language['left_subseq']
    assert object.name == 'Standard Hungarian palatal harmony of alternating suffixes'

    input_list = ['',
                    f"b u + n - {Long_B_H_R_T} d i - y - {B_M_R_NT}",
                    f"n i n u - y {F_M_U_NT} - o",
                    f"n i - u y - {Long_C_L_U_NT}",
                    f"n y - u y - {Long_B_M_R_T}",
                    f"u i d e - u y",
                    f"u d e - u y",
                    f"y i i n {F_M_U_NT} e - u y",
                    
                    
                 ]
    output_list = ['',
                    f"b u + n - {Long_F_H_R_T} d i - y - {F_M_U_NT}",
                    f"n i n u - u {B_M_R_NT} - o",
                    f"n i - y y - {Long_F_M_U_T}",
                    f"n y - y y - {Long_F_M_R_T}",
                    f"u i d e - y y",
                    f"u d e - u u",
                    f"y i i n {F_M_U_NT} e - y y",
                    
                    ]
    run_test_on_strings(input_list, output_list, object)
