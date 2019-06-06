# Import all variables that represent unicode hex codes
from unicode_variable_repr import *

# Description of what each element in the language lists correspond to.
list_desc = ['VH pattern', 'State set','Alphabet of relevant symbols',
            'Transition set', 'Preprocessing necessary?', 'Postprocessing necessary?',
            'LtoR?','What preprocessing nec?', 'What postproc nec?','Relevant features',
            'Neutral vowels?', 'Transparent/Opaque?'
            ]

vh_dataset ={1:
                ['Kisa applicative suffix', {0:'ila', 1:'ila', 2:'ela'},
                ['i','e','u','o'],
                {(0, '?'): ('?', 0), (0, 'i'): ('i', 1),
                    (0, 'u'): ('u', 1), (0, 'e'): ('e', 2),
                    (0, 'o'): ('o', 2), (1, 'i'): ('i', 1),
                    (1, 'u'): ('u', 1), (1, '?'): ('?', 1),
                    (1, 'e'): ('e', 2), (1, 'o'): ('o', 2),
                    (2, '?'): ('?', 2), (2, 'e'): ('e', 2),
                    (2, 'o'): ('o', 2), (2, 'i'): ('i', 1),
                    (2, 'u'): ('u', 1)}, True, False, True,
                'Preprocess by removing last 3 characters ("Vla") of input',
                '"a" is a transparent neutral vowel'
                ],
             2:
                ['Kisa reversative suffix', {0:'ula', 1:'ula', 2:'ola'}, ['u','o'],
                {(0, '?'): ('?', 0), (0, 'u'): ('u', 1), (0, 'o'): ('o', 2),
                    (2, 'u'): ('u', 1), (1, 'o'): ('o', 2), (1, '?'): ('?', 1),
                    (2, '?'): ('?', 2)}, True, False, True,
                 'remove last 3 chars for preprocessing', 'vowels: a,e,i'],
             3:
                ['Sibe vowel rounding harmony', {0:'', 1:'', 2:''},
                ['i','y',C_H_U_T, 'u', F_M_U_NT, F_M_R_T, 'a', B_M_R_NT],
                {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2), (0,'i'):('i',1),
                    (0,C_H_U_T):(C_H_U_T ,1), (0,F_M_U_NT):(F_M_U_NT ,1),
                    (0,'a'):('a',1), (0,'y'):('y',2), (0,'u'):('u',2),
                    (0,F_M_R_T):(F_M_R_T ,2), (0,B_M_R_NT):(B_M_R_NT,2),
                    (1,'i'):('i',1), (1,C_H_U_T):(C_H_U_T ,1),
                    (1,F_M_U_NT):(F_M_U_NT ,1), (1,'a'):('a',1), (2,'y',):('y',2),
                    (2,'u'):('u',2), (2,F_M_R_T):(F_M_R_T ,2), (2,B_M_R_NT):(B_M_R_NT,2),
                    (1,'y'):('i',1), (1,'u'):(C_H_U_T ,1),(1,F_M_R_T):(F_M_U_NT ,1),
                    (1,B_M_R_NT):('a',1), (2,'i',):('y',2), (2,C_H_U_T):('u',2),
                    (2,F_M_U_NT):(F_M_R_T ,2), (2,'a'):(B_M_R_NT,2)},
                False, False, True, 'Rounding is relevant',
                'As an aside, suffixal velar Cs become uvular if a non-high vowel appears in the stem',
                'No neutral vowels'],
            4:
                ['Tuvan backness harmony', {0:'',1:'',2:''},
                ['i','y',B_H_U_T,'u','e',F_M_R_T,'a','o'],
                {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2),
                    (0,'i'):('i',1), (0,'y'):('y' ,1), (0,'e'):('e' ,1),
                    (0,F_M_R_T):(F_M_R_T,1), (0,B_H_U_T):(B_H_U_T,2),
                    (0,'u'):('u',2), (0,'a'):('a' ,2), (0,'o'):('o',2),
                    (1,'i'):('i',1), (1,'y'):('y' ,1),(1,'e'):('e' ,1),
                    (1,F_M_R_T):(F_M_R_T,1), (2,B_H_U_T,):(B_H_U_T,2),
                    (2,'u'):('u',2), (2,'a'):('a' ,2), (2,'o'):('o',2),
                    (1,B_H_U_T):('i',1), (1,'u'):('y' ,1),(1,'a'):('e' ,1),
                    (1,'o'):(F_M_R_T,1), (2,'i',):(B_H_U_T,2), (2,'y'):('u',2),
                    (2,'e'):('a',2), (2,F_M_R_T):('o',2)},False ,False , True,
                'Backness harmonizes', 'pairs are of the same height',
                'No neutral vowels'
                ]
            }
