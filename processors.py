from unicode_variable_repr import *
from vh_fst import FST


'''AI--------------------------------------------------------------------------
    Preprocess string after user input
    Input: space-delimited string of Unicode characters and variables
        as represented in unicode_variable_repr.py
    Output: (Boolean, list):
                True, list: Run FST on list of characters
                False, list: output the string without any FST processing
--------------------------------------------------------------------------AI'''
def preprocess(string, fst):
    string_as_list = string.split(" ")
    if string_as_list == ['']:
        return False, []

    if not fst.preprocess_req:
        return True, string_as_list

    # remove any empty strings in the list
    string_as_list = [item for item in string_as_list if item != ""]
    input_list = []

    # Add characters to the input_list, processing unicode variables as it iterates
    # caveat: if a word contains more than one strings with "-" in them, only the
    # last one is processed as the suffix, and the rest are completely ignored.
    # This should be expected behavior for now since words with more than one "-"
    # symbols are invalid words anyway.
    for ch in string_as_list:
        try:
            input_list.append(globals()[ch])
        except KeyError:
            if ch != "":
                if fst.hyphenate_suffix:
                    if "-" in ch:
                        fst.suffix = ch.replace("-", "")
                    else:
                        # if suffix does not contain a hyphen
                        if ch == string_as_list[-1]:
                            print (f"Please enter a word with a hyphenated suffix.")
                            return False, [] # indicate no further processing is to be done.
                        else:
                            input_list.append(ch)
                else:
                    input_list.append(ch)
    # Preprocessing for left-subsequential languages
    if fst.left_subseq:

        if fst.name == "Kisa applicative suffix Vlɑ"\
            or fst.name == "Kisa reversative suffix Vlɑ":
            return True, input_list[:-3]

        elif fst.name in {"Uyghur backness harmony",
            "Uyghur plural suffix -lVr", 'Uyghur dative suffix'+U_F_V+'V'}:
            # run the preprocess step
            preliminary_fst = FST('5P')
            if fst.name == "Uyghur backness harmony":
                return True, preliminary_fst.step(input_list)
            elif fst.name == "Uyghur plural suffix -lVr":
                input_list = input_list[:-3]
                return True, preliminary_fst.step(input_list)
            elif fst.name == 'Uyghur dative suffix'+U_F_V+'V':
                input_list = input_list[:-2]
                return True, preliminary_fst.step(input_list)
            # return True, preliminary_fst.step(input_list)
        elif fst.name == "Halh (Mongolic) rounding harmony":
            # run the preprocess step
            preliminary_fst = FST('8P')
            return True, preliminary_fst.step(input_list)

        else:
            return True, input_list

    # Preprocessing for right-subseuential languages
    elif not fst.left_subseq:

        # languages 9,10,11,12,13
        if fst.name in {
            'Jingulu nominal root with non-neuter gender suffix',
            'Jingulu adjectivial root with non-neuter gender suffix',
            'Jingulu verbal root with subject agreement-marking suffix',
            'Jingulu verbal root with motion-imperative suffix',
            'Jingulu verbal root with negative imperative suffix',
        }:
            if not "u" in fst.suffix and not "i" in fst.suffix:
                input_list.append(fst.suffix)
                return False, input_list

        return True, input_list[::-1]


# Post-process a list after the FST runs through it.
def postprocess(lst, fst):
    if not fst.left_subseq:
        lst = lst[::-1]
    if fst.hyphenate_suffix:
        if hasattr(fst, "suffix"):
            lst.append(fst.suffix)
    return "".join(lst)
