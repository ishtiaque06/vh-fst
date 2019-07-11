from vh_fst import FST
import os.path
from subprocess import call


'''AI--------------------------------------------------------------------------
    Writes an FST to a GraphViz file format
--------------------------------------------------------------------------AI'''
def fst_to_gv(fst_object):
    if type(fst_object) is not FST:
        raise TypeError("Please enter an FST object as defined in vh_fst.py.")

    try:
        os.mkdir("illustrations")
    except Exception as e:
        if str(e) != "[Errno 17] File exists: 'illustrations'":
            print(f"[(utils.fst_to_gv) Info]: {e}")
    file_name = fst_object.name.replace("/", " or ")
    with open(os.path.join("illustrations", file_name + ".gv"), "w") as f:
        f.write("digraph fst {\n")
        f.write('\tgraph [pad="0.5", nodesep="1", ranksep="2"];\n')
        f.write("\trankdir=LR;\n")
        f.write('\tsize="10,10";\n')

        # list the nodes in the FST
        f.write(f"\tnode [shape = point]; start;\n")
        f.write(f"\tnode [shape = doublecircle];\n")
        for key in fst_object.states:
            if fst_object.states[key] == "":
                fst_object.states[key] = uc(0x03bb)
            f.write(f'\t\t"{key}, {fst_object.states[key]}";\n')
        f.write("\n")
        trans = fst_object.transitions
        graph_dict = {}

        # Gather all transitions into a graph dict to label the string
        # transormations properly (ex. one arrow to represent "a:b", "c:d"
        # from state A to state B)
        for key in trans:
            input_state = key[0]
            input_letter = key[1]
            output_state = trans[key][1]
            output_letter = trans[key][0]
            value = graph_dict.get((input_state, output_state), [])
            value.append(f"{input_letter}:{output_letter}")
            graph_dict[(input_state, output_state)] = value

        # Write the graph on file for the FST
        for key in graph_dict:
            f.write(f'\t"{key[0]}, {fst_object.states[key[0]]}" ->'
                f'\t"{key[1]}, '
                f'{fst_object.states[key[1]]}" '
                f'[ label = "{", ".join(graph_dict[key])}" ];\n')
        f.write(f'\tstart -> "0, {fst_object.states[0]}";\n')
        f.write("}")

        print ("GraphViz file generation complete! Your GraphViz file is "
            f"'illustrations/{file_name}.gv'")
    return file_name


'''AI--------------------------------------------------------------------------
    Takes a filename for a GraphViz (*.gv) file and returns an SVG image
    corresponding to that filename
    Input: Filename (without extension) of a GraphViz file
    Output: SVG image in an "illustrations" folder relative to current one
    Precondition: The GV image must be in the directory this function is run
    from.
--------------------------------------------------------------------------AI'''
def gv_to_svg(fst_name):
    try:
        os.chdir(f"{os.getcwd()}/illustrations")
    except Exception as e:
        os.mkdir("illustrations")
        os.chdir(f"{os.getcwd()}/illustrations")
    code = call(["dot", "-Tsvg", f"{fst_name}.gv", "-o", f"{fst_name}.svg"])
    if code != 0:
        print ("[(utils.gv_to_svg) Error]: SVG Generation failed.")
    else:
        print ("Image generation complete! "
                f"Your file is at 'illustrations/{fst_name}.svg")
    os.chdir("..")
    return

def increasing_prefixes(string):
    """
        Helper function. Takes in a string and returns list of
        increasing substrings of the string.

        Example: inc_substrings("start") => ["","s", "st", "sta", "star", "start"]

        * Input: :code:`<type 'str>'` The string to build list of subsquences out of.
        * Output: :code:`<type 'list'>` List of subsequences
    """
    return [string[:i] for i in range(len(string) + 1)]


def spe_to_fst(A, B, C, D):
    """
        Takes in a rule of form A->B/C_D and creates an FST from that rule.

        Following are the types of rules covered by this generator:

        * a / b -> c_d (ex. qwertcaduiop -> qwertcbduiop)
        * TODO: a / b -> #_c (ex. aceuio -> bceuio)
        * TODO: a / b -> c_# (ex. qwertca -> qwertcb)
        * a / b -> _c  (ex. qwertacqeacee -> qwertbcqubcee)
        * a / b -> c\_  (ex. qwertcaqwecauio -> qwertcbqwecbuio)

        * Input:
            * A: :code:`<type 'str'>`: The letter to change
            * B: :code:`<type 'str'>`: The letter to change to
            * C: :code:`<type 'str'>`: First part of env in which 'a' changes to 'b'
            * D: :code:`<type 'str'>`: Second part of env in which 'a' changes to 'b'
        * Output:
            * FST: :code:`<type 'FST'>`: An FST object from the :code:`vh_fst.FST` class.
    """
    args_to_self = locals()
    alphabet = set()

    # Populate alphabet from given arguments
    for key in args_to_self:
        value = args_to_self[key]
        if value != "":
            translation = {ord(c):'' for c in '()'}
            value = value.translate(translation) # Removes '(' and ')'
            alphabet = alphabet.union(set(value))

    string_to_build = C + A + D
    string_states_list = increasing_prefixes(string_to_build)
    states = dict([(i, string_states_list[i]) for i in range(len(string_states_list) - 1)])

    transitions = {}
    no_of_states = len(string_states_list)
    for i in range(no_of_states - 1): # iterate till state before last state
        # Before reaching the character to replace
        last_ch_of_next_state = string_states_list[i + 1][-1]

        stored_string = string_to_build[len(C):i]

        # Process letters not in alphabet
        transitions[(i, '?')] = (stored_string + '?', 0)

        # All letters in the alphabet but that don't have transitions to the
        # next state
        excluded_set = set([last_ch_of_next_state, string_to_build[0]])
        for letter in alphabet.difference(excluded_set):
            transitions[(i, letter)] = (stored_string + letter, 0)
        if len(excluded_set) != 1:
            transitions[(i, string_to_build[0])] = (stored_string + string_to_build[0], 1)

        if i < len(C):
            transitions[(i, last_ch_of_next_state)] = (last_ch_of_next_state, i+1)
        else:
            # Final transition. This finishes the change in string.
            if i+1 == no_of_states - 1:
                if (string_states_list[i + 1] == string_to_build):
                    stored_string = B + stored_string[1:]

                # If D is empty, then the last character doesn't need to be added
                if D != '':
                    transitions[(i, last_ch_of_next_state)] = (stored_string
                        + last_ch_of_next_state, 0)
                else:
                    transitions[(i, last_ch_of_next_state)] = (stored_string, 0)
            else:
                transitions[(i, last_ch_of_next_state)] = ('', i+1)

    # Add properties required to initiate the class
    name = f"{A} -> {B} / {C}_{D}"

    dictionary = {
        'name': name,
        'states': states,
        'alphabet': alphabet,
        'transitions': transitions,
        'spe_generated': True
    }
    fst = FST(dictionary)
    return fst

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print ("Usage: python3 utils.py [command]")
        print ("Commands:")
        print("  all_diagrams\tOutputs GraphViz and SVG representations of all VH patterns\n"
              "                present in the current dataset file.\n")
        print("  spe_to_fst\tOpens up an interface where you can create and use an \n"
              "                FST based on a given SPE-style rule. ")
        exit(0)
    if sys.argv[1] == "all_diagrams":
        from vh_patterns_dataset import vh_dataset
        from unicode_variable_repr import *
        for key in vh_dataset:
            try:
                object = FST(vh_dataset[key])
                file_name = fst_to_gv(object)
                gv_to_svg(file_name)
            except Exception as e:
                raise e
    if sys.argv[1] == "spe_to_fst":
        pass
