from vh_patterns_dataset import vh_dataset
from vh_fst import FST
from unicode_variable_repr import *
from processors import preprocess, postprocess, split_word_components

# import call method from subprocess module
from subprocess import call
import os

# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')


# Shows available patterns available for the FST
def show_patterns():
    for i in range(len(vh_dataset)):
        try:
            print(f"{i}. {vh_dataset[i]['name']}")
        except: # for FSTs that are not numbered by integers like 5p and 8p
            pass

# Takes selection of vowel harmony pattern from user
def prompt_selection():
    user_input = input("Select a vowel harmony pattern (Ex: 1)\n"
        "Enter q to quit, l to list all patterns\n"
        ">>> ")
    return user_input

# Takes in a string when a vowel harmony pattern is specified
def prompt_word_input():
    user_input = input("Please enter a word delimited with spaces (Ex: s t r i n g)\n"
        "(enter --help for help and more examples, --q to quit)\n"
        ">>> ")
    return user_input

# Show help while using the Vowel Harmony patterns
def show_vh_help(fst):
    print("")
    print(f"Welcome to the help section of {fst.name}.")
    print("")
    print("Inputting a word is pretty simple: you enter the word, separated by "
        "spaces, like so: ")
    print("t s o m i l a")
    print("\nYou can also enter a word with its letters in IPA. ")
    print ("For example, you can express 'tsomilɑ' as 't s o m i l B_L_U_NT'\n"
        "where B_L_U_NT stands for the IPA symbol ɑ, the Back, Low, Unrounded, "
        "lax (Not Tense) vowel.")
    print("")
    print("Help menu commands: ")
    print("list-symbols       List all IPA symbol representations that we offer")
    print("q                  Exit this help menu")
    while True:
        user_input =  input("help -> ")
        if user_input in {'q', 'Q'}:
            break
        if user_input == "list-symbols":
            print("Consonants: ")
            for key in cons_as_dict:
                print (f"{key}: {cons_as_dict[key]}")
            print("\nVowels: ")
            for key in vowels_as_dict:
                print (f"{key}: {vowels_as_dict[key]}")


# Shows the intro message for a vowel-harmony pattern interface
# TODO: Show notes for languages in vh_patterns_dataset.
def show_vh_intro(fst):
    clear()
    print (5 * "=" + len(fst.name) * "=" + 5 * "=")
    print (f"     {fst.name}")
    print (5 * "=" + len(fst.name) * "=" + 5 * "=")
    print("\nFollowing vowels take part in this vowel harmony: ")
    print(",".join(fst.alphabet))
    print ("\nPlease enter a word delimited with spaces (Ex: s t r i n g)\n"
        "(enter --help for help and more examples, --q to quit)\n")


# Main function, shows statements and instructions, processes input
def main():
    clear()
    print ("Welcome to the Vowel Harmony FST Command-line Interface.\n"
        "This program lets you choose a vowel harmony pattern from several and \n"
        "attempts to give you the correct phonetic representation of valid words \n"
        "in the pattern of your choosing.\n"
        "\nThese are patterns that this program supports at the moment:"
    )
    show_patterns()
    while True:
        print ("==============================================================")
        print ("  Vowel Harmony FST Command-line Interface for Phonologists")
        print ("==============================================================")
        user_input = prompt_selection()
        if user_input in "qQ":
            break
        if user_input == "l":
            clear()
            show_patterns()
        else:
            try:
                user_input = int(user_input)
                fst = FST(user_input)
            except (KeyError, ValueError):
                clear()
                print ("Please enter a valid selection.\n")
                continue
            show_vh_intro(fst)
            while True:
                word = input(f"{fst.name} >>> ")
                if word in {'--q', '--Q'}:
                    clear()
                    break
                if word == "--help":
                    show_vh_help(fst)
                    show_vh_intro(fst)
                    continue
                word, prefix_as_list, stem_as_list, suffix_as_list = \
                    split_word_components(word)
                process_yes_or_no, word_as_list = \
                    preprocess(word, prefix_as_list, stem_as_list, suffix_as_list, fst)
                if process_yes_or_no:
                    final = fst.step(word_as_list)
                    final_word = postprocess(final, fst)
                    print (final_word)
                else:
                    print("".join(word_as_list))


if __name__ == "__main__":
    main()
