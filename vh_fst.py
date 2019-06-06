from vh_patterns_dataset import vh_dataset

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

    def __init__(self, num):

        language = vh_dataset[num]
        self.name = language['name']
        self.states =  language['states']
        self.alphabet = language['alphabet']
        self.transitions = language['transitions']
        self.left_subseq = language['left_subseq']
        self.preprocess_req = language['preprocess_req']
        self.postprocess_req = language['postprocess_req']

    # def preprocess(self, word_as_list):
    #     if self.preprocess_req:
    #         # Preprocess according to rules
    #         if self.name == "Kisa applicative suffix":
    #             return word_as_list[:-3] # return the word except the -ila suffix
    #
    #     else:
    #         # return word as is.
    #         return word_as_list
    #
    # def postprocess(self, word_as_list):
    #     if self.postprocess_req:
    #         return word_as_list # Do something
    #     else:
    #         return word_as_list # Return word as is.

    def step(self, word_as_list):
        if word_as_list == []:
            return ['']
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



    # def convert(self, word):
    #     if word == "":
    #         return ""
    #     word_as_list = list(word) # Convert string to list
    #
    #     if self.preprocess_req:
    #         word_as_list = self.preprocess(word_as_list)
    #
    #     word_converted = self.step(word_as_list)
    #
    #     if self.postprocess_req:
    #         word_converted = self.postprocess(word_converted)
    #
    #     return "".join(word_converted) # Return word represented as string
