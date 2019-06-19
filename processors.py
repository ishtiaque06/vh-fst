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
    if string.count("+") > 1 or string.count("-") > 1:
        print ("Your word contains more than one prefix or suffix.")
        return False, []
    # if there is both a prefix and a suffix
    if (len(string.split("+")) == 2) and (len(string.split("-")) == 2):
        prefix_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("+")[0].split(" ") if ch != ""]
            )
        rest = string.split("+")[1]
        stem_as_list = convert_chars_to_unicode(
            [ch for ch in rest.split("-")[0].split(" ") if ch != ""]
            )
        suffix_as_list = convert_chars_to_unicode(
            [ch for ch in rest.split("-")[1].split(" ") if ch != ""]
            )
        word_as_list = prefix_as_list + stem_as_list + suffix_as_list

        fst.prefix = prefix_as_list
        fst.suffix = suffix_as_list

    # if it only has prefix
    elif len(string.split("+")) == 2:
        # Get all characters in prefix
        prefix_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("+")[0].split(" ") if ch != ""]
            )
        stem_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("+")[1].split(" ") if ch != ""]
            )
        word_as_list = prefix_as_list + stem_as_list

        fst.prefix = prefix_as_list

    # if it only has a suffix
    elif len(string.split("-")) == 2:
        # Get all characters in suffix
        suffix_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("-")[1].split(" ") if ch != ""]
            )
        stem_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("-")[0].split(" ") if ch != ""]
            )
        word_as_list = stem_as_list + suffix_as_list

        fst.suffix = suffix_as_list

    # if it doesn't have a prefix or a suffix
    else:
        word_as_list = convert_chars_to_unicode(
            [ch for ch in string.split(" ") if ch != ""]
            )

    # empty input
    if word_as_list == []:
        return False, []

    # if preprocessing isn't required on the input string
    if not fst.preprocess_req:
        return True, word_as_list

    # Preprocessing for left-subsequential languages
    if fst.left_subseq:

        if fst.name == "Kisa applicative suffix Vlɑ"\
            or fst.name == "Kisa reversative suffix Vlɑ":
            return True, word_as_list[:-3]

        elif fst.name in {"Uyghur backness harmony",
            "Uyghur plural suffix -lVr", 'Uyghur dative suffix -'+U_F_V+'V'}:
            # run the preprocess step
            preliminary_fst = FST('5P')
            if fst.name == "Uyghur backness harmony":
                return True, preliminary_fst.step(word_as_list)
            elif fst.name == "Uyghur plural suffix -lVr":
                word_as_list = word_as_list[:-3]
                return True, preliminary_fst.step(word_as_list)
            elif fst.name == 'Uyghur dative suffix -'+U_F_V+'V':
                word_as_list = word_as_list[:-2]
                return True, preliminary_fst.step(word_as_list)
        elif fst.name == "Halh (Mongolic) rounding harmony":
            # run the preprocess step
            preliminary_fst = FST('8P')
            return True, preliminary_fst.step(word_as_list)

        else:
            return True, word_as_list

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
                return False, word_as_list

        return True, stem_as_list[::-1]


# Post-process a list after the FST runs through it.
def postprocess(lst, fst):
    if not fst.left_subseq:
        lst = lst[::-1]
    if fst.hyphenate_suffix:
        if hasattr(fst, "suffix"):
            lst.append("".join(fst.suffix))
    return "".join(lst)


'''AI--------------------------------------------------------------------------
    Given a list of characters, convert any unicode variables to its unicode repr
    Input: List of characters
    Output: List of characters, with the ones specified as variable names replaced
        with the actual unicode representation
--------------------------------------------------------------------------AI'''
def convert_chars_to_unicode(lst):
    output = []
    for ch in lst:
        try:
            output.append(globals()[ch])
        except KeyError:
            output.append(ch)
    return output
