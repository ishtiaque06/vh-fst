from vh_patterns_dataset import vh_dataset
from vh_fst import FST


# Shows available patterns available for the FST
def show_patterns():
    print (
        "1. Kisa applicative suffix\n"
        "2. Kisa reversative suffix\n"
        "3. Sibe vowel rounding harmony\n"
        "4. Tuvan backness harmony\n"
    )

# Takes selection of vowel harmony pattern from user
def prompt_selection():
    user_input = input("Choose a vowel harmony pattern (enter q to quit): ")
    return user_input

# Takes in a string when a vowel harmony pattern is specified
def prompt_word_input():
    user_input = input("Please enter a word, or enter --q to go back: ")
    return user_input

# preprocess string after user input
def preprocess(string, fst):
    if fst.name == "Kisa applicative suffix"\
        or fst.name == "Kisa reversative suffix":
        return list(string[:-3])
    else:
        return list(string)

# Post-process a list after the FST runs through it.
def postprocess(lst, fst):
    return "".join(lst)


# Main function, shows statements and instructions, processes input
def main():
    print ("Welcome to the Vowel Harmony FST Command-line Interface.\n"
        "This program lets you choose a vowel harmony pattern from several and \n"
        "attempts to give you the correct phonetic representation of valid words \n"
        "in the pattern of your choosing.\n"
        "\nThese are patterns that this program supports at the moment:"
    )
    show_patterns()
    user_input = prompt_selection()
    while user_input not in 'qQ':
        try:
            user_input = int(user_input)
            try:
                fst = FST(user_input)
                word = prompt_word_input()
                while word not in {'--q', '--Q'}:
                    word_as_list = preprocess(word, fst)
                    final = fst.step(word_as_list)
                    final_word = postprocess(final, fst)
                    print (f"Final output: {final_word}")
                    word = prompt_word_input()

            except KeyError as e:
                raise ValueError("Please select a valid pattern number\n")
            user_input = prompt_selection()
        except ValueError as e:
            print ("\n!!!!!!!!!!!!!!!!!!!")
            print ("! Invalid command !")
            print ("!!!!!!!!!!!!!!!!!!!\n")
            print (e)
            print ("Please select a number among these available: ")
            show_patterns()
            user_input = prompt_selection()



if __name__ == "__main__":
    main()
