from unicode_variable_repr import *
from vh_fst import FST
from vh_patterns_dataset import vh_dataset


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
            preliminary_language = vh_dataset['5P']
            preliminary_fst = FST(preliminary_language)
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
            preliminary_language = vh_dataset['8P']
            preliminary_fst = FST(preliminary_language)
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
                if suffix_as_list != []:
                    preliminary_language = vh_dataset['17P']
                    preliminary_fst = FST(preliminary_language)
                    fst.suffix = preliminary_fst.step(suffix_as_list[0])
                return False, stem_as_list + fst.suffix
        elif fst.name in {
            "Maasai (Eastern Nilotic) ATR harmony",
            "Nawuri (North Guang) ATR harmony"
            }:
            stem_as_list.insert(0, '!')
            stem_as_list.append('&')
            return True, prefix_as_list + stem_as_list + suffix_as_list
        elif fst.name == "Kashaya (Pomoan) translaryngeal harmony":
            fst_p = vh_dataset['29P']
            return True, fst_p.step(word_as_list)
        elif fst.name == "Standard Hungarian palatal harmony of alternating suffixes":
            stem_as_list.insert(0, '!')
            return True, prefix_as_list + stem_as_list + suffix_as_list
        elif fst.name == "Tunica harmony":
            word_as_list.append('#')
            return True, word_as_list
        else:
            return True, word_as_list

    # Preprocessing for right-subsequential languages
    else:

        # languages 9,10,11,12,13
        if fst.name in {
            'Jingulu nominal root with non-neuter gender suffix',
            'Jingulu adjectivial root with non-neuter gender suffix',
            'Jingulu verbal root with subject agreement-marking suffix',
            'Jingulu verbal root with motion-imperative suffix',
            'Jingulu verbal root with negative imperative suffix',
        }:
            return True, word_as_list[::-1]
            # if not "u" in fst.suffix[0] and not "i" in fst.suffix[0]:
            #     return False, word_as_list
            # else:
            #     suffix_start = word_as_list.index('-')
            #     return True, word_as_list[:suffix_start][::-1]
        elif fst.name == 'Yoruba ATR harmony':
            return True, word_as_list[::-1]
        elif fst.name=="Kalenjin ATR harmony":
            language = vh_dataset[24]
            def add_delimiters(affix_list):
                for affix in affix_list:
                    if affix in language['n-a_suff']:
                        affix.insert(0, '&')
                    elif affix in language['n-a_r&pre']:
                        affix.append('!')
                return affix_list
            # prefix pre-processing
            prefix_as_list = add_delimiters(prefix_as_list)
            suffix_as_list = add_delimiters(suffix_as_list)
            stem_as_list = add_delimiters(stem_as_list)
            prefix_flat = []
            [prefix_flat.extend(prefix) for prefix in prefix_as_list]
            prefix_as_list = prefix_flat
            if len(suffix_as_list) >= 1:
                suffix_to_add = suffix_as_list[0]
            else:
                suffix_to_add = []
            return True, (prefix_as_list + stem_as_list + suffix_to_add)[::-1]
            # h e h i + h i + h i + a w q - a e
        elif fst.name==\
            "Asturian Lena (Romance) height harmony with inflectional suffixes":
            return True, word_as_list[::-1]
        return True, word_as_list[::-1]



# Post-process a list after the FST runs through it.
def postprocess(word_as_list, fst):
    if fst.postprocess_req:
        if not fst.left_subseq:
            word_as_list = word_as_list[::-1]
            if fst.name == "Igbo ATR harmony":
                post_fst = FST(vh_dataset['22B'])
                output = post_fst.step(word_as_list)
                word_as_list = output[::-1]
            elif fst.name == "Diola-Fogny (Jola-Fonyi) ATR harmony":
                word_as_list = fst.step(word_as_list)
                word_as_list = word_as_list[::-1]
            elif fst.name == \
                    "Pasiego vowel harmony (metaphony, raising, and centralization)":
                word_as_list = word_as_list[::-1]
                fst_b = FST(vh_dataset['26B'])
                word_as_list = fst_b.step(word_as_list)
                fst_c = FST(vh_dataset['26C'])
                word_as_list = fst_c.step(word_as_list)[::-1]
            elif fst.name == "Kalenjin ATR harmony":
                # reversing this for lazy (but probably not efficient) parsing
                word_as_list = word_as_list[::-1]
                if '+' in word_as_list:
                    final_prefixes = word_as_list[word_as_list.index('+'):][::-1]
                    stem = word_as_list[:word_as_list.index('+')][::-1]
                else:
                    final_prefixes = []
                    stem = word_as_list
                if '-' in stem:
                    stem = stem[:stem.index('-')]
                post_language = vh_dataset['24B']
                post_fst = FST(post_language)
                suffix_as_list = []
                [suffix_as_list.extend(suff) for suff in fst.suffix]
                processed_stem_and_suffix = post_fst.step(stem+suffix_as_list)
                word_as_list = final_prefixes + processed_stem_and_suffix
        else:
            if fst.name == "Maasai (Eastern Nilotic) ATR harmony":
                word_as_list = word_as_list[::-1]
                fst_b = vh_dataset['28B']
                word_as_list = fst_b.step(word_as_list)[::-1]
            if fst.name == "Nawuri (North Guang) ATR harmony":
                fst_b = vh_dataset['31B']
                reversed = word_as_list[::-1]
                word_as_list = fst_b.step(reversed)[::-1]
    return "".join(word_as_list)


def convert_chars_to_unicode(lst):
    """
        Given a list of characters, convert any unicode variables to its unicode repr
        Input: List of characters
        Output: List of characters, with the ones specified as variable names replaced
            with the actual unicode representation
    """
    output = []
    for ch in lst:
        try:
            output.append(globals()[ch])
        except KeyError:
            output.append(ch)
    return output


def split_word_components(string):
    '''
        Given a space-delimited string, return prefix, suffix, stem and word
        Input: <type 'string'>
        Output: <type 'list' x4>
            * word_as_list: list of chars representing the word without affix markers
            * prefix_as_list: list of (list of chars with prefix markers)
            * stem
            * suffix_as_list: list of (list of chars with suffix markers)
    '''

    word_as_list = convert_chars_to_unicode(
        [ch for ch in string.split(" ") if ch != ""]
        )
    # if there is both prefix(es) and suffix(es)
    if ("+" in string) and ("-" in string):
        last_prefix_symbol_loc = \
            [i for i, ltr in enumerate(string) if ltr == '+'][-1]
        first_suffix_symbol_loc = string.find('-')
        if first_suffix_symbol_loc < last_prefix_symbol_loc:
            print ("Please enter the prefix(es) before the suffix(es).")
            return [], [], [], []

        prefixes_as_list = extract_prefixes(string)
        suffixes_as_list = extract_suffixes(string)

        rest = string.split("+")[-1]
        stem_as_list = convert_chars_to_unicode(
            [ch for ch in rest.split("-")[0].split(" ") if ch != ""]
            )

    # if it only has prefix
    elif "+" in string:
        # Get all characters in prefix
        prefixes_as_list = extract_prefixes(string)
        stem_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("+")[-1].split(" ") if ch != ""]
            )
        suffixes_as_list = []

    # if it only has a suffix
    elif len(string.split("-")) == 2:
        # Get all characters in suffix
        suffixes_as_list = extract_suffixes(string)
        stem_as_list = convert_chars_to_unicode(
            [ch for ch in string.split("-")[0].split(" ") if ch != ""]
            )
        prefixes_as_list = []

    # if it doesn't have a prefix or a suffix
    else:
        prefixes_as_list = []
        stem_as_list = word_as_list
        suffixes_as_list = []
    return word_as_list, prefixes_as_list, stem_as_list, suffixes_as_list


def remove_empty_strings(affix_list):
    '''
        excludes empty string from a list of space-delimited affixes
        Example: remove_empty_strings(['h +', ' e +', ' l +'])
                                        => [['h', '+'], ['e', '+'], ['l', '+']]

        Input: list<string>
        Output: list<list<string>>
    '''
    output_list = []
    for str in affix_list:
        temp_list = convert_chars_to_unicode(
            [ch for ch in str.split(" ") if ch != ""]
        )
        output_list.append(temp_list)
    return output_list


def extract_prefixes(word):
    '''
        Inputs a word and outputs its prefixes delimited by '+'
        as a list of list of chars
    '''
    prefixes = [prefix+"+" for prefix in word.split("+")][:-1]
    return remove_empty_strings(prefixes)


def extract_suffixes(word):
    '''
        Inputs a word and outputs its suffixes delimited by '-'
        as a list of list of chars
    '''
    suffixes = ["-" + suffix for suffix in word.split("-")[1:]]
    return remove_empty_strings(suffixes)
