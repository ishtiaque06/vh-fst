'''AI--------------------------------------------------------------------------

    =====================================================================
    FST class to map words in a set of languages to their expected vowel
    pronunciations
    =====================================================================

    Attributes:
        states:  <list> of tuples: (state_label, string_to_attach)
        alphabet: <list> of relevant letters in the language (most likely vowels)
        transitions: <tuple>(start_state, input_string, output_string, next_state)
        left_subseq: <boolean> (Is the FST left-subsequential? If not, right sub)
        preprocess_req: <boolean> Preprocessing required on input?
        postprocess_req: <boolean> Postprocessing required on input?


    Methods:
        preprocess:
            Input: <list>: word to preprocess
            Output: <list>: word modified according to preprocessing rules

        postprocess:
            Input: <list>: word to postprocess
            Output: <list>: word modified according to postprocessing rules

        step:
            Input: <list>: input word
            Output: <list>: final word (before postprocessing) after transitions
                have been applied.

        convert:
            Input: <str>: input word from the user
            Output: <str>: Output word in possibly IPA symbols, after postprocessing

            Method dependency: preprocess, postprocess, step 
--------------------------------------------------------------------------AI'''
class FST:

    def __init__(self, language):

        if language == "Kisa applicative suffix":
            self.states = [(0,'ila'), (1,'ila'), (2,'ela')]
            self.alphabet = ['i','e','u','o']
            self.transitions = [(0,'?','?',0), (0,'i','i',1), (0,'u','u',1),
                                (0,'e','e',2), (0,'o','o',2), (1,'i','i',1),
                                (1,'u','u',1), (1,'?','?',1), (1,'e','e',2),
                                (1,'o','o',2), (2,'?','?',2), (2,'e','e',2),
                                (2,'o','o',2), (2,'i','i',1), (2,'u','u',1)
                                ]
            self.left_subseq = True
            self.preprocess_req = True
            self.postprocess_req = False
