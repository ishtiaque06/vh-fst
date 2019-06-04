from vh_fst import FST

def test_kisa_applicative():
    object = FST("Kisa applicative suffix")
    assert object.states == [(0,'ila'),(1,'ila'),(2,'ela')]
    assert object.alphabet == ['i','e','u','o']
    assert object.transitions == [(0,'?','?',0), (0,'i','i',1),(0,'u','u',1),
                                (0,'e','e',2),(0,'o','o',2),(1,'i','i',1),
                                (1,'u','u',1),(1,'?','?',1),(1,'e','e',2),
                                (1,'o','o',2),(2,'?','?',2),(2,'e','e',2),
                                (2,'o','o',2),(2,'i','i',1),(2,'u','u',1)
                                ]
    assert object.preprocess_req == True
    assert object.postprocess_req == False
    assert object.left_subseq == True
