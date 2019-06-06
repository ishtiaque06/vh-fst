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

# Takes input command from user
def prompt_selection():
    user_input = input("Choose a vowel harmony pattern (enter q to quit): ")
    return user_input

# preprocess string after
def preprocess(string, fst):
    if fst.name == "Kisa applicative suffix"\
        or fst.name == "Kisa reversative suffix":
        return list(string[:-3])
    else:
        return string

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
                data = vh_dataset[user_input]
                print (data)
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
