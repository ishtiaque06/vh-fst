class FST:
    """
    Finite State Transducer.

    This is class to transform strings in a formal language to a potentially different ones
    given a set of states and transitions. This is quite the general-purpose FST,
    and is designed to work with any language given the parameters in :code:`__init__` method.

    The target of this project is to use this FST to computationally model vowel-harmony patterns.

    *Notes.* Even though it's not much more than a general-purpose FST, its attributes
    :code:`left_subseq`, :code:`preprocess_req` and :code:`postprocess_req`
    are tied to the :code:`preprocess` and :code:`postprocess` functions in the :code:`processors.py`
    module. Since these are booleans, having them initialized as :code:`False` for a general-purpose
    FST class would be enough.
    """

    def __init__(self, language):
        """
            Object initialization method.

            * Input: :code:`<dict>`: Takes in a dictionary containing following attributes:
                * :code:`states``:  :code:`<list>` of tuples: (state_label, string_to_attach)
                * :code:`alphabet`: :code:`<list>` of relevant letters in the language (most likely vowels)
                * :code:`transitions`: :code:`<tuple>` (start_state, input_string, output_string, next_state)
                * :code:`name`: :code:`<str>` Type of vowel-harmony pattern this FST represents
                * :code:`left_subseq`: :code:`<boolean>` (Is the FST left-subsequential? If not, right sub)
                * :code:`preprocess_req`: :code:`<boolean>` Preprocessing required on input?
                * :code:`postprocess_req`: :code:`<boolean>` Postprocessing required on input?
            * Output: :code:`<None>`

        """

        self.name = language['name']
        self.states =  language['states']
        self.alphabet = language['alphabet']
        self.transitions = language['transitions']
        self.left_subseq = language['left_subseq']
        self.preprocess_req = language['preprocess_req']
        self.postprocess_req = language['postprocess_req']

    def step(self, word_as_list):
        """
            Runs the FST given a word represented as a list.

            * Input: :code:`<list>`: input word
            * Output: :code:`<list>`: final word (before postprocessing) after
              transitions have been applied.
        """

        if word_as_list == []:
            return []
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
