from unicode_variable_repr import *
from vh_fst import FST


'''AI--------------------------------------------------------------------------
    Preprocess string after user input
    Input: <type 'list' x4>, <type 'FST'>
    Output: (Boolean, list):
                True, list: Run FST on list of characters
                False, list: output the string without any FST processing
--------------------------------------------------------------------------AI'''
def preprocess(
                word_as_list,
                prefix_as_list,
                stem_as_list,
                suffix_as_list,
                fst
    ):
    fst.prefix = prefix_as_list
    fst.suffix = suffix_as_list

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

        elif fst.name == "Kalmyk (Oirat) harmony":
            '''AI---------------------------------------------------------------
                Rules for language 17
            ---------------------------------------------------------------AI'''
            # If there is a suffix, hyphenate
            # Check if i is the only type of vowel in the stem
            #     if not, run stem + suffix through 17
            #     if yes, don't process the stem. Input the suffix into 17P.
            #       Output is the stored stem + output of 17P
            alphabet_as_set = set(fst.alphabet)
            vowels_in_stem = set()
            for ch in stem_as_list:
                if ch in fst.alphabet:
                    vowels_in_stem.add(ch)
            if vowels_in_stem.intersection(alphabet_as_set) != {'i'}:
                return True, word_as_list
            else:
                preliminary_fst = FST('17P')
                fst.suffix = preliminary_fst.step(suffix_as_list)
                return False, stem_as_list + fst.suffix

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
def postprocess(word_as_list, fst):
    if fst.postprocess_req:
        if not fst.left_subseq:
            word_as_list = word_as_list[::-1]
        if fst.hyphenate_suffix:
            # print ("hyphenate")
            if hasattr(fst, "suffix"):
                word_as_list.append("".join(fst.suffix))
    return "".join(word_as_list)


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


'''AI--------------------------------------------------------------------------
    Given a space-delimited string, return prefix, suffix, stem and word
    Input: <type 'string'>
    Output: <type 'list' x4>
--------------------------------------------------------------------------AI'''
def split_word_components(string):
    if string.count("+") > 1 or string.count("-") > 1:
        print ("Your word contains more than one prefix or suffix.")
        return [], [], [], []

    # if there is both a prefix and a suffix
    if (len(string.split("+")) == 2) and (len(string.split("-")) == 2):
        if string.find('-') < string.find('+'):
            print ("Please enter the prefix before the suffix.")
            return [], [], [], []

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
        suffix_as_list = []

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
        prefix_as_list = []

    # if it doesn't have a prefix or a suffix
    else:
        word_as_list = convert_chars_to_unicode(
            [ch for ch in string.split(" ") if ch != ""]
            )
        prefix_as_list = []
        stem_as_list = word_as_list
        suffix_as_list = []
    return word_as_list, prefix_as_list, stem_as_list, suffix_as_list
