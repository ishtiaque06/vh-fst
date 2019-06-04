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
        self.name: <str> Type of vowel-harmony pattern this FST represents


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

        self.name = language
        if language == "Kisa applicative suffix":
            self.states =  {0: 'il'+uc(0x03b1),
                            1: 'il'+uc(0x03b1),
                            2: 'el'+uc(0x03b1)}
            self.alphabet = ['i','e','u','o']
            self.transitions = {(0, '?'): ('?', 0), (0, 'i'): ('i', 1),
                                (0, 'u'): ('u', 1), (0, 'e'): ('e', 2),
                                (0, 'o'): ('o', 2), (1, 'i'): ('i', 1),
                                (1, 'u'): ('u', 1), (1, '?'): ('?', 1),
                                (1, 'e'): ('e', 2), (1, 'o'): ('o', 2),
                                (2, '?'): ('?', 2), (2, 'e'): ('e', 2),
                                (2, 'o'): ('o', 2), (2, 'i'): ('i', 1),
                                (2, 'u'): ('u', 1)}
            self.left_subseq = True
            self.preprocess_req = True
            self.postprocess_req = False
        elif language == "Kisa reversative suffix":
            self.states =  {0: 'ul'+uc(0x03b1),
                            1: 'ul'+uc(0x03b1),
                            2: 'ol'+uc(0x03b1)}
            self.alphabet = ['u', 'o']
            self.transitions = {(0, '?'): ('?', 0), (0, 'u'): ('u', 1),
                                (0, 'o'): ('o', 2), (2, 'u'): ('u', 1),
                                (1, 'o'): ('o', 2), (1, '?'): ('?', 1),
                                (2, '?'): ('?', 2)}
            self.left_subseq = True



    def preprocess(self, word_as_list):
        if self.preprocess_req:
            # Preprocess according to rules
            if self.name == "Kisa applicative suffix":
                return word_as_list[:-3] # return the word except the -ila suffix

        else:
            # return word as is.
            return word_as_list

    def postprocess(self, word_as_list):
        if self.postprocess_req:
            return word_as_list # Do something
        else:
            return word_as_list # Return word as is.

    def step(self, word_as_list):
        output_list = []
        current_state = 0
        while word_as_list:
            letter = word_as_list[0]
            if letter not in self.alphabet:
                output_list.append(letter)
                letter = '?'
            else:
                output_list.append(letter)
            output_letter, next_state = self.transitions[(current_state, letter)]
            current_state = next_state
            word_as_list = word_as_list[1:]
        output_list.append(self.states[current_state])
        return output_list



    def convert(self, word):
        if word == "":
            return ""
        word_as_list = list(word) # Convert string to list

        if self.preprocess_req:
            word_as_list = self.preprocess(word_as_list)

        word_converted = self.step(word_as_list)

        if self.postprocess_req:
            word_converted = self.postprocess(word_converted)

        return "".join(word_converted) # Return word represented as string


# Outputs string representation of a unicode hex representation
def uc(hex):
    return chr(int(hex))
