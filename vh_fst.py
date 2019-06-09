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
        step:
            Input: <list>: input word
            Output: <list>: final word (before postprocessing) after transitions
                have been applied.
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

    def step(self, word_as_list):
        if word_as_list == []:
            return ['']
        output_list = []
        current_state = 0
        while word_as_list:
            letter = word_as_list[0]
            if letter not in self.alphabet:
                letter = '?'
            output_letter, next_state = self.transitions[(current_state, letter)]
            current_state = next_state
            if output_letter == '?':
                output_list.append(word_as_list[0])
            else:
                output_list.append(output_letter)
            word_as_list = word_as_list[1:]
        output_list.append(self.states[current_state])
        return output_list
