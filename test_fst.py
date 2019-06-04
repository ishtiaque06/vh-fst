from vh_fst import FST, uc

def test_kisa_applicative():
    object = FST("Kisa applicative suffix")
    assert object.states =={0: 'il'+uc(0x03b1),
                            1: 'il'+uc(0x03b1),
                            2: 'el'+uc(0x03b1)}
    assert object.alphabet == ['i','e','u','o']
    assert object.transitions == {(0,'?'): ('?',0), (0,'i'): ('i',1),
                                (0,'u'): ('u', 1),(0,'e'):('e',2),
                                (0,'o'): ('o',2), (1,'i'): ('i',1),
                                (1,'u'): ('u',1), (1,'?'): ('?',1),
                                (1,'e'): ('e',2), (1,'o'): ('o',2),
                                (2,'?'): ('?',2), (2,'e'): ('e',2),
                                (2,'o'): ('o',2), (2,'i'): ('i',1),
                                (2,'u'): ('u',1)
                                }
    assert object.preprocess_req == True
    assert object.postprocess_req == False
    assert object.left_subseq == True
    assert object.name == "Kisa applicative suffix"

    input = ["i", "t", "u", "k", "i", "l", "a"]
    preprocessed = object.preprocess(input)
    assert preprocessed == ["i", "t", "u", "k"]

    postprocessed = object.postprocess(input)
    assert postprocessed == input

    input_list = ["tsomila", "rekela", "bisila", "", "bobisila"]
    output_list = ["tsomelα", "rekelα", "bisilα", "", "bobisilα"]
    for i in range(len(input_list)):
        assert output_list[i] == object.convert(input_list[i])
