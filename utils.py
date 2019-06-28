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


'''AI--------------------------------------------------------------------------
Takes in a rule of form A->B/C_D and creates an FST from that rule.
--------------------------------------------------------------------------AI'''
def spe_to_fst():
    pass
