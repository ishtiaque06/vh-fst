# Import all variables that represent unicode hex codes
from unicode_variable_repr import *

# Description of what each element in the language lists correspond to.
list_desc = ['VH pattern', 'State set','Alphabet of relevant symbols',
            'Transition set', 'Preprocessing necessary?', 'Postprocessing necessary?',
            'LtoR?','Prompt user to demarcate suffix with hyphen','details of preprocessing',
             'details of postprocessing','admin_notes=notes for creators',
             'notes: ex: What preprocessing nec?, What postproc nec?,Relevant features, Neutral vowels?, Transparent/Opaque?',
             'harmony_feature: lists types of featural harmony involved;'
             'can include Height, Palatal (front/back), Labial (rounding), ATR/RTR, Length (long/short)',
            'sc:stem control harmony-true or false',
            'dr:dominant-recessive harmony-True or False',
            'transparent:list of transparent vowels,None if none',
            'opaque:list of opaque vowels,None if none']

vh_dataset=\
{1:
    {
        'name': 'Kisa applicative suffix Vl'+B_L_U_NT,
        'states': {0:'il'+B_L_U_NT, 1:'il'+B_L_U_NT, 2:'el'+B_L_U_NT},
        'alphabet': ['i','e','u','o',B_L_U_NT],
        'transitions': {(0, '?'): ('?', 0), (0, 'i'): ('i', 1),
            (0, 'u'): ('u', 1), (0, 'e'): ('e', 2),
            (0, 'o'): ('o', 2), (1, 'i'): ('i', 1),
            (1, 'u'): ('u', 1), (1, '?'): ('?', 1),
            (1, 'e'): ('e', 2), (1, 'o'): ('o', 2),
            (2, '?'): ('?', 2), (2, 'e'): ('e', 2),
            (2, 'o'): ('o', 2), (2, 'i'): ('i', 1),
            (2, 'u'): ('u', 1),
            (0, B_L_U_NT): (B_L_U_NT, 0), (1, B_L_U_NT): (B_L_U_NT, 1),
            (2, B_L_U_NT): (B_L_U_NT, 2)},
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'admin_notes': ['Preprocess by removing last 3 characters ("Vla") of input'],
        'notes':['"a" is a transparent neutral vowel'],
        'harmony_feature':['Height'],
        'sc':True,
        'dr':False,
        'transparent':['B_L_U_NT is a transparent neutral vowel'],
        'opaque':None
    },
2:
    {
        'name': 'Kisa reversative suffix Vl'+B_L_U_NT,
        'states': {0:'ul'+B_L_U_NT, 1:'ul'+B_L_U_NT, 2:'ol'+B_L_U_NT},
        'alphabet': ['u','o',B_L_U_NT,'e','i'],
        'transitions': {(0, '?'): ('?', 0), (0, 'u'): ('u', 1),
            (0, 'o'): ('o', 2), (2, 'u'): ('u', 1), (1, 'o'): ('o', 2),
            (1, '?'): ('?', 1),(2, '?'): ('?', 2),
            (0, 'e'): ('e', 0), (1, 'e'): ('e', 1), (2, 'e'): ('e', 2),
            (0, 'i'): ('i', 0), (1, 'i'): ('i', 1), (2, 'i'): ('i', 2),
            (0, B_L_U_NT): (B_L_U_NT, 0), (1, B_L_U_NT): (B_L_U_NT, 1),
            (2, B_L_U_NT): (B_L_U_NT, 2)},
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'admin_notes': ['remove last 3 chars for preprocessing'],
        'notes':[B_L_U_NT+', i, e are transparent vowels'],
        'harmony_feature':['Height'],
        'sc':True,
        'dr':False,
        'transparent':[B_L_U_NT+',i, and e are transparent neutral vowels'],
        'opaque':None
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
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['Rounding is relevant',
            'As an aside, suffixal velar Cs become uvular if a'
             'non-high vowel appears in the stem',
            'No neutral vowels'],
        'harmony_feature':['Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
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
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['Backness harmonizes', 'pairs are of the same height',
            'No neutral vowels'],
        'harmony_feature':['Palatal'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
    },
    #5P is the attributes for which the FST must be run for selections 5,6, and 7 prior to running their respective attributes
    #I.e., the order is User input=> language-relevant preprocessing=> input into 5P=>output is the input for 5, 6, 7
'5P':
     {
        'name': 'Uyghur Preliminary rounding harmony',
        'states': {0:'',1:'',2:''},
        'alphabet': ['i','e','y',F_M_R_T],
        'transitions': {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (0,'i'):('i',1),(0,'e'):('e',1),(0,'y'):('y',2),
            (0,F_M_R_T):(F_M_R_T,2),(1,'y'):('i',1),(1,F_M_R_T):('e',1),
            (2,'i'):('y',2),(2,'e'):(F_M_R_T,2), (1,'i'):('i',1),
            (1,'e'):('e',1), (2,'y'):('y',2), (2,F_M_R_T): (F_M_R_T, 2)
            },
        'left_subseq':True,
        'hyphenate_suffix': False,
        'preprocess_req': False,
        'postprocess_req': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes':None,
        'harmony_feature':['Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
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
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets': 'Preprocess by running initial input through FST with 5P as parameters',
        'postprocess_dets': None,
        'notes': ['Backness harmonizes', 'pairs are of the same height',
            'i and e are transparent neutral vowels','there is rounding harmony i:y,e:FMRT'],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['i for Palatal and Labial','e for Palatal and Labial'],
        'opaque':None
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
        'hyphenate_suffix': False,
        'preprocess_dets': 'Preprocess by removing last three characters '
            'and then running this shortened input through FST with 5P as parameters',
        'postprocess_dets': None,
        'notes': ['DOES NOT WORK FOR DISHARMONIC LOAN WORDS',
                    'Backness harmonizes','i and e are transparent neutral vowels',
                    '[+back] default for the suffix',
                    'there is rounding harmony i:y,e:FMRT'],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['i for Palatal and Labial','e for Palatal and Labial'],
        'opaque':None
    },
7: #needs preprocessing with 5P
    {
        'name': 'Uyghur dative suffix -'+U_F_V+'V',
        'states': {0: U_F_V+B_L_U_NT,1:'ga',2:U_F_V+B_L_U_NT},
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
        'hyphenate_suffix': False,
        'preprocess_dets': 'Preprocess by removing last two characters'
            ' and then running this shortened input through FST with 5P as parameters',
        'postprocess_dets': None,
        'notes': ['DOES NOT WORK FOR DISHARMONIC LOAN WORDS',
                'Backness harmonizes','i and e are transparent neutral vowels',
                '[+back] default for the suffix',
                'there is rounding harmony i:y,e:FMRT'],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['i for Palatal and Labial','e for Palatal and Labial'],
        'opaque':None
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
            (2,'a'):('a',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,B_M_R_NT):(B_M_R_NT,2),
            (2,'u'):(B_H_R_NT,2),(2,'e'):('a',2),(2,'o'):(B_M_R_NT,2), (2,'i'):('i',2)},
        'preprocess_req':False,
        'postprocess_req':False,
        'left_subseq':True,
        'hyphenate_suffix': False,
        'preprocess_dets': None,
        'postprocess_dets': None,
        'notes':None,
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False
     },
8: #needs preprocessing with 8P
    {
        'name': 'Halh (Mongolic) rounding harmony',
        'states': {0:'',1:'',2:'',3:''},
        'alphabet': ['e','u','o','a',B_M_R_NT,B_H_R_NT],
        'transitions': {(0,'?'):('?',0), (1,'?'):('?',1),(2,'?'):('?',2), (3,'?'):('?',3),
            (0,'u'):('u',0), (0,B_H_R_NT):(B_H_R_NT,0), (3,'u'):('u',3),(3,B_H_R_NT):(B_H_R_NT,3),(3,'e'):('e',3),
            (3,'a'):('a',3), (3,'o'):('e',3),(3,B_M_R_NT):('a',3), (0,'e'):('e',1),(0,'a'):('a',1),(0,'o'):('o',2),
            (0,B_M_R_NT):(B_M_R_NT,2), (1,'u'):('u',3),(1,B_H_R_NT):(B_H_R_NT,3),(2,B_H_R_NT):(B_H_R_NT,3),
            (1,'e'):('e',1),(1,'a'):('a',1),(2,'o'):('o',2),(2,B_M_R_NT):(B_M_R_NT,2), (1,'o'):('e',1),
            (1,B_M_R_NT):('a',1),(2,'e'):('o',2),(2,'a'):(B_M_R_NT,2), (2,'u'):('u',3), (2,'i'):('i',2),
            (0, 'i'): ('i', 0),(1,'i'):('i', 1), (3,'i'):('i',3)},
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets': 'Preprocess by running initial input through FST with 8P as parameters',
        'postprocess_dets': None,
        'notes': ['Roundness harmonizes', 'pairs are of the same height',
            'i is transparent neutral vowel', 'high rd vowels do not trigger harmony; they are blockers'],
        'harmony_feature':['Labial','ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':['i for Labial and RTR harmony'],
        'opaque':['[+high,+Labial/Rd] vowels are blockers']
    },
9:
    {
        'name': 'Jingulu nominal root with non-neuter gender suffix',
        'states': {0:'',1:''},
        'alphabet': ['a','u','i'],
        'transitions': {(0,'?'):('?',0), (0,'a'):('i',0),(0,'i'):('i',1), (0,'u'):('u',1),
            (1,'?'):('?',1),(1,'a'):('a',1),(1,'i'):('i',1),(1,'u'):('u',1)},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'hyphenate_suffix': True, #Instruct user to insert a hyphen before the suffix (ex. input: r o o t - s u f wherein suf is the suffix)
        'preprocess_dets': "Check if 'u' or 'i' in suffix; "
            "if not, return input as output; "
            "if true, store suffix, but remove it from input; "
            "reverse the input and enter it into FST",
        'postprocess_dets':'Reverse output of FST; '
            'append stored suffix back on',
        'notes': ['[+high] harmonizes regressively from suffix to root',
            '[+high] in root acts as a blocker which does not lend its own feature (does not reset domain)'],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['[+high] in the root is a blocker which does not lend its own feature']
    },
10:
    {
        'name': 'Jingulu adjectivial root with non-neuter gender suffix',
        'states': {0:'',1:''},
        'alphabet': ['a','u','i'],
        'transitions': {(0,'?'):('?',0), (0,'a'):('i',0),(0,'i'):('i',1), (0,'u'):('u',1),
            (1,'?'):('?',1),(1,'a'):('a',1),(1,'i'):('i',1),(1,'u'):('u',1)},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'hyphenate_suffix': True, #Instruct user to insert a hyphen before the suffix (ex. input: r o o t - s u f wherein suf is the suffix)
        'preprocess_dets': "Check if 'u' or 'i' in suffix; "
            "if not, return input as output; if true, store suffix, but remove it from input; "
            "reverse the input and enter it into FST",
        'postprocess_dets':'Reverse output of FST; append stored suffix back on',
        'notes': ['[+high] harmonizes regressively from suffix to root',
            '[+high] in root acts as a blocker which does not lend its own feature (does not reset domain)'],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['[+high] in the root is a blocker which does not lend its own feature']
    },
11:
    {
        'name': 'Jingulu verbal root with subject agreement-marking suffix',
        'states': {0:'',1:''},
        'alphabet': ['a','u','i'],
        'transitions': {(0,'?'):('?',0), (0,'a'):('i',0),(0,'i'):('i',1), (0,'u'):('u',1),
            (1,'?'):('?',1),(1,'a'):('a',1),(1,'i'):('i',1),(1,'u'):('u',1)},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'hyphenate_suffix': True, #Instruct user to insert a hyphen before the suffix (ex. input: r o o t - s u f wherein suf is the suffix)
        'preprocess_dets': "Check if 'u' or 'i' in suffix; "
            "if not, return input as output; if true, store suffix, but remove it from input; "
            "reverse the input and enter it into FST",
        'postprocess_dets':'Reverse output of FST; append stored suffix back on',
        'notes': ['[+high] harmonizes regressively from suffix to root',
            '[+high] in root acts as a blocker which does not lend its own feature (does not reset domain)'],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['[+high] in the root is a blocker which does not lend its own feature']
    },
12:
    {
        'name': 'Jingulu verbal root with motion-imperative suffix',
        'states': {0:'',1:''},
        'alphabet': ['a','u','i'],
        'transitions': {(0,'?'):('?',0), (0,'a'):('i',0),(0,'i'):('i',1), (0,'u'):('u',1),
            (1,'?'):('?',1),(1,'a'):('a',1),(1,'i'):('i',1),(1,'u'):('u',1)},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'hyphenate_suffix': True, #Instruct user to insert a hyphen before the suffix (ex. input: r o o t - s u f wherein suf is the suffix)
        'preprocess_dets': "Check if 'u' or 'i' in suffix; "
            "if not, return input as output; if true, store suffix, but remove it from input; "
            "reverse the input and enter it into FST",
        'postprocess_dets':'Reverse output of FST; append stored suffix back on',
        'notes': ['[+high] harmonizes regressively from suffix to root',
            '[+high] in root acts as a blocker which does not lend its own feature (does not reset domain)'],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['[+high] in the root is a blocker which does not lend its own feature']
    },
13:
    {
        'name': 'Jingulu verbal root with negative imperative suffix',
        'states': {0:'',1:''},
        'alphabet': ['a','u','i'],
        'transitions': {(0,'?'):('?',0), (0,'a'):('i',0),(0,'i'):('i',1), (0,'u'):('u',1),
            (1,'?'):('?',1),(1,'a'):('a',1),(1,'i'):('i',1),(1,'u'):('u',1)},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'hyphenate_suffix': True, #Instruct user to insert a hyphen before the suffix (ex. input: r o o t - s u f wherein suf is the suffix)
        'preprocess_dets': "Check if 'u' or 'i' in suffix; "
            "if not, return input as output; if true, store suffix, but remove it from input; "
            "reverse the input and enter it into FST",
        'postprocess_dets':'Reverse output of FST; append stored suffix back on',
        'notes': ['[+high] harmonizes regressively from suffix to root',
            '[+high] in root acts as a blocker which does not lend its own feature (does not reset domain)'],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['[+high] in the root is a blocker which does not lend its own feature']
    },
14:
    {
        'name': 'Turkish palatal and rounding vowel harmony',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','e','y',F_M_R_T,B_H_U_T,'u',B_L_U_NT,'o'],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',1),(0,'e'):('e',1),(0,B_H_U_T):(B_H_U_T,2),
                       (0,B_L_U_NT):(B_L_U_NT,2), (0,'y'):('y',3),(0,F_M_R_T):(F_M_R_T,3),
                       (0,'u'):('u',4),(0,'o'):('o',4),
                       (1,'?'):('?',1),(1,'i'):('i',1),(1,'e'):('e',1),
                       (1,F_M_R_T):(F_M_R_T,1),(1,'y'):('i',1),(1,B_H_U_T):('i',1),(1,'u'):('i',1),
                       (1,B_L_U_NT):('e',1),(1,'o'):(F_M_R_T,1),
                       (2,'?'):('?',2),(2,B_H_U_T):(B_H_U_T,2),(2,B_L_U_NT):(B_L_U_NT,2),
                       (2,'o'):('o',2),(2,'u'):(B_H_U_T,2),(2,'i'):(B_H_U_T,2),
                       (2,'y'):(B_H_U_T,2),(2,'e'):(B_L_U_NT,2),(2,F_M_R_T):('o',2),
                       (3,'?'):('?',3),(3,'y'):('y',3),(3,'e'):('e',3),
                       (3,F_M_R_T):(F_M_R_T,3),(3,'i'):('y',3),(3,B_H_U_T):('y',3),(3,'u'):('y',3),
                       (3,B_L_U_NT):('e',3),(3,'o'):(F_M_R_T,3),
                       (4,'?'):('?',4),(4,'u'):('u',4),(4,'o'):('o',4),
                       (4,B_L_U_NT):(B_L_U_NT,4),(4,B_H_U_T):('u',4),(4,'i'):('u',4),
                       (4,'y'):('u',4),(4,'e'):(B_L_U_NT,4),(4,F_M_R_T):('o',4)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['front/backness and roundness harmonize progressively',
            'low vowels do not harmonize with rounding of preceding vowels; '
            'only valid for non-compounded words because compounds can constitute '
            'multiple harmonic domains',
            'This FST does not accurately reflect instances in which root-final '
            'consonants can decide frontness of suffixal vowels'],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
    },
15:
    {
        'name': 'Finnish palatal (front/back) vowel harmony',
        'states': {0:'',1:'',2:''},
        'alphabet': ['i','e','y',F_M_R_T,F_L_U_T,'u',B_L_U_NT,'o'],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',0),(0,'e'):('e',0),
                       (0,'y'):('y',1),(0,F_M_R_T):(F_M_R_T,1),(0,F_L_U_T):(F_L_U_T,1),
                       (0,'u'):('u',2),(0,'o'):('o',2),(0,B_L_U_NT):(B_L_U_NT,2),
                       (1,'?'):('?',1),(1,'i'):('i',1),(1,'e'):('e',1),
                       (1,'y'):('y',1),(1,F_M_R_T):(F_M_R_T,1),(1,F_L_U_T):(F_L_U_T,1),
                       (1,'u'):('y',1),(1,'o'):(F_M_R_T,1),(1,B_L_U_NT):(F_L_U_T,1),
                       (2,'?'):('?',2),(2,'i'):('i',2),(2,'e'):('e',2),
                       (2,'u'):('u',2),(2,'o'):('o',2),(2,B_L_U_NT):(B_L_U_NT,2),
                       (2,'y'):('u',2),(2,F_M_R_T):('o',2),(2,F_L_U_T):(B_L_U_NT,2)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['front/backness harmonizes progressively', 'i and e are transparent',
            'some words (e.g., loan words) may be disharmonic; in such cases this FST parametrization will be invalid'],
        'harmony_feature':['Palatal'],
        'sc':True,
        'dr':False,
        'transparent':['i','e'],
        'opaque':None
    },
16:
    {
        'name': 'Classical Mongolian palatal vowel harmony', #extinct language
        'states': {0:'',1:'',2:''},
        'alphabet': ['i','e','y',F_M_R_T,'u','a','o'],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',0),
                       (0,'y'):('y',1),(0,F_M_R_T):(F_M_R_T,1),(0,'e'):('e',1),
                       (0,'u'):('u',2),(0,'o'):('o',2),(0,'a'):('a',2),
                       (1,'?'):('?',1),(1,'i'):('i',1),(1,'e'):('e',1),
                       (1,'y'):('y',1),(1,F_M_R_T):(F_M_R_T,1),
                       (1,'u'):('y',1),(1,'o'):(F_M_R_T,1),(1,'a'):('e',1),
                       (2,'?'):('?',2),(2,'i'):('i',2),(2,'a'):('a',2),
                       (2,'u'):('u',2),(2,'o'):('o',2),
                       (2,'y'):('u',2),(2,F_M_R_T):('o',2),(2,'e'):('a',2)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['extinct language','front/backness harmonizes progressively','i is transparent',
            'compounded words may constitute multiple harmonic domains, meaning this FST MAY NOT BE VALID FOR COMPOUNDED WORDS',
            '/a/ and /e/ are treated as archiphonemes, despite /a/ in its traditional representation differing multifeaturally from /e/'],
        'harmony_feature':['Palatal'],
        'sc':True,
        'dr':False,
        'transparent':['i'],
        'opaque':None
    },
'17P': #suffix is input to this if /i/ is only vowel in the stem
    {
        'name': 'Kalmyk (Oirat) suffixal processing for stems with only /i/ as vowel',
        'states': {0:''},
        'alphabet': ['i','e','y',F_M_R_T,'u','a','o',F_L_U_T],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',0), (0,'y'):('y',0),
                       (0,'u'):('y',0),(0,F_L_U_T):(F_L_U_T,0),(0,'e'):('e',0),
                       (0,'o'):(F_M_R_T,0),(0,'a'):(F_L_U_T,0),(0,F_M_R_T):(F_M_R_T,0)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,#technically, suffix is only input to this
        'preprocess_dets':"If there is a suffix (hyphen) & /i/ is only vowel in the stem,"
            " then store stem and only input the suffix into this",
        'postprocess_dets':"Append output to stored stem, this is your output",
        'notes': None,
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
    },
17:
    {
        'name': 'Kalmyk (Oirat) harmony',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','e','y',F_M_R_T,'u','a','o',F_L_U_T],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',0),(0,'a'):('a',4),
                       (0,'y'):('y',1),(0,F_M_R_T):(F_M_R_T,1),(0,'e'):('e',2),
                       (0,F_L_U_T):(F_L_U_T,2),(0,'o'):('o',3),(0,'u'):('u',3),
                       (1,'?'):('?',1),(1,'i'):('i',1),(1,'y'):('y',1),
                       (1,F_M_R_T):(F_M_R_T,1),(1,'e'):(F_M_R_T,1),
                       (1,'u'):('y',1),(1,'o'):(F_M_R_T,1),(1,'a'):(F_L_U_T,1),
                       (2,'?'):('?',2),(2,'i'):('i',2),(2,'e'):('e',2),
                       (2,F_L_U_T):(F_L_U_T,2),(2,'o'):(F_M_R_T,2),
                       (2,'u'):('y',2),(2,F_M_R_T):(F_M_R_T,2),(2,'a'):(F_L_U_T,2),
                       (3,'?'):('?',3),(3,'i'):('i',3),(3,'e'):('o',3),
                       (3,'u'):('u',3),(3,'o'):('o',3),(3,'y'):('u',3),
                       (3,F_M_R_T):('o',3),(3,F_L_U_T):('a',3),
                       (4,'?'):('?',4),(4,'i'):('i',4),(4,'e'):('o',4),
                       (4,'u'):('u',4),(4,'o'):('o',4),(4,'y'):('u',4),
                       (4,F_M_R_T):('o',4),(4,F_L_U_T):('a',4)},
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': True, #instruct user to hyphenate suffix if there is in fact a suffix in the input
        'preprocess_dets':"If there is a suffix, user should hyphenate "
            "like so for input: s t e m - s u f f i x; "
            "If /i/ is the only vowel that appears in the stem, input the stem "
            "into 17P, the output is then the untouched stem with the 17P output suffix; "
            "Otherwise (if there is a non-/i/ vowel in the stem), "
            "remove the hyphen and run the entire output through FST 17, return output",
        'postprocess_dets':None,
        'notes': ['Mongolic language','front/backness harmonizes progressively',
            'progressive stem-control labial harmony',
            'i is transparent, except when it is the only vowel in the stem, '
            'in which case it triggers suffixal front-harmonization',
            'Key assumptions that were made despite lack of data: '
            'I assumed that rounded vowels only trigger rounding harmony if '
            'they are the first vowel in the word; additionally, I assumed that '
            '/e/ back-harmonizes to /o/' , 'Acoustic analysis by '
            '*[Frelinger, 2016](https://people.umass.edu/scable/LING404-SP16/Kalmyk/Student-Projects/Frelinger.pdf) , '
            'although necessarily preliminary and inconclusive, suggests '
            'that labial harmony is not so defined in Oirat; because this '
            'contradicts the prevalent perspective, however, such did not '
            'inform this FST'],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['i for Palatal and Labial, unless i is the only stem vowel'],
        'opaque':None
    },
18:
    {
        'name': 'Khalkha Mongolian harmony',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','e','u',B_H_R_NT,'a','o',B_M_R_NT],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',0),
                       (0,B_M_R_NT):(B_M_R_NT,1),(0,'o'):('o',2),(0,'a'):('a',3),
                       (0,B_H_R_NT):(B_H_R_NT,3),(0,'e'):('e',4),(0,'u'):('u',4),
                       (1,'?'):('?',1),(1,'i'):('i',1),(1,B_H_R_NT):(B_H_R_NT,3),
                       (1,'u'):('u',4),(1,B_M_R_NT):(B_M_R_NT,1),(1,'a'):(B_M_R_NT,1),
                       (1,'e'):(B_M_R_NT,1),(1,'o'):(B_M_R_NT,1),
                       (2,'?'):('?',2),(2,'i'):('i',2),(2,B_H_R_NT):(B_H_R_NT,3),
                       (2,'u'):('u',4),(2,B_M_R_NT):('o',2),(2,'o'):('o',2),
                       (2,'e'):('o',2),(2,'a'):('o',2),
                       (3,'?'):('?',3),(3,'i'):('i',3),(3,'a'):('a',3),
                       (3,'e'):('a',3),(3,'o'):('a',3),(3,B_M_R_NT):('a',3),
                       (3,'u'):(B_H_R_NT,3),(3,B_H_R_NT):(B_H_R_NT,3),
                       (4,'?'):('?',4),(4,'i'):('i',4),(4,'e'):('e',4),
                       (4,'o'):('e',4),(4,'a'):('e',4),(4,B_M_R_NT):('e',4),
                       (4,'u'):('u',4),(4,B_H_R_NT):('u',4)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None,
        'postprocess_dets':None,
        'notes': ['Mongolic language','Progressive ATR/RTR and labial harmony',
            'i is transparent for both types of harmony','/u,'+B_H_R_NT+'/ '
            'block [+labial] spreading such that following vowels are [-labial]',
            'I did not find data of the form a...B_M_R_NT or e...o, so I assumed '
            '[-Labial] spreads progressively, just as [+Labial does]'],
        'harmony_feature':['ATR/RTR','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['/i/ for ATR/RTR and Labial'],
        'opaque':['/u, B_H_R_NT/ are blockers for [+labial], all that follows is '
        '[-labial]']
    },
19:
    {
        'name': 'Dagur Mongolian harmony',
        'states': {0:'',1:'',2:'',3:''},
        'alphabet': ['i',schwa,'u','a',B_M_R_NT],
        'transitions': {(0,'?'):('?',0),(0,'i'):('i',0),
                       (0,B_M_R_NT):(B_M_R_NT,1),(0,schwa):(schwa,2),(0,'u'):('u',2),
                       (0,'a'):('a',3),
                       (1,'?'):('?',1),(1,'i'):('i',1),(1,B_M_R_NT):(B_M_R_NT,1),
                       (1,schwa):(B_M_R_NT,1),(1,'a'):(B_M_R_NT,1),(1,'u'):(B_M_R_NT,1),
                       (2,'?'):('?',2),(2,'i'):('i',2),(2,schwa):(schwa,2),(2,'u'):('u',2),
                       (2,'a'):(schwa,2),(2,B_M_R_NT):('u',2),
                       (3,'?'):('?',3),(3,'i'):('i',3),(3,'a'):('a',3),(3,schwa):('a',3),
                       (3,'u'):(B_M_R_NT,3),(3,B_M_R_NT):(B_M_R_NT,3)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None,
        'postprocess_dets':None,
        'notes': ['Mongolic language','Progressive ATR/RTR and labial harmony',
            'i is transparent for both types of harmony',
            'only'+ B_M_R_NT+' triggers [+labial] harmonization',
            'I did not find a sequence of [a...B_M_R_NT], so I assume that '
            '[a] triggers [-labial] harmony, but such is unconfirmed'],
        'harmony_feature':['ATR/RTR','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['/i/ for ATR/RTR and Labial'],
        'opaque':None
    },
20:
    {
        'name': 'Tunica harmony',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',12:''},
        'alphabet': ['i','e',F_M_U_NT,'u','o',B_M_R_NT,B_L_U_NT,'h',G_P_VL],
        'transitions': {(0,'?'):('?',0),(0,G_P_VL):(G_P_VL,0),(0,'h'):('h',0),(0,B_L_U_NT):(B_L_U_NT,0),
                       (2,'?'):('?',0),(0,'i'):('',1),(1,'?'):('i?',0),(1,G_P_VL):('i'+G_P_VL,2),
                       (1,'h'):('ih',2),(1,'i'):('',1),(1,'e'):('',3),(1,F_M_U_NT):('',5),
                       (1,B_L_U_NT):('',5),(1,'u'):('',1),(1,'o'):('',3),(1,B_M_R_NT):('',5),
                       (2,'i'):('',1),(2,'e'):('',3),(2,F_M_U_NT):('',5),(2,B_L_U_NT):('',5),
                       (2,'u'):('',1),(2,'o'):('',3),(2,B_M_R_NT):('',5),(3,'i'):('',1),
                       (3,'e'):('',3),(3,F_M_U_NT):('',5),(3,B_L_U_NT):('',5),(3,'u'):('',1),
                       (3,'o'):('',3),(3,B_M_R_NT):('',5),(4,'i'):('',1),(4,'e'):('',3),
                       (4,F_M_U_NT):('',5),(4,B_L_U_NT):('',5),(4,'u'):('',1),(4,'o'):('',3),
                       (4,B_M_R_NT):('',5),(5,'i'):('',1),(5,'e'):('',3),(5,F_M_U_NT):('',5),
                       (5,B_L_U_NT):('',5),(5,'u'):('',1),(5,'o'):('',3),(5,B_M_R_NT):('',5),
                       (6,'i'):('',1),(6,'e'):('',3),(6,F_M_U_NT):('',5),(6,B_L_U_NT):('',5),
                       (6,'u'):('',1),(6,'o'):('',3),(6,B_M_R_NT):('',5),(7,'u'):('',7),
                       (7,'o'):('',9),(7,B_M_R_NT):('',11),(7,'i'):('',7),(7,'e'):('',9),
                       (7,F_M_U_NT):('',11),(7,B_L_U_NT):('',11),(8,'u'):('',7),(8,'o'):('',9),
                       (8,B_M_R_NT):('',11),(8,'i'):('',7),(8,'e'):('',9),(8,F_M_U_NT):('',11),
                       (8,B_L_U_NT):('',11),(9,'u'):('',7),(9,'o'):('',9),(9,B_M_R_NT):('',11),
                       (9,'i'):('',7),(9,'e'):('',9),(9,F_M_U_NT):('',11),(9,B_L_U_NT):('',11),
                       (10,'u'):('',7),(10,'o'):('',9),(10,B_M_R_NT):('',11),(10,'i'):('',7),
                       (10,'e'):('',9),(10,F_M_U_NT):('',11),(10,B_L_U_NT):('',11),(11,'u'):('',7),
                       (11,'o'):('',9),(11,B_M_R_NT):('',11),(11,'i'):('',7),(11,'e'):('',9),
                       (11,F_M_U_NT):('',11),(11,B_L_U_NT):('',11),(12,'u'):('',7),(12,'o'):('',9),
                       (12,B_M_R_NT):('',11),(12,'i'):('',7),(12,'e'):('',9),(12,F_M_U_NT):('',11),
                       (12,B_L_U_NT):('',11),(4,'?'):('?',0),(0,'e'):('',3),(3,'?'):('e?',0),
                       (3,G_P_VL):('e'+G_P_VL,4),(3,'h'):('eh',4),(6,'?'):('?',0),
                       (0,F_M_U_NT):('',5),(5,'?'):(F_M_U_NT+'?',0),(5,G_P_VL):(F_M_U_NT+G_P_VL,6),
                       (5,'h'):(F_M_U_NT+'h',6),(8,'?'):('?',0),(0,'u'):('',7),(7,'?'):('u?',0),
                       (7,G_P_VL):('u'+G_P_VL,8),(7,'h'):('uh',8),(10,'?'):('?',0),(0,'o'):('',9),
                       (9,'?'):('o?',0),(9,G_P_VL):('o'+G_P_VL,10),(9,'h'):('oh',10),(12,'?'):('?',0),
                       (0,B_M_R_NT):('',11),(11,'?'):(B_M_R_NT+'?',0),(11,G_P_VL):(B_M_R_NT+G_P_VL,12),
                       (11,'h'):(B_M_R_NT+'h',12) #118
                       },
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'hyphenate_suffix': False,
        'preprocess_dets':None,
        'postprocess_dets':None,
        'notes': ['Front/backness and roundness harmonize progressively',
            'harmonization is blocked by all consonants, except pharyngeals, '
            'which are transparent',
            'vowels cannot appear consecutively, thus deletion of initial '
            'trigger vowels occurs in sequences of two adjacent vowels',
            'this FST incorporates deletion of first vowel in sequences of '
            'two vowels, it cannot process sequences of 3+ vowels properly, '
            'but it is assumed such sequences would never manifest'],
        'harmony_feature':['Palatal','Labial'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':None
    },
21:
    {
        'name': 'Yoruba ATR harmony',
        'states': {0:'',1:'',2:'',3:'',4:'',5:''},
        'alphabet': ['i','u','a','e','o',F_M_U_NT,B_M_R_NT],
        'transitions': {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
                        (4,'?'):('?',4),(5,'?'):('?',5),(0,'i'):('i',0),(0,'u'):('u',0),
                        (0,'a'):('a',0),(1,'e'):('e',1),(1,'o'):('o',1),(1,F_M_U_NT):('e',1),
                        (1,B_M_R_NT):('o',1),(3,'a'):('a',3),(4,'a'):('a',4),(2,F_M_U_NT):(F_M_U_NT,2),
                        (2,B_M_R_NT):(B_M_R_NT,2),(2,'e'):(F_M_U_NT,2),(2,'o'):(B_M_R_NT,2),
                        (0,'e'):('e',1),(0,'o'):('o',1),(0,F_M_U_NT):(F_M_U_NT,2),(0,B_M_R_NT):(B_M_R_NT,2),
                        (1,'a'):('a',3),(3,'e'):('e',1),(3,'o'):('o',1),(3,F_M_U_NT):('e',1),
                        (3,B_M_R_NT):('o',1),(3,'i'):('i',0),(3,'u'):('u',0),(1,'i'):('i',5),
                        (1,'u'):('u',5),(5,'e'):('e',1),(5,'o'):('o',1),(5,F_M_U_NT):('e',1),(5,B_M_R_NT):('o',1),
                        (5,'i'):('i',0),(5,'u'):('u',0),(5,'a'):('a',0),(2,'i'):('i',5),(2,'u'):('u',5),
                        (2,'a'):('a',4),(4,F_M_U_NT):(F_M_U_NT,2),(4,'e'):(F_M_U_NT,2),(4,B_M_R_NT):(B_M_R_NT,2),
                        (4,'o'):(B_M_R_NT,2),(4,'i'):('i',0),(4,'u'):('u',0)
                       },
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': False,
        'plus_prefix':True,
        'hyphenate_suffix': False,
        'preprocess_dets':'Reverse the stem, input the stem into FST 21 '
            '(if there is a prefix, do not enter the prefix into 21 -only the stem)',
        'postprocess_dets':'Reverse the stem output from 21; '
            'If the first vowel in the reversed output is in (i,u,e,o): '
            'input the prefix into 21A; If the first vowel in the reversed output '
            'is in (a,F_M_U_NT,B_M_R_NT), input the prefix into 21B; '
            'append the output prefix to the postprocessed stem - '
            'this is the final output',
        'notes': ['Yoruba lacks suffices',
            'Vowel inventory reference: A Grammar of Yoruba by Ayo Bamgbose',
            'primary reference: Yoruba Vowel Harmony by Diana Archangeli (DA)',
            'Regressive ATR', 'harmony differs somewhat between disyllabic contexts'
            ' and contexts with more than 2 syllables',
            'DA seems to suggest that /e/ or /o/ cannot precede /a/, '
            'but this does not seem to reliably be the case in the data, '
            'therefore this FST treats /a/ like a transparent vowel, rather than'
            ' a [-ATR] trigger like DA seemingly posits','mid vowels trigger [+-ATR] '
            'harmony','high vowels /i,u/ seem to reset the harmony domain in '
            'non-disyllabic monomorphemic stems, so they are treated as opaque'
            ' blockers in stems; I treat them as transparent vowels in prefixes, '
            'however, but this may be a tenuous assertion and can reasonably be '
            'subject to scrutiny','DA indicates that in sequences of MHM, wherein '
            'M=mid vowel and H=high vowel and in which consonants can separate '
            'the vowels, the first M MUST be [+ATR]; while I found this not to be '
            'the case in some words '
            '(e.g., foruk[back,mid,round,lax,-ATR]sil[front,mid,unrounded,lax,-ATR], '
            'ib[F_M_U_NT]rubojo), I adopted this assessment and incorporated '
            'it into the FST; this relationship does not seem to be the case'
            ' for multiple high vowels between mid vowels (i.e., MHHM), '
            'nor do high vowels seem to ensure [+ATR] upon harmonic reset '
            'in all contexts','/i,u,a/, although not triggers in the stem, '
            'can trigger [ATR] characterization of the prefix; the first '
            'vowel of the stem triggers the ATR harmony of the prefix '
            'such that [+ATR] vowels /i,u,e,o/trigger [+ATR] harmony of '
            'the prefix, while the other [-ATR] vowels trigger [-ATR] harmony'],
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':['/a/','/i,u/ in prefixes'],
        'opaque':['/i,u/ in stems seem to initiate new harmonic domains']
    },
'21A':
    {
        'name': 'Yoruba prefix +ATR processing',
        'states': {0:''},
        'alphabet': ['i','u','a','e','o',F_M_U_NT,B_M_R_NT],
        'transitions': {(0,'?'):('?',0),(0,'a'):('a',0),(0,'i'):('i',0),(0,'u'):('u',0),
                        (0,'e'):('e',0),(0,'o'):('o',0),(0,F_M_U_NT):('e',0),(0,B_M_R_NT):('o',0)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': False,
        'plus_prefix':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Only enter the prefix (if there was one for 21) into this; '
            'prefix should be entered into 21A only if the first vowel of the output stem is +ATR',
        'postprocess_dets':'Append output prefix to the output stem from 21',
        'notes':None,
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':['/a/','/i,u/ in prefixes'],
        'opaque':None
    },
'21B':
    {
        'name': 'Yoruba prefix -ATR processing',
        'states': {0:''},
        'alphabet': ['i','u','a','e','o',F_M_U_NT,B_M_R_NT],
        'transitions': {(0,'?'):('?',0),(0,'a'):('a',0),(0,'i'):('i',0),(0,'u'):('u',0),
                        (0,F_M_U_NT):(F_M_U_NT,0),(0,B_M_R_NT):(B_M_R_NT,0),(0,'e'):(F_M_U_NT,0),(0,'o'):(B_M_R_NT,0)},
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': False,
        'plus_prefix':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Only enter the prefix (if there was one for 21) into this; '
            'prefix should be entered into 21B only if the first vowel of the output stem is -ATR',
        'postprocess_dets':'Append output prefix to the output stem from 21',
        'notes':None,
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':['/a/','/i,u/ in prefixes'],
        'opaque':None
    },
}
