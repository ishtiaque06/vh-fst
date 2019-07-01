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
    with open(os.path.join("illustrations", fst_object.name + ".gv"), "w") as f:
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
            f"'illustrations/{fst_object.name}.gv'")


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
        print (f"Image generation complete! Your file is at 'illustrations/{fst_name}")
    os.chdir("..")
    return

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print ("Usage: python3 utils.py [command]")
        print ("Commands:")
        print("  diagram_all\tOutputs GraphViz and SVG representations of all VH patterns\n"
              "                present in the current dataset file.")
        exit(0)
    if sys.argv[1] == "diagram_all":
        from vh_patterns_dataset import vh_dataset
        from unicode_variable_repr import *
        for i in range(len(vh_dataset)):
            try:
                object = FST(i)
                fst_to_gv(object)
                gv_to_svg(object.name)
            except Exception as e:
                print(e)

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

        * Input:
            * A: :code:`<type 'str'>`: The letter to change
            * B: :code:`<type 'str'>`: The letter to change to
            * C: :code:`<type 'str'>`: First part of env in which 'a' changes to 'b'
            * D: :code:`<type 'str'>`: Second part of env in which 'a' changes to 'b'
        * Output:
            * FST: :code:`<type 'FST'>`: An FST object from the vh_fst.FST class.
    """
    args_to_self = locals()
    alphabet = set()

    # Populate alphabet from given arguments
    for key in args_to_self:
        value = args_to_self[key]
        if value != "":
            alphabet = alphabet.union(set(args_to_self[key]))

    string_to_build = C + A + D
    string_states_list = increasing_prefixes(string_to_build)
    states = dict([(i, string_states_list[i]) for i in range(len(string_states_list) - 1)])
    transitions = {}
    transitions[(0, "?")] = ("?", 0)
    '''
        Three iterations needed. After the first part is over and second part
        starts, start holding on to the current string and outputting nothing.
        If at each subsequent state, the FST is to step forward, keep holding
        the string and output lambda (empty string). Else, check if the letter that
        breaks the flow is in the alphabet. If it is, find the largest numbered
        state with that letter in the end and go there. Else, go to state 0 and
        start from there.
    '''
    no_of_states = len(string_states_list)
    for i in range(no_of_states - 1): # iterate till state before last state
        # Before reaching the character to replace
        last_ch_next_state = string_states_list[i + 1][-1]
        if i < len(C):
            transitions[(i, '?')] = ('?', 0)
            transitions[(i, last_ch_next_state)] = (last_ch_next_state, i+1)
            excluded_set = set([last_ch_next_state, C[0]])
            for letter in alphabet.difference(excluded_set):
                transitions[(i, letter)] = (letter, 0)
            if len(excluded_set) != 1:
                transitions[(i, C[0])] = (C[0], 1)
        else:
            stored_string = string_to_build[len(C):i]
            transitions[(i, '?')] = (stored_string + '?', 0)
            # Final transition. This finishes the change in string.
            excluded_set = set([last_ch_next_state, C[0]])
            for letter in alphabet.difference(excluded_set):
                transitions[(i, letter)] = (stored_string + letter, 0)
            if len(excluded_set) != 1:
                transitions[(i, C[0])] = (stored_string + C[0], 1)
            if i+1 == no_of_states - 1:
                if stored_string[0] == A and string_states_list[i + 1] == string_to_build:
                    stored_string = B + stored_string[1:]
                else:
                    raise ValueError(f"The stored string's first letter isn't {A}. "
                        f"The implementation of this function is probably faulty.")
                transitions[(i, last_ch_next_state)] = (stored_string
                                                        + last_ch_next_state, 0)
            else:
                transitions[(i, last_ch_next_state)] = ('', i+1)
    name = f"{A} -> {B} / {C}_{D}"
    left_subseq = True
    preprocess_req = False
    postprocess_req = False
    dictionary = {
        'name': name,
        'states': states,
        'alphabet': alphabet,
        'left_subseq': left_subseq,
        'preprocess_req': preprocess_req,
        'postprocess_req': postprocess_req,
        'transitions': transitions
    }
    fst = FST(dictionary)
    return fst
    

'''
a->b/cd_ef
'''
alphabet_global = {'a', 'b', 'c', 'd', 'e', 'f'}
transitions_global = {
    (0, '?'): ('?', 0),
    (0, 'a'): ('a', 0),
    (0, 'b'): ('b', 0),
    (0, 'c'): ('c', 1),
    (0, 'd'): ('d', 0),
    (0, 'e'): ('e', 0),
    (0, 'f'): ('f', 0),
    (1, '?'): ('?', 0),
    (1, 'a'): ('a', 0),
    (1, 'b'): ('b', 0),
    (1, 'c'): ('c', 1),
    (1, 'd'): ('d', 2),
    (1, 'e'): ('e', 0),
    (1, 'f'): ('f', 0),
    (2, '?'): ('?', 0),
    (2, 'a'): ('', 3),
    (2, 'b'): ('b', 0),
    (2, 'c'): ('c', 1),
    (2, 'd'): ('d', 0),
    (2, 'e'): ('e', 0),
    (2, 'f'): ('f', 0),
    (3, '?'): ('a?', 0),
    (3, 'a'): ('aa', 0),
    (3, 'b'): ('ab', 0),
    (3, 'c'): ('ac', 1),
    (3, 'd'): ('ad', 0),
    (3, 'e'): ('', 4),
    (3, 'f'): ('af', 0),
    (4, '?'): ('ae?', 0),
    (4, 'a'): ('aea', 0),
    (4, 'b'): ('aeb', 0),
    (4, 'c'): ('aec', 1),
    (4, 'd'): ('aed', 0),
    (4, 'e'): ('aee', 0),
    (4, 'f'): ('bef', 0),
}
import pprint
d = spe_to_fst("a", "b", "cd", "ef").transitions
print(transitions_global == d)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(transitions_global)
# pp.pprint(d)
