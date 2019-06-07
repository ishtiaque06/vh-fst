# Import all variables that represent unicode hex codes
from unicode_variable_repr import *

# Description of what each element in the language lists correspond to.
list_desc = ['VH pattern', 'State set','Alphabet of relevant symbols',
            'Transition set', 'Preprocessing necessary?', 'Postprocessing necessary?',
            'LtoR?','What preprocessing nec?', 'What postproc nec?','Relevant features',
            'Neutral vowels?', 'Transparent/Opaque?'
            ]

vh_dataset={1:
                {
                    'name': 'Kisa applicative suffix Vl'+B_L_U_NT,
                    'states': {0:'il'+B_L_U_NT, 1:'il'+B_L_U_NT, 2:'el'+B_L_U_NT},
                    'alphabet': ['i','e','u','o'],
                    'transitions': {(0, '?'): ('?', 0), (0, 'i'): ('i', 1),
                        (0, 'u'): ('u', 1), (0, 'e'): ('e', 2),
                        (0, 'o'): ('o', 2), (1, 'i'): ('i', 1),
                        (1, 'u'): ('u', 1), (1, '?'): ('?', 1),
                        (1, 'e'): ('e', 2), (1, 'o'): ('o', 2),
                        (2, '?'): ('?', 2), (2, 'e'): ('e', 2),
                        (2, 'o'): ('o', 2), (2, 'i'): ('i', 1),
                        (2, 'u'): ('u', 1)},
                    'preprocess_req': True,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'notes': ['Preprocess by removing last 3 characters ("Vla") of input',
                            '"a" is a transparent neutral vowel']
                },
            2:
                {
                    'name': 'Kisa reversative suffix -Vl'+B_L_U_NT,
                    'states': {0:'ul'+B_L_U_NT, 1:'ul'+B_L_U_NT, 2:'ol'+B_L_U_NT},
                    'alphabet': ['u','o'],
                    'transitions': {(0, '?'): ('?', 0), (0, 'u'): ('u', 1),
                        (0, 'o'): ('o', 2), (2, 'u'): ('u', 1), (1, 'o'): ('o', 2),
                        (1, '?'): ('?', 1),(2, '?'): ('?', 2)},
                    'preprocess_req': True,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'notes': ['remove last 3 chars for preprocessing', 'vowels: a,e,i']
                 },
            3:
                {
                    'name': 'Sibe vowel rounding harmony',
                    'states': {0:'', 1:'', 2:''},
                    'alphabet': ['i','y',C_H_U_T, 'u', F_M_U_NT, F_M_R_T, 'a', B_M_R_NT],
                    'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2),
                        (0,'i'):('i',1), (0,C_H_U_T):(C_H_U_T ,1),
                        (0,F_M_U_NT):(F_M_U_NT ,1), (0,'a'):('a',1), (0,'y'):('y',2),
                        (0,'u'):('u',2),(0,F_M_R_T):(F_M_R_T ,2), (0,B_M_R_NT):(B_M_R_NT,2),
                        (1,'i'):('i',1), (1,C_H_U_T):(C_H_U_T ,1),
                        (1,F_M_U_NT):(F_M_U_NT ,1), (1,'a'):('a',1), (2,'y',):('y',2),
                        (2,'u'):('u',2), (2,F_M_R_T):(F_M_R_T ,2), (2,B_M_R_NT):(B_M_R_NT,2),
                        (1,'y'):('i',1), (1,'u'):(C_H_U_T ,1),(1,F_M_R_T):(F_M_U_NT ,1),
                        (1,B_M_R_NT):('a',1), (2,'i',):('y',2), (2,C_H_U_T):('u',2),
                        (2,F_M_U_NT):(F_M_R_T ,2), (2,'a'):(B_M_R_NT,2)},
                    'preprocess_req': False,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'notes': ['Rounding is relevant',
                        'As an aside, suffixal velar Cs become uvular if a '
                        'non-high vowel appears in the stem',
                        'No neutral vowels']
                },
            4:
                {
                    'name': 'Tuvan backness harmony',
                    'states': {0:'',1:'',2:''},
                    'alphabet': ['i','y',B_H_U_T,'u','e',F_M_R_T,'a','o'],
                    'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2),
                        (0,'i'):('i',1), (0,'y'):('y' ,1), (0,'e'):('e' ,1),
                        (0,F_M_R_T):(F_M_R_T,1), (0,B_H_U_T):(B_H_U_T,2),
                        (0,'u'):('u',2), (0,'a'):('a' ,2), (0,'o'):('o',2),
                        (1,'i'):('i',1), (1,'y'):('y' ,1),(1,'e'):('e' ,1),
                        (1,F_M_R_T):(F_M_R_T,1), (2,B_H_U_T,):(B_H_U_T,2),
                        (2,'u'):('u',2), (2,'a'):('a' ,2), (2,'o'):('o',2),
                        (1,B_H_U_T):('i',1), (1,'u'):('y' ,1),(1,'a'):('e' ,1),
                        (1,'o'):(F_M_R_T,1), (2,'i',):(B_H_U_T,2), (2,'y'):('u',2),
                        (2,'e'):('a',2), (2,F_M_R_T):('o',2)},
                    'preprocess_req': False,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'notes': ['Backness harmonizes', 'pairs are of the same height',
                        'No neutral vowels']
                },
            #5P is the attributes for which the FST must be run for selections 5,6, and 7 prior to running their respective attributes
            #I.e., the order is User input=> language-relevant preprocessing=> input into 5P=>output is the input for 5, 6, 7
            '5P':
                 {
                    'name': 'Uyghur Preliminary rounding harmony',
                    'states': {0:'',1:'',2:''},
                    'alphabet': ['i','e','y',F_M_R_T],
                    'transitions': {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(0,'i'):('i',1),(0,'e'):('e',1),(0,'y'):('y',2), (0,F_M_R_T):(F_M_R_T,2),(1,'y'):('i',1),(1,F_M_R_T):('e',1),(2,'i'):('y',2),(2,'e'):(F_M_R_T,2)}
                 },
            5: #needs preprocessing with 5P
                {
                    'name': 'Uyghur backness harmony',
                    'states': {0:'',1:'',2:''},
                    'alphabet': ['i','y','u','e',F_M_R_T,'a','o',B_L_U_NT],
                    'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2),
                        (0,'i'):('i',0), (1,'i'):('i',1),(2,'i'):('i',2),
                        (0,'e'):('e',0), (1,'e'):('e',1),(2,'e'):('e',2),
                        (0,'a'):('a',1), (0,'y'):('y' ,1), (0,F_M_R_T):(F_M_R_T,1),
                        (0,'u'):('u',2), (0,B_L_U_NT):(B_L_U_NT,2), (0,'o'):('o',2),
                        (1,F_M_R_T):(F_M_R_T,1), (1,'y'):('y' ,1),(1,'a'):('a' ,1),
                        (2,'u'):('u',2), (2,B_L_U_NT):(B_L_U_NT ,2), (2,'o'):('o',2),
                        (1,'u'):('y' ,1),(1,B_L_U_NT):('a' ,1),(1,'o'):(F_M_R_T,1), 
                        (2,'y'):('u',2), (2,'a'):(B_L_U_NT,2), (2,F_M_R_T):('o',2)},
                    'preprocess_req': False,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'preprocess_dets': 'Preprocess by running initial input through FST with 5P as parameters'
                    'notes': ['Backness harmonizes', 'pairs are of the same height',
                        'i and e are transparent neutral vowels','there is rounding harmony i:y,e:FMRT']
                },
             6: #needs preprocessing with 5P
                {
                    'name': 'Uyghur plural suffix -lVr',
                    'states': {0:'l'+B_L_U_NT+'r',1:'lar',2:'l'+B_L_U_NT+'r'},
                    'alphabet': ['i','y','u','e',F_M_R_T,'a','o',B_L_U_NT],
                    'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2),
                        (0,'i'):('i',0), (1,'i'):('i',1),(2,'i'):('i',2),
                        (0,'e'):('e',0), (1,'e'):('e',1),(2,'e'):('e',2),
                        (0,'a'):('a',1), (0,'y'):('y' ,1), (0,F_M_R_T):(F_M_R_T,1),
                        (0,'u'):('u',2), (0,B_L_U_NT):(B_L_U_NT,2), (0,'o'):('o',2),
                        (1,F_M_R_T):(F_M_R_T,1), (1,'y'):('y' ,1),(1,'a'):('a' ,1),
                        (2,'u'):('u',2), (2,B_L_U_NT):(B_L_U_NT ,2), (2,'o'):('o',2),
                        (1,'u'):('y' ,1),(1,B_L_U_NT):('a' ,1),(1,'o'):(F_M_R_T,1), 
                        (2,'y'):('u',2), (2,'a'):(B_L_U_NT,2), (2,F_M_R_T):('o',2)},
                    'preprocess_req': True,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'preprocess_dets': 'Preprocess by removing last three characters and then running this shortened input through FST with 5P as parameters'
                    'notes': ['DOES NOT WORK FOR DISHARMONIC LOAN WORDS','Backness harmonizes','i and e are transparent neutral vowels','[+back] default for the suffix','there is rounding harmony i:y,e:FMRT']
                },
            7: #needs preprocessing with 5P
                {
                    'name': 'Uyghur dative suffix'+U_F_V+'V',
                    'states': {0: U_F_V+B_L_U_N_T,1:'ga',2:U_F_V+B_L_U_NT},
                    'alphabet': ['i','y','u','e',F_M_R_T,'a','o',B_L_U_NT],
                    'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2),
                        (0,'i'):('i',0), (1,'i'):('i',1),(2,'i'):('i',2),
                        (0,'e'):('e',0), (1,'e'):('e',1),(2,'e'):('e',2),
                        (0,'a'):('a',1), (0,'y'):('y' ,1), (0,F_M_R_T):(F_M_R_T,1),
                        (0,'u'):('u',2), (0,B_L_U_NT):(B_L_U_NT,2), (0,'o'):('o',2),
                        (1,F_M_R_T):(F_M_R_T,1), (1,'y'):('y' ,1),(1,'a'):('a' ,1),
                        (2,'u'):('u',2), (2,B_L_U_NT):(B_L_U_NT ,2), (2,'o'):('o',2),
                        (1,'u'):('y' ,1),(1,B_L_U_NT):('a' ,1),(1,'o'):(F_M_R_T,1), 
                        (2,'y'):('u',2), (2,'a'):(B_L_U_NT,2), (2,F_M_R_T):('o',2)},
                    'preprocess_req': True,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'preprocess_dets': 'Preprocess by removing last two characters and then running this shortened input through FST with 5P as parameters'
                    'notes': ['DOES NOT WORK FOR DISHARMONIC LOAN WORDS','Backness harmonizes','i and e are transparent neutral vowels','[+back] default for the suffix','there is rounding harmony i:y,e:FMRT']
                },
            #8P is the attributes for which the FST must be run for selection 8 prior to running its respective attributes
            #I.e., the order is User input=>  input into 8P=>output is the input for 8
            '8P':
                 {
                    'name': 'Halh Preliminary pharyngeal (RTR) harmony',
                    'states': {0:'',1:'',2:''},
                    'alphabet': ['i','e','u','o','a',B_M_R_NT,B_H_R_NT],
                    'transitions': {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
                        (0,'i'):('i',1),(0,'e'):('e',1),(0,'u'):('u',1),(0,'o'):('o',1),
                        (0,'a'):('a',2), (0,B_H_R_NT):(B_H_R_NT,2),(0,B_M_R_NT):(B_M_R_NT,2),
                        (1,'i'):('i',1),(1,'e'):('e',1),(1,'u'):('u',1),(1,'o'):('o',1),
                        (1,B_H_R_NT):('u',1),(1,'a'):('e',1),(1,B_M_R_NT):('o',1),
                        (2,'a'):('a',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,B_M_R_NT),
                        (2,'u'):(B_H_R_NT,2),(2,'e'):('a',2),(2,'o'):(B_M_R_NT,2)},
                 },
            8: #needs preprocessing with 8P
                {
                    'name': 'Halh (Mongolic) rounding harmony',
                    'states': {0:'',1:'',2:'',3:''},
                    'alphabet': ['e','u','o','a',B_M_R_NT,B_H_R_NT],
                    'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2), (3,'?'):('?',3),
                        (0,'u'):('u',0), (0,B_H_R_NT):(B_H_R_NT,0), (3,'u'):('u',3),(3,B_H_R_NT):(B_H_R_NT,3),(3,'e'):('e',3),
                        (3,'a'):('a',3), (3,'o'):('e',3),(3,B_M_R_NT):('a',3), (0,'e'):('e',1),(0,'a'):('a',1),(0,'o'):('o',2),
                        (0,B_M_R_NT):(B_M_R_NT,2), (1,'u'):('u',3),(1,B_H_R_NT),(B_H_R_NT,3),(2,B_H_R_NT):(B_H_R_NT,3),
                        (1,'e'):('e',1),(1,'a'):('a',1),(2,'o'):('o',2),(2,B_M_R_NT):(B_M_R_NT,2), (1,'o'):('e',1),
                        (1,B_M_R_NT):('a',1),(2,'e'):('o',2),(2,'a'):(B_M_R_NT,2)}, 
                    'preprocess_req': False,
                    'postprocess_req': False,
                    'left_subseq': True,
                    'preprocess_dets': 'Preprocess by running initial input through FST with 8P as parameters'
                    'notes': ['Roundness harmonizes', 'pairs are of the same height',
                        'i is transparent neutral vowels', 'high rd vowels do not rigger harmony; they are blockers']
                },
            
            
             }
