from vh_fst import FST
from vh_patterns_dataset import vh_dataset
from app import preprocess, postprocess

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
    for i in range(len(input_list)):
        preprocessed = preprocess(input_list[i], object)
        assert output_list[i] == postprocess(object.step(preprocessed), object)
