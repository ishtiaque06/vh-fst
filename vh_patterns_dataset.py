# Import all variables that represent unicode hex codes
from unicode_variable_repr import *

def show_implementation_details(id):
    '''
        Given a language from vh_dataset in this file, prints the following info:

        * name <string>
        * left_subseq <boolean>
        * preprocess_dets <string>
        * postprocess_dets <string>
    '''
    language = vh_dataset[id]
    print ("Name: ", language['name'])
    print ("Left subsequential?", language['left_subseq'])
    print ("Preprocess details: ", language['preprocess_dets'])
    print ("Postprocess details: ", language['postprocess_dets'])

# Description of what each element in the language lists correspond to.
list_desc = ['VH pattern', 'State set','Alphabet of relevant symbols',
            'Transition set', 'Preprocessing necessary?', 'Postprocessing necessary?',
            'LtoR?-if false, means right subsequential',
            'Bidirectionally subsequential?','Prompt user to demarcate suffix with hyphen',
            'details of preprocessing',
            'details of postprocessing','admin_notes=notes for creators',
            'notes: ex: What preprocessing nec?, What postproc nec?, '
                'Relevant features, Neutral vowels?, Transparent/Opaque?',
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
        'bidir_subseq':False,
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
        'bidir_subseq':False,
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
        'bidir_subseq':False,
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
        'bidir_subseq':False,
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
    #5P is the attributes for which the FST must be run for selections
    # 5,6, and 7 prior to running their respective attributes
    #I.e., the order is User input=> language-relevant preprocessing
    #=> input into 5P=>output is the input for 5, 6, 7
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
        'bidir_subseq':False,
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
        'bidir_subseq':False,
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
        'bidir_subseq':False,
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
        'bidir_subseq':False,
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
    #8P is the attributes for which the FST must be run for selection 8 prior to
    # running its respective attributes
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
        'bidir_subseq':False,
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
            (0,'u'):('u',0), (0,B_H_R_NT):(B_H_R_NT,0),
            (3,'u'):('u',3),(3,B_H_R_NT):(B_H_R_NT,3),(3,'e'):('e',3),
            (3,'a'):('a',3), (3,'o'):('e',3),(3,B_M_R_NT):('a',3),
            (0,'e'):('e',1),(0,'a'):('a',1),(0,'o'):('o',2),
            (0,B_M_R_NT):(B_M_R_NT,2), (1,'u'):('u',3),(1,B_H_R_NT):(B_H_R_NT,3),
            (2,B_H_R_NT):(B_H_R_NT,3),
            (1,'e'):('e',1),(1,'a'):('a',1),(2,'o'):('o',2),(2,B_M_R_NT):(B_M_R_NT,2),
            (1,'o'):('e',1),
            (1,B_M_R_NT):('a',1),(2,'e'):('o',2),(2,'a'):(B_M_R_NT,2), (2,'u'):('u',3),
            (2,'i'):('i',2),
            (0, 'i'): ('i', 0),(1,'i'):('i', 1), (3,'i'):('i',3)},
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets': 'Preprocess by running initial input through FST with 8P as parameters',
        'postprocess_dets': None,
        'notes': ['Roundness harmonizes', 'pairs are of the same height',
            'i is transparent neutral vowel',
            'high rd vowels do not trigger harmony; they are blockers'],
        'harmony_feature':['Labial','ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':['i for Labial and RTR harmony'],
        'opaque':['[+high,+Labial/Rd] vowels are blockers']
    },
    9:
    {
        'name': 'Jingulu nominal root with non-neuter gender suffix',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['a','u','i','-','+'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),
            (0,'+'):('+',0),(0,'a'):('a',0),(0,'-'):('-',4),(0,'u'):('u',1),
            (0,'i'):('i',1),
            (1,'+'):('+',1),(1,'a'):('a',1),(1,'u'):('u',1),(1,'i'):('i',1),
            (1,'-'):('-',2),
            (2,'a'):('i',2),(2,'-'):('-',2),(2,'i'):('i',3),(2,'u'):('u',3),
            (2,'+'):('+',3),
            (3,'+'):('+',3),(3,'a'):('a',3),(3,'u'):('u',3),(3,'i'):('i',3),
            (3,'-'):('-',3),
            (4,'+'):('+',4),(4,'a'):('a',4),(4,'u'):('u',4),(4,'i'):('i',4),
            (4,'-'):('-',4),
            },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        # Instruct user to insert a hyphen before the suffix
        # (ex. input: r o o t - s u f wherein suf is the suffix)
        'hyphenate_suffix': True,
        'preprocess_dets': "Reverse the input and enter it into FST",
        'postprocess_dets':'Reverse output of FST',
        'notes': ['FST only works if the titular suffix is the only suffix in the input',
            '[+high] harmonizes regressively from suffix to root',
            '[+high] in root acts as a blocker which does not lend its own feature '
            '(does not reset domain)'],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['[+high] in the root is a blocker which does not lend its own feature']
    },
    10:
        {
            'name': 'Jingulu adjectivial root with non-neuter gender suffix',
            'states': {0:'',1:'',2:'',3:'',4:''},
            'alphabet': ['a','u','i','-','+'],
            'transitions':
                {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
                (4,'?'):('?',4),
                (0,'+'):('+',0),(0,'a'):('a',0),(0,'-'):('-',4),(0,'u'):('u',1),
                (0,'i'):('i',1),
                (1,'+'):('+',1),(1,'a'):('a',1),(1,'u'):('u',1),(1,'i'):('i',1),
                (1,'-'):('-',2),
                (2,'a'):('i',2),(2,'-'):('-',2),(2,'i'):('i',3),(2,'u'):('u',3),
                (2,'+'):('+',3),
                (3,'+'):('+',3),(3,'a'):('a',3),(3,'u'):('u',3),(3,'i'):('i',3),
                (3,'-'):('-',3),
                (4,'+'):('+',4),(4,'a'):('a',4),(4,'u'):('u',4),(4,'i'):('i',4),
                (4,'-'):('-',4),
                },
            'preprocess_req': True,
            'postprocess_req': True,
            'left_subseq': False,
            'bidir_subseq':False,
            #Instruct user to insert a hyphen before the suffix
            # (ex. input: r o o t - s u f wherein suf is the suffix)
            'hyphenate_suffix': True,
            'preprocess_dets': "Reverse the input and enter it into FST",
            'postprocess_dets':'Reverse output of FST',
            'notes': ['FST only works if the titular suffix is the only suffix in the input',
            '[+high] harmonizes regressively from suffix to root',
                '[+high] in root acts as a blocker which does not lend its own '
                'feature (does not reset domain)'],
            'harmony_feature':['Height'],
            'sc':False,
            'dr':False,
            'transparent':None,
            'opaque':['[+high] in the root is a blocker which does not lend its own feature']
        },
    11:
        {
            'name': 'Jingulu verbal root with subject agreement-marking suffix',
            'states': {0:'',1:'',2:'',3:'',4:''},
            'alphabet': ['a','u','i','-','+'],
            'transitions':
                {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
                (4,'?'):('?',4),
                (0,'+'):('+',0),(0,'a'):('a',0),(0,'-'):('-',4),(0,'u'):('u',1),
                (0,'i'):('i',1),
                (1,'+'):('+',1),(1,'a'):('a',1),(1,'u'):('u',1),(1,'i'):('i',1),
                (1,'-'):('-',2),
                (2,'a'):('i',2),(2,'-'):('-',2),(2,'i'):('i',3),(2,'u'):('u',3),
                (2,'+'):('+',3),
                (3,'+'):('+',3),(3,'a'):('a',3),(3,'u'):('u',3),(3,'i'):('i',3),
                (3,'-'):('-',3),
                (4,'+'):('+',4),(4,'a'):('a',4),(4,'u'):('u',4),(4,'i'):('i',4),
                (4,'-'):('-',4),
                },
            'preprocess_req': True,
            'postprocess_req': True,
            'left_subseq': False,
            'bidir_subseq':False,
            #Instruct user to insert a hyphen before the suffix
            # (ex. input: r o o t - s u f wherein suf is the suffix)
            'hyphenate_suffix': True,
            'preprocess_dets': "Reverse the input and enter it into FST",
            'postprocess_dets':'Reverse output of FST',
            'notes': [
                'FST only works if the titular suffix is the only suffix in the input',
                '[+high] harmonizes regressively from suffix to root',
                '[+high] in root acts as a blocker which does not lend its own '
                'feature (does not reset domain)'],
            'harmony_feature':['Height'],
            'sc':False,
            'dr':False,
            'transparent':None,
            'opaque':['[+high] in the root is a blocker which does not lend its own feature']
        },
    12:
        {
            'name': 'Jingulu verbal root with motion-imperative suffix',
            'states': {0:'',1:'',2:'',3:'',4:''},
            'alphabet': ['a','u','i','-','+'],
            'transitions':
                {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
                (4,'?'):('?',4),
                (0,'+'):('+',0),(0,'a'):('a',0),(0,'-'):('-',4),(0,'u'):('u',1),
                (0,'i'):('i',1),
                (1,'+'):('+',1),(1,'a'):('a',1),(1,'u'):('u',1),(1,'i'):('i',1),
                (1,'-'):('-',2),
                (2,'a'):('i',2),(2,'-'):('-',2),(2,'i'):('i',3),(2,'u'):('u',3),
                (2,'+'):('+',3),
                (3,'+'):('+',3),(3,'a'):('a',3),(3,'u'):('u',3),(3,'i'):('i',3),
                (3,'-'):('-',3),
                (4,'+'):('+',4),(4,'a'):('a',4),(4,'u'):('u',4),(4,'i'):('i',4),
                (4,'-'):('-',4),
                },
            'preprocess_req': True,
            'postprocess_req': True,
            'left_subseq': False,
            'bidir_subseq':False,
            #Instruct user to insert a hyphen before the suffix
            # (ex. input: r o o t - s u f wherein suf is the suffix)
            'hyphenate_suffix': True,
            'preprocess_dets': "Reverse the input and enter it into FST",
            'postprocess_dets':'Reverse output of FST',
            'notes': [
                'FST only works if the titular suffix is the only suffix in the input',
                '[+high] harmonizes regressively from suffix to root',
                '[+high] in root acts as a blocker which does not lend its own '
                'feature (does not reset domain)'],
            'harmony_feature':['Height'],
            'sc':False,
            'dr':False,
            'transparent':None,
            'opaque':['[+high] in the root is a blocker which does not lend its own feature']
        },
    13:
        {
            'name': 'Jingulu verbal root with negative imperative suffix',
            'states': {0:'',1:'',2:'',3:'',4:''},
            'alphabet': ['a','u','i','-','+'],
            'transitions':
                {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
                (4,'?'):('?',4),
                (0,'+'):('+',0),(0,'a'):('a',0),(0,'-'):('-',4),(0,'u'):('u',1),
                (0,'i'):('i',1),
                (1,'+'):('+',1),(1,'a'):('a',1),(1,'u'):('u',1),(1,'i'):('i',1),
                (1,'-'):('-',2),
                (2,'a'):('i',2),(2,'-'):('-',2),(2,'i'):('i',3),(2,'u'):('u',3),
                (2,'+'):('+',3),
                (3,'+'):('+',3),(3,'a'):('a',3),(3,'u'):('u',3),(3,'i'):('i',3),
                (3,'-'):('-',3),
                (4,'+'):('+',4),(4,'a'):('a',4),(4,'u'):('u',4),(4,'i'):('i',4),
                (4,'-'):('-',4),
                },
            'preprocess_req': True,
            'postprocess_req': True,
            'left_subseq': False,
            'bidir_subseq':False,
            #Instruct user to insert a hyphen before the suffix
            # (ex. input: r o o t - s u f wherein suf is the suffix)
            'hyphenate_suffix': True,
            'preprocess_dets': "Reverse the input and enter it into FST",
            'postprocess_dets':'Reverse output of FST',
            'notes': [
                'FST only works if the titular suffix is the only suffix in the input',
                '[+high] harmonizes regressively from suffix to root',
                '[+high] in root acts as a blocker which does not lend its own '
                'feature (does not reset domain)'],
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
        'transitions':
            {(0,'?'):('?',0),(0,'i'):('i',1),(0,'e'):('e',1),(0,B_H_U_T):(B_H_U_T,2),
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
        'bidir_subseq':False,
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
        'transitions':
            {(0,'?'):('?',0),(0,'i'):('i',0),(0,'e'):('e',0),
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
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['front/backness harmonizes progressively', 'i and e are transparent',
            'some words (e.g., loan words) may be disharmonic; '
            'in such cases this FST parametrization will be invalid'],
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
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':None ,
        'postprocess_dets':None ,
        'notes': ['extinct language','front/backness harmonizes progressively',
            'i is transparent',
            'compounded words may constitute multiple harmonic domains, '
            'meaning this FST MAY NOT BE VALID FOR COMPOUNDED WORDS',
            '/a/ and /e/ are treated as archiphonemes, despite /a/ in its traditional '
            'representation differing multifeaturally from /e/'],
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
        'bidir_subseq':False,
        'hyphenate_suffix': False,#technically, suffix is only input to this
        'preprocess_dets':"If there is a suffix (hyphen) & /i/ is only vowel "
            "in the stem, then store stem and only input the suffix into this",
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
                       (3,F_M_R_T):('o',3),(3,F_L_U_T):('a',3),(3,'a'):('a',3),
                       (4,'?'):('?',4),(4,'i'):('i',4),(4,'e'):('o',4),
                       (4,'u'):('u',4),(4,'o'):('o',4),(4,'y'):('u',4),
                       (4,F_M_R_T):('o',4),(4,F_L_U_T):('a',4),(4,'a'):('a',4),},
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': True, #instruct user to hyphenate suffix if there is in fact a suffix in the input
        'preprocess_dets':"If there is a suffix, user should hyphenate like so "
            "for input: s t e m - s u f f i x; If /i/ is the only vowel that "
            "appears in the stem, input the stem into 17P, the output is then "
            "the untouched stem with the 17P output suffix; Otherwise "
            "(if there is a non-/i/ vowel in the stem), remove the hyphen and "
            "run the entire output through FST 17, return output",
        'postprocess_dets':None,
        'notes': ['Mongolic language','front/backness harmonizes progressively',
            'progressive stem-control labial harmony','i is transparent, except '
            'when it is the only vowel in the stem, in which case it triggers suffixal '
            'front-harmonization',
            'Key assumptions that were made despite lack of data: '
            'I assumed that rounded vowels only trigger rounding harmony if they '
            'are the first vowel in the word; additionally, I assumed that '
            '/e/ back-harmonizes to /o/' ,
            'Acoustic analysis by '
            '*[Frelinger, 2016](https://people.umass.edu/scable/LING404-SP16/Kalmyk/Student-Projects/Frelinger.pdf) , '
            'although necessarily preliminary and inconclusive, '
            'suggests that labial harmony is not so defined in Oirat; '
            'because this contradicts the prevalent perspective, however, '
            'such did not inform this FST'],
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
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':None,
        'postprocess_dets':None,
        'notes': ['Mongolic language','Progressive ATR/RTR and labial harmony',
            'i is transparent for both types of harmony',
            '/u,'+B_H_R_NT+'/ block [+labial] spreading such that following vowels '
            'are [-labial]','I did not find data of the form a...B_M_R_NT or e...o, '
            'so I assumed [-Labial] spreads progressively, just as [+Labial does]'],
        'harmony_feature':['ATR/RTR','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['/i/ for ATR/RTR and Labial'],
        'opaque':['/u, B_H_R_NT/ are blockers for [+labial], all that follows is [-labial]']
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
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':None,
        'postprocess_dets':None,
        'notes': ['Mongolic language',
            'Progressive ATR/RTR and labial harmony',
            'i is transparent for both types of harmony',
            'only'+ B_M_R_NT+' triggers [+labial] harmonization',
            'I did not find a sequence of [a...B_M_R_NT], so I assume that [a] '
            'triggers [-labial] harmony, but such is unconfirmed'],
        'harmony_feature':['ATR/RTR','Labial'],
        'sc':True,
        'dr':False,
        'transparent':['/i/ for ATR/RTR and Labial'],
        'opaque':None
    },
    20:
    {
        'name': 'Tunica harmony',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',12:'',13:''},
        'alphabet': ['i','e',F_M_U_NT,'u','o',B_M_R_NT,B_L_U_NT,'h',G_P_VL,'+','-','#'],
        'transitions':
        {(0,'+'):('',0),(1,'+'):('',1),(2,'+'):('',2),(3,'+'):('',3),(4,'+'):('',4),
         (5,'+'):('',5),(6,'+'):('',6),(7,'+'):('',7),(8,'+'):('',8),(9,'+'):('',9),
         (10,'+'):('',10),(11,'+'):('',11),(12,'+'):('',12),(13,'+'):('',13),
         (0,'-'):('',0),(1,'-'):('',1),(2,'-'):('',2),(3,'-'):('',3),(4,'-'):('',4),
         (5,'-'):('',5),(6,'-'):('',6),(7,'-'):('',7),(8,'-'):('',8),(9,'-'):('',9),
         (10,'-'):('',10),(11,'-'):('',11),(12,'-'):('',12),(13,'-'):('',13),
         (1,'#'):('i',13),(3,'#'):('e',13),(5,'#'):(F_M_U_NT,13),(7,'#'):('u',13),
         (9,'#'):('o',13),(11,'#'):(B_M_R_NT,13),
         (0,'#'):('',13),(2,'#'):('',13),(4,'#'):('',13),(6,'#'):('',13),
         (8,'#'):('',13),(10,'#'):('',13),(12,'#'):('',13),
         
         (13,'#'):('',13),(13,'i'):('',13),(13,'e'):('',13),(13,F_M_U_NT):('',13),
         (13,'u'):('',13),(13,'o'):('',13),(13,B_M_R_NT):('',13),(13,B_L_U_NT):('',13),
       (0,'?'):('?',0),(0,G_P_VL):(G_P_VL,0),(0,'h'):('h',0),(0,B_L_U_NT):(B_L_U_NT,0),
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
       (11,'h'):(B_M_R_NT+'h',12)
       },
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Append "#" to end of input',
        'postprocess_dets':None,
        'notes': ['Front/backness and roundness harmonize progressively',
            'harmonization is blocked by all consonants, except pharyngeals, '
            'which are transparent','vowels cannot appear consecutively, thus '
            'deletion of initial trigger vowels occurs in sequences of two adjacent '
            'vowels',
            'this FST incorporates deletion of first vowel in sequences of two vowels, '
            'it cannot process sequences of 3+ vowels properly, but it is assumed '
            'such sequences would never manifest'],
        'harmony_feature':['Palatal','Labial'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':None
    },
    21:
    {
        'name': 'Yoruba ATR harmony',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:''},
        'alphabet': ['i','u','a','e','o',F_M_U_NT,B_M_R_NT,'+'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),(5,'?'):('?',5),(0,'i'):('i',0),(0,'u'):('u',0),
            (0,'a'):('a',6),(1,'e'):('e',1),(1,'o'):('o',1),(1,F_M_U_NT):('e',1),
            (1,B_M_R_NT):('o',1),(3,'a'):('a',3),(4,'a'):('a',4),(2,F_M_U_NT):(F_M_U_NT,2),
            (2,B_M_R_NT):(B_M_R_NT,2),(2,'e'):(F_M_U_NT,2),(2,'o'):(B_M_R_NT,2),
            (0,'e'):('e',1),(0,'o'):('o',1),(0,F_M_U_NT):(F_M_U_NT,2),(0,B_M_R_NT):(B_M_R_NT,2),
            (1,'a'):('a',3),(3,'e'):('e',1),(3,'o'):('o',1),(3,F_M_U_NT):('e',1),
            (3,B_M_R_NT):('o',1),(3,'i'):('i',0),(3,'u'):('u',0),(1,'i'):('i',5),
            (1,'u'):('u',5),(5,'e'):('e',1),(5,'o'):('o',1),(5,F_M_U_NT):('e',1),(5,B_M_R_NT):('o',1),
            (5,'i'):('i',0),(5,'u'):('u',0),(5,'a'):('a',6),(2,'i'):('i',5),(2,'u'):('u',5),
            (2,'a'):('a',4),(4,F_M_U_NT):(F_M_U_NT,2),(4,'e'):(F_M_U_NT,2),(4,B_M_R_NT):(B_M_R_NT,2),
            (4,'o'):(B_M_R_NT,2),(4,'i'):('i',0),(4,'u'):('u',0),(6,'i'):('i',0),(6,'u'):('u',0),
            (6,'a'):('a',6),(6,'?'):('?',6),(6,'e'):('e',1),(6,'o'):('o',1),
            (6,F_M_U_NT):(F_M_U_NT,2),(6,B_M_R_NT):(B_M_R_NT,2),(0,'+'):('+',7),(1,'+'):('+',7),
            (5,'+'):('+',7),(2,'+'):('+',8),(3,'+'):('+',8),(4,'+'):('+',8),(6,'+'):('+',8),
            (7,'a'):('a',7),(7,'i'):('i',7),(7,'e'):('e',7),(7,'o'):('o',7),(7,'u'):('u',7),
            (7,F_M_U_NT):('e',7),(7,B_M_R_NT):('o',7),(7,'?'):('?',7),(8,'a'):('a',8),(8,'i'):('i',8),
            (8,'u'):('u',8),(8,'?'):('?',8),(8,F_M_U_NT):(F_M_U_NT,8),(8,B_M_R_NT):(B_M_R_NT,8),
            (8,'e'):(F_M_U_NT,8),(8,'o'):(B_M_R_NT,8)
           },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'plus_prefix':True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Need entire input entered (i.e., prefix+root as a whole '
            'if there is a prefix),Reverse the input before processing with FST',
        'postprocess_dets':'Reverse the output before returning to user',
        'notes': ['Yoruba lacks suffices',
            'Vowel inventory reference: A Grammar of Yoruba by Ayo Bamgbose',
            'primary reference: Yoruba Vowel Harmony by Diana Archangeli (DA)',
            'Regressive ATR', 'harmony differs somewhat between disyllabic contexts '
            'and contexts with more than 2 syllables',
            'DA seems to suggest that /e/ or /o/ cannot precede /a/, but this '
            'does not seem to reliably be the case in the data, therefore this '
            'FST treats /a/ like a transparent vowel, rather than a [-ATR] trigger'
            ' like DA seemingly posits','mid vowels trigger [+-ATR] harmony',
            'high vowels /i,u/ seem to reset the harmony domain in non-disyllabic '
            'monomorphemic stems, so they are treated as opaque blockers in stems; '
            'I treat them as transparent vowels in prefixes, however, but this may '
            'be a tenuous assertion and should be subject to scrutiny',
            'DA indicates that in sequences of MHM, wherein M=mid vowel and H=high '
            'vowel and in which consonants can separate the vowels, the first M MUST '
            'be [+ATR]; while I found this not to be the case in some words '
            '(e.g., foruk[back,mid,round,lax,-ATR]sil[front,mid,unrounded,lax,-ATR], '
            'ib[F_M_U_NT]rubojo), I adopted this assessment and incorporated it '
            'into the FST; this relationship does not seem to be the case for multiple '
            'high vowels between mid vowels (i.e., MHHM), nor do high vowels seem to ensure '
            '[+ATR] upon harmonic reset in all contexts','/i,u,a/, although not '
            'triggers in the stem, can trigger [ATR] characterization of the prefix; '
            'the first vowel of the stem triggers the ATR harmony of the prefix such '
            'that [+ATR] vowels /i,u,e,o/trigger [+ATR] harmony of the prefix, while '
            'the other [-ATR] vowels trigger [-ATR] harmony'],
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':['/a/','/i,u/ in prefixes'],
        'opaque':['/i,u/ in stems seem to initiate new harmonic domains']
    },

    22:
    {
        'name': 'Igbo ATR harmony',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','u','a','e','o','I',B_H_R_NT,B_M_R_NT,'+','-'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),(0,'+'):('+',0),(1,'+'):('+',1),(2,'+'):('+',2),(3,'+'):('+',3),
            (4,'+'):('+',4),(0,'i'):('i',1),(0,'u'):('u',1),(0,'e'):('e',1),(0,'o'):('o',1),
            (1,'i'):('i',1),(1,'u'):('u',1),(1,'e'):('e',1),(1,'o'):('o',1),(1,'-'):('-',3),
            (1,'I'):('I',2),(1,'a'):('a',2),(1,B_H_R_NT):(B_H_R_NT,2),(1,B_M_R_NT):(B_M_R_NT,2),
            (2,'i'):('i',1),(2,'u'):('u',1),(2,'e'):('e',1),(2,'o'):('o',1),
            (0,'I'):('I',2),(0,'a'):('a',2),(0,B_H_R_NT):(B_H_R_NT,2),(0,B_M_R_NT):(B_M_R_NT,2),
            (2,'I'):('I',2),(2,'a'):('a',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,B_M_R_NT):(B_M_R_NT,2),
            (2,'-'):('-',4),(0,'-'):('-',4),(3,'-'):('-',3),(3,'i'):('i',3),(3,'u'):('u',3),
            (3,'e'):('e',3),(3,'o'):('o',3),(3,'I'):('i',3),(3,B_H_R_NT):('u',3),
            (3,'a'):('e',3),(3,B_M_R_NT):('o',3),(4,'-'):('-',4),(4,'I'):('I',4),
            (4,'a'):('a',4),(4,B_M_R_NT):(B_M_R_NT,4),(4,B_H_R_NT):(B_H_R_NT,4),(4,'i'):('I',4),
            (4,'e'):('a',4),(4,'o'):(B_M_R_NT,4),(4,'u'):(B_H_R_NT,4)
           },
        'preprocess_req': False,
        'postprocess_req': True,
        'left_subseq': None, #with 22B, is technically bidirectional
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'',
        'postprocess_dets':'Reverse this output, and enter it into FST 22B',
        'notes': ['Roots do not alternate',
            'THIS FST IS NOT NECESSARILY ACCURATE FOR COMPOUND WORDS:+ATR and -ATR '
            'do not co-occur in same word, except in compounds or loanwords',
            'bidirectional subsequential harmonization','stem-control',
            'no transparent vowels'],
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None,

    },
    '22B':
    {
        'name': 'Igbo ATR harmony second direction',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','u','a','e','o','I',B_H_R_NT,B_M_R_NT,'+','-'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),(0,'-'):('-',0),(1,'-'):('-',1),(2,'-'):('-',2),(3,'-'):('-',3),
            (4,'-'):('-',4),(0,'i'):('i',1),(0,'u'):('u',1),(0,'e'):('e',1),(0,'o'):('o',1),
            (1,'i'):('i',1),(1,'u'):('u',1),(1,'e'):('e',1),(1,'o'):('o',1),(1,'+'):('+',3),
            (1,'I'):('I',2),(1,'a'):('a',2),(1,B_H_R_NT):(B_H_R_NT,2),(1,B_M_R_NT):(B_M_R_NT,2),
            (2,'i'):('i',1),(2,'u'):('u',1),(2,'e'):('e',1),(2,'o'):('o',1),
            (0,'I'):('I',2),(0,'a'):('a',2),(0,B_H_R_NT):(B_H_R_NT,2),(0,B_M_R_NT):(B_M_R_NT,2),
            (2,'I'):('I',2),(2,'a'):('a',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,B_M_R_NT):(B_M_R_NT,2),
            (2,'+'):('+',4),(0,'+'):('+',4),(3,'+'):('+',3),(3,'i'):('i',3),(3,'u'):('u',3),
            (3,'e'):('e',3),(3,'o'):('o',3),(3,'I'):('i',3),(3,B_H_R_NT):('u',3),
            (3,'a'):('e',3),(3,B_M_R_NT):('o',3),(4,'+'):('+',4),(4,'I'):('I',4),
            (4,'a'):('a',4),(4,B_M_R_NT):(B_M_R_NT,4),(4,B_H_R_NT):(B_H_R_NT,4),(4,'i'):('I',4),
            (4,'e'):('a',4),(4,'o'):(B_M_R_NT,4),(4,'u'):(B_H_R_NT,4)
           },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False, #with 22, is technically bidirectional
        'bidir_subseq':False,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'Should have been run through 22 and the reversed output '
            'of 22 should be 22Bs input',
        'postprocess_dets':'Reverse output, this is your final output',
        'notes': ['Roots do not alternate',
            'THIS FST IS NOT NECESSARILY ACCURATE FOR COMPOUND WORDS:+ATR and -ATR '
            'do not co-occur in same word, except in compounds or loanwords',
            'bidirectional subsequential harmonization','stem-control',
            'no transparent vowels'],

        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None,
    },

    23:
    {
        'name': 'Diola-Fogny (Jola-Fonyi) ATR harmony',
        'states': {0:'',1:''},
        'alphabet': ['i','u',schwa,'e','o','I',B_H_R_NT,B_M_R_NT,'a',F_M_U_NT],
        'transitions': {(0,'?'):('?',0),(1,'?'):('?',1),(0,'I'):('I',0),(0,'a'):('a',0),
                        (0,F_M_U_NT):(F_M_U_NT,0),(0,B_M_R_NT):(B_M_R_NT,0),
                        (0,B_H_R_NT):(B_H_R_NT,0),(0,'i'):('i',1),(0,'e'):('e',1),
                        (0,'o'):('o',1),(0,'u'):('u',1),(0,schwa):(schwa,1),(1,'e'):('e',1),
                        (1,'o'):('o',1),(1,'u'):('u',1),(1,schwa):(schwa,1),(1,'i'):('i',1),
                        (1,F_M_U_NT):('e',1),(1,B_M_R_NT):('o',1),(1,B_H_R_NT):('u',1),
                        (1,'a'):(schwa,1),(1,'I'):('i',1),
                       },
        'preprocess_req': False,
        'postprocess_req': True,
        'left_subseq': None,
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':None,
        'postprocess_dets':'Reverse output, run through 23 again, reverse again to get final output',
        'notes': ['+ATR and -ATR do not co-occur in same word',
            'dominant-recessive harmony wherein [+ATR] is the dominant feature '
            'and [-ATR] is recessive','no transparent vowels','/i,e,o,u,schwa/ '
            'are considered [+ATR], all other vowels are [-ATR], sound represented '
            'as schwa is considered [+ATR] despite the schwa symbol usually representing '
            'a particular [-ATR] phoneme','Language has alternating and non-alternating '
            'morphemes; the non-alternating morphemes always have only [+ATR] vowels, '
            'whereas the alternating morphemes alternate between all + or - ATR; '
            'If there is a non-alternating morpheme in a word, all vowels in that word '
            'are [+ATR], If not, all vowels are [-ATR] because [-ATR] is the default for'
            ' alternating morphemes'],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':True,
        'transparent':None,
        'opaque':None,
    },
    24:
    {
        'name': 'Kalenjin ATR harmony',
        'states': {0:'',1:'',2:''},
        'alphabet':
            ['!','i',Long_F_H_U_T,'u',Long_B_H_R_T,C_L_U_T,Long_C_L_U_T,'e',
            Long_F_M_U_T,'o',Long_B_M_R_T,'I',Long_F_H_U_NT,B_H_R_NT,Long_B_H_R_NT,
            B_M_R_NT,Long_B_M_R_NT,'a',Long_C_L_U_NT,F_M_U_NT,Long_F_M_U_NT],
        'transitions':
            {(0,'!'):('',0),(1,'!'):('',0),(2,'!'):('',0),
            (0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (0,'i'):('i',1),(1,'i'):('i',1),(0,'u'):('u',1),(1,'u'):('u',1),
            (0,'e'):('e',1),(1,'e'):('e',1),(0,'o'):('o',1),(1,'o'):('o',1),
            (0,C_L_U_T):(C_L_U_T,1),(1,C_L_U_T):(C_L_U_T,1),
            (0,Long_C_L_U_T):(Long_C_L_U_T,1),
            (1,Long_C_L_U_T):(Long_C_L_U_T,1),(0,Long_B_M_R_T):(Long_B_M_R_T,1),
            (1,Long_B_M_R_T):(Long_B_M_R_T,1),
            (0,Long_F_M_U_T):(Long_F_M_U_T,1),(1,Long_F_M_U_T):(Long_F_M_U_T,1),
            (0,Long_B_H_R_T):(Long_B_H_R_T,1),
            (1,Long_B_H_R_T):(Long_B_H_R_T,1),(0,Long_F_H_U_T):(Long_F_H_U_T,1),
            (1,Long_F_H_U_T):(Long_F_H_U_T,1),
            (1,'a'):(C_L_U_T,1),(1,B_M_R_NT):('o',1),(1,B_H_R_NT):('u',1),
            (1,F_M_U_NT):('e',1),(1,'I'):('i',1),
            (1,Long_C_L_U_NT):(Long_C_L_U_T,1),(1,Long_B_M_R_NT):(Long_B_M_R_T,1),
            (1,Long_B_H_R_NT):(Long_B_H_R_T,1),
            (1,Long_F_M_U_NT):(Long_F_M_U_T,1),(1,Long_F_H_U_NT):(Long_F_H_U_T,1),
            (0,'I'):('I',2),(0,B_H_R_NT):(B_H_R_NT,2),(0,F_M_U_NT):(F_M_U_NT,2),
            (0,B_M_R_NT):(B_M_R_NT,2),
            (0,'a'):('a',2),(0,Long_F_H_U_NT):(Long_F_H_U_NT,2),
            (0,Long_B_H_R_NT):(Long_B_H_R_NT,2),
            (0,Long_F_M_U_NT):(Long_F_M_U_NT,2),(0,Long_B_M_R_NT):(Long_B_M_R_NT,2),
            (0,Long_C_L_U_NT):(Long_C_L_U_NT,2),
            (2,'I'):('I',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,F_M_U_NT):(F_M_U_NT,2),
            (2,B_M_R_NT):(B_M_R_NT,2),
            (2,'a'):('a',2),(2,Long_F_H_U_NT):(Long_F_H_U_NT,2),
            (2,Long_B_H_R_NT):(Long_B_H_R_NT,2),
            (2,Long_F_M_U_NT):(Long_F_M_U_NT,2),(2,Long_B_M_R_NT):(Long_B_M_R_NT,2),
            (2,Long_C_L_U_NT):(Long_C_L_U_NT,2),
            (2,'i'):('I',2),(2,'u'):(B_H_R_NT,2),(2,'e'):(F_M_U_NT,2),
            (2,'o'):(B_M_R_NT,2),
            (2,C_L_U_T):('a',2),(2,Long_F_H_U_T):(Long_F_H_U_NT,2),
            (2,Long_B_H_R_T):(Long_B_H_R_NT,2),
            (2,Long_F_M_U_T):(Long_F_M_U_NT,2),(2,Long_B_M_R_T):(Long_B_M_R_NT,2),
            (2,Long_C_L_U_T):(Long_C_L_U_NT,2),
           },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': None,
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'For each individual prefix (form: pre+), root, suffix '
            '(form: -suffix), if in n-a_suff value, add "&" to beginning '
            '(ex: &-suffix)/elif in n-a_r&pre value, add "!" to end (ex: root!, prefix+!); '
            'Isolate joining of all prefixes, root, and the very first suffix '
            '(ex: pre+pre+root-suf); Reverse this - such is the input to this FST 24',
        'postprocess_dets':'Reverse the output, The processed prefixes will be the '
            'first part of the final output; take the processed root from this and '
            'join it with all of the suffixes in the initial input --such is the '
            'input for FST 24B',
        'notes':['ATR harmony','Length is contrastive for vowels',
            'Vowels in prefixes and roots harmonize with vowels of morpheme to their right, '
            'Suffixes harmonize with vowels of morpheme to their left',
            'There are alternating and non-alternating morphemes--non-alternating morphemes'
            ' reset harmonic domain, trigger harmony with their own vowels '
            '(thus, vowels of non-alternating morphemes are opaque de facto)',
            'While non-alternating morphemes with immutably [+ATR] vowels trigger [+ATR] '
            'harmony, I was unsure whether n-a morphemes with [-ATR] vowels also trigger '
            '[-ATR] harmony or simply block harmony; I assume they also trigger [-ATR] '
            'harmony for the sake of consistency amidst the equivocality'],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['Vowels within non-alternating morphemes are treated as opaque, '
            'triggering a new harmonic domain, perpetuating their own [ATR] feature '
            'until another non-alternating morpheme is encountered'],
        'n-a_suff': ['-e','-'+P_N_V+Long_C_L_U_T,'-'+A_LF_VL+'u',
            '-'+A_LF_VL+Long_C_L_U_T+'k','-n'+Long_C_L_U_T,'-'+A_LF_VL+Long_C_L_U_T,
            '-kej','-k'+Long_C_L_U_NT,'-kaj','-'+A_LF_VL+'w'+Long_C_L_U_NT+'k',
            '-k'+Long_F_M_U_NT], #add '&' at start of suffix (before -; ex: &-kej)
        'n-a_r&pre': ['k'+Long_F_M_U_T+'r','ma+','un',V_N_V+'et','kol',
            V_N_V+Long_F_M_U_NT+'t','k'+B_M_R_NT+'l'] #add ! at end of root or prefix (ex: un!; ma+!),
    },
    '24B':
    {
        'name': 'Kalenjin ATR harmony 2nd run',
        'states': {0:'',1:'',2:''},
        'alphabet':
            ['&','i',Long_F_H_U_T,'u',Long_B_H_R_T,C_L_U_T,Long_C_L_U_T,'e',
            Long_F_M_U_T,'o',Long_B_M_R_T,'I',Long_F_H_U_NT,B_H_R_NT,Long_B_H_R_NT,
            B_M_R_NT,Long_B_M_R_NT,'a',Long_C_L_U_NT,F_M_U_NT,Long_F_M_U_NT],
        'transitions':
            {(0,'&'):('',0),(1,'&'):('',0),(2,'&'):('',0),
            (0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (0,'i'):('i',1),(1,'i'):('i',1),(0,'u'):('u',1),(1,'u'):('u',1),
            (0,'e'):('e',1),(1,'e'):('e',1),(0,'o'):('o',1),(1,'o'):('o',1),
            (0,C_L_U_T):(C_L_U_T,1),(1,C_L_U_T):(C_L_U_T,1),
            (0,Long_C_L_U_T):(Long_C_L_U_T,1),
            (1,Long_C_L_U_T):(Long_C_L_U_T,1),(0,Long_B_M_R_T):(Long_B_M_R_T,1),
            (1,Long_B_M_R_T):(Long_B_M_R_T,1),
            (0,Long_F_M_U_T):(Long_F_M_U_T,1),(1,Long_F_M_U_T):(Long_F_M_U_T,1),
            (0,Long_B_H_R_T):(Long_B_H_R_T,1),
            (1,Long_B_H_R_T):(Long_B_H_R_T,1),(0,Long_F_H_U_T):(Long_F_H_U_T,1),
            (1,Long_F_H_U_T):(Long_F_H_U_T,1),
            (1,'a'):(C_L_U_T,1),(1,B_M_R_NT):('o',1),(1,B_H_R_NT):('u',1),
            (1,F_M_U_NT):('e',1),(1,'I'):('i',1),
            (1,Long_C_L_U_NT):(Long_C_L_U_T,1),(1,Long_B_M_R_NT):(Long_B_M_R_T,1),
            (1,Long_B_H_R_NT):(Long_B_H_R_T,1),
            (1,Long_F_M_U_NT):(Long_F_M_U_T,1),(1,Long_F_H_U_NT):(Long_F_H_U_T,1),
            (0,'I'):('I',2),(0,B_H_R_NT):(B_H_R_NT,2),(0,F_M_U_NT):(F_M_U_NT,2),
            (0,B_M_R_NT):(B_M_R_NT,2),
            (0,'a'):('a',2),(0,Long_F_H_U_NT):(Long_F_H_U_NT,2),
            (0,Long_B_H_R_NT):(Long_B_H_R_NT,2),
            (0,Long_F_M_U_NT):(Long_F_M_U_NT,2),(0,Long_B_M_R_NT):(Long_B_M_R_NT,2),
            (0,Long_C_L_U_NT):(Long_C_L_U_NT,2),
            (2,'I'):('I',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,F_M_U_NT):(F_M_U_NT,2),
            (2,B_M_R_NT):(B_M_R_NT,2),
            (2,'a'):('a',2),(2,Long_F_H_U_NT):(Long_F_H_U_NT,2),
            (2,Long_B_H_R_NT):(Long_B_H_R_NT,2),
            (2,Long_F_M_U_NT):(Long_F_M_U_NT,2),(2,Long_B_M_R_NT):(Long_B_M_R_NT,2),
            (2,Long_C_L_U_NT):(Long_C_L_U_NT,2),
            (2,'i'):('I',2),(2,'u'):(B_H_R_NT,2),(2,'e'):(F_M_U_NT,2),
            (2,'o'):(B_M_R_NT,2),
            (2,C_L_U_T):('a',2),(2,Long_F_H_U_T):(Long_F_H_U_NT,2),
            (2,Long_B_H_R_T):(Long_B_H_R_NT,2),
            (2,Long_F_M_U_T):(Long_F_M_U_NT,2),(2,Long_B_M_R_T):(Long_B_M_R_NT,2),
            (2,Long_C_L_U_T):(Long_C_L_U_NT,2),
           },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': None,
        'bidir_subseq':False,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'Should have already been run through 24 '
            '(with all the additional processing noted there)',
        'postprocess_dets':'Combine processed prefixes from 24 with the output '
            'of this (24B); this is the final output to the user',
        'notes':['ATR harmony','Length is contrastive for vowels',
            'Vowels in prefixes and roots harmonize with vowels of morpheme to their right, '
            'Suffixes harmonize with vowels of morpheme to their left',
            'There are alternating and non-alternating morphemes--non-alternating morphemes '
            'reset harmonic domain, trigger harmony with their own vowels '
            '(thus, vowels of non-alternating morphemes are opaque de facto)',
            'While non-alternating morphemes with immutably [+ATR] vowels trigger [+ATR] harmony, '
            'I was unsure whether n-a morphemes with [-ATR] vowels also trigger '
            '[-ATR] harmony or simply block harmony; I assume they also trigger '
            '[-ATR] harmony for the sake of consistency amidst the equivocality'],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['Vowels within non-alternating morphemes are treated as opaque, '
            'triggering a new harmonic domain, perpetuating their own [ATR] feature '
            'until another non-alternating morpheme is encountered'],
        'n-a_suff': ['-e','-'+P_N_V+Long_C_L_U_T,'-'+A_LF_VL+'u',
            '-'+A_LF_VL+Long_C_L_U_T+'k','-n'+Long_C_L_U_T,'-'+A_LF_VL+Long_C_L_U_T,
            '-kej','-k'+Long_C_L_U_NT,'-kaj','-'+A_LF_VL+'w'+Long_C_L_U_NT+'k',
            '-k'+Long_F_M_U_NT], #add '&' at start of suffix (before -; ex: &-kej)
        'n-a_r&pre': ['k'+Long_F_M_U_T+'r','ma+','un',V_N_V+'et','kol',
            V_N_V+Long_F_M_U_NT+'t','k'+B_M_R_NT+'l']
            #add ! at end of root or prefix (ex: un!; ma+!),
    },
    25:
    {
        'name': 'Asturian Lena (Romance) height harmony with inflectional suffixes',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['a','u','i','e','o',"'"],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (3,'?'):('?',3),(4,'?'):('?',4),(0,"'"):("'",0),(1,"'"):("'",3),
            (4,"'"):("'",3),(2,"'"):("'",2),(3,"'"):("'",3),(0,'u'):('u',1),
            (0,'i'):('i',2),(0,'e'):('e',2),(0,'o'):('o',2),(0,'a'):('a',2),
            (1,'u'):('u',4),(1,'i'):('i',4),(1,'e'):('e',4),(1,'o'):('o',4),
            (1,'a'):('a',4),(2,'u'):('u',2),(2,'i'):('i',2),(2,'e'):('e',2),
            (2,'o'):('o',2),(2,'a'):('a',2),(4,'u'):('u',2),(4,'i'):('i',2),
            (4,'e'):('e',2),(4,'o'):('o',2),(4,'a'):('a',2),(3,'i'):('i',2),
            (3,'u'):('u',2),(3,'e'):('i',2),(3,'o'):('u',2),(3,'a'):('e',2),},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        #Instruct user to insert a hyphen before the suffix
        #(ex. input: r o o t - s u f wherein suf is the suffix)
        'hyphenate_suffix': True,
        'preprocess_dets': "Entire user input (prefixes,stem, and suffixes; "
            "do not remove +s or -s) is needed as input here; "
            "reverse the input and enter it into this FST",
        'postprocess_dets':'Reverse the output',
        'notes': ['PLEASE INDICATE THAT A VOWEL IS STRESSED BY INCLUDING '
            'AN APOSTROPHE ("'") AFTER EACH STRESSED VOWEL (ex: kumpi"'"t)',
            'THIS FST ASSUMES THAT AN INFLECTIONAL SUFFIX IS THE LAST MORPHEME '
            'IN THE INPUT; IT WILL BE WRONG IF THAT IS NOT THE CASE',
            '[+high] harmonizes regressively from the ultimate vowel of '
            'an inflectional suffix','/u/ triggers harmony',
            'only stressed vowels are targets of harmony',
            'harmony targets the first stressed vowel within two vowels '
            'to the left of the trigger'
            ],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':['Unstressed vowels are transparent'],
        'opaque':None,
    },
26:
    {
        'name': 'Pasiego vowel harmony (metaphony, raising, and centralization)',
        'states': {0:'',1:'',2:'',3:''},
        'alphabet': ['a','u','i','e','o',"'",Cent_F_H_U_T,Cent_C_L_U_NT,
            Cent_B_M_R_T,Cent_B_H_R_T],
        'transitions':
            {(0,'?'):('?',1),(1,'?'):('?',1),(2,'?'):('?',2),
            (3,'?'):('?',3),(0,"'"):("'",0),(1,"'"):("'",1),
            (2,"'"):("'",3),(3,"'"):("'",3),(0,'a'):('a',1),
            (0,'o'):('o',1),(0,'e'):('e',1),
            (0,Cent_C_L_U_NT):(Cent_C_L_U_NT,1),(0,Cent_B_M_R_T):(Cent_B_M_R_T,1),
            (0,'u'):(Cent_B_H_R_T,2),(0,Cent_B_H_R_T):(Cent_B_H_R_T,2),
            (0,Cent_F_H_U_T):(Cent_F_H_U_T,2),
            (0,'i'):('i',2),(1,'a'):('a',1),(1,'o'):('o',1),(1,'e'):('e',1),
            (1,Cent_C_L_U_NT):(Cent_C_L_U_NT,1),
            (1,Cent_B_M_R_T):(Cent_B_M_R_T,1),(1,'u'):('u',2),(1,'i'):('i',2),
            (1,Cent_F_H_U_T):(Cent_F_H_U_T,2),
            (1,Cent_B_H_R_T):(Cent_B_H_R_T,2),(2,'i'):('i',2),(2,'u'):('u',2),
            (2,Cent_F_H_U_T):(Cent_F_H_U_T,2),
            (2,Cent_B_H_R_T):(Cent_B_H_R_T,2),(2,'a'):('a',1),(2,'o'):('o',1),
            (2,'e'):('e',1),
            (2,Cent_C_L_U_NT):(Cent_C_L_U_NT,1),(2,Cent_B_M_R_T):(Cent_B_M_R_T,1),
            (3,'i'):('i',2),
            (3,'u'):('u',2),(3,Cent_F_H_U_T):(Cent_F_H_U_T,2),
            (3,Cent_B_H_R_T):(Cent_B_H_R_T,2),
            (3,'e'):('i',1),(3,'o'):('u',1),(3,'a'):('a',1),
            (3,Cent_C_L_U_NT):(Cent_C_L_U_NT,1),
            (3,Cent_B_M_R_T):(Cent_B_H_R_T,1),},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets': "Reverse the input and enter it into this FST",
        'postprocess_dets':'Enter output into 26B',
        'notes': ['PLEASE INDICATE THAT A VOWEL IS STRESSED BY INCLUDING AN '
            'APOSTROPHE ("'") AFTER EACH STRESSED VOWEL (ex: kumpi"'"t)',
            'Vowel inventory is /i,e,a,o,u/, as well as their centralized variants',
            '/u/ becomes centralized when word-final; /i,e/ are produced as a schwa '
            'word-finally; /o/ becomes a high vowel word-finally, but is still thought'
            ' of as /o/',
            'Within a one-vowel window, a stressed mid vowel raises before a high vowel '
            '(metaphony)',
            'Mid vowels raise before a stressed syllable with a high vowel or a '
            'prevocalic glide (j,w)','Word-final centralized /u/ triggers regressive '
            'centralization (also professed to be [-ATR] harmony); /e/ is transparent '
            'for this harmony ',
            '/i,e,a,o,u/ are conceptualized as [+ATR] and their centralized counterparts '
            'are conceptualized as [-ATR]; in this way harmony involves ATR harmony/centralization'
            ],
        'harmony_feature':['Height','ATR/RTR'],
        'sc':False,
        'dr':False,
        'transparent':['Unstressed vowels are transparent to metaphony',
            '/a/ is transparent to height harmony (raising)',
            '/e/ is transparent to centralization'],
        'opaque':None,
    },
 '26B':
    {
        'name': 'Pasiego unstressed vowel raising',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:''},
        'alphabet': ['a','u','i','e','o',"'",'j','w',Cent_F_H_U_T,Cent_C_L_U_NT,Cent_B_M_R_T,Cent_B_H_R_T],
        'transitions':
        #(5,''):('',5) should never occur, but I included it;
        # if it does occur, the result will be inaccurate
            {(0,'?'):('?',0),(1,'?'):('?',0),(2,'?'):('?',3),
            (3,'?'):('?',3),(4,'?'):('?',0),(5,'?'):('?',0),(6,'?'):('?',2),
            (0,"'"):("'",1),(1,"'"):("'",1),
            (3,"'"):("'",4),(2,"'"):("'",2),(4,"'"):("'",4),(5,"'"):("'",5),
            (6,"'"):("'",6),
            (0,'j'):('j',0),(0,'w'):('w',0),(0,'a'):('a',0),
            (0,Cent_C_L_U_NT):(Cent_C_L_U_NT,0),
            (0,'e'):('e',0),(0,'o'):('o',0),(0,Cent_B_M_R_T):(Cent_B_M_R_T,0),
            (0,'i'):('i',0),(0,Cent_F_H_U_T):(Cent_F_H_U_T,0),(0,'u'):('u',0),
            (0,Cent_B_H_R_T):(Cent_B_H_R_T,0),
            (1,'e'):('e',1),(1,'o'):('o',1),(1,Cent_B_M_R_T):(Cent_B_M_R_T,1),
            (1,'a'):('a',1),
            (1,Cent_C_L_U_NT):(Cent_C_L_U_NT,1),(1,'i'):('i',2),(1,'u'):('u',2),
            (1,'j'):('j',2),(1,'w'):('w',2),
            (1,Cent_F_H_U_T):(Cent_F_H_U_T,2),(1,Cent_B_H_R_T):(Cent_B_H_R_T,2),
            (2,'a'):('a',2),(2,Cent_C_L_U_NT):(Cent_C_L_U_NT,2),
            (2,'e'):('e',2),(2,'o'):('o',2),(2,Cent_B_M_R_T):(Cent_B_M_R_T,2),
            (2,'i'):('i',2),
            (2,Cent_F_H_U_T):(Cent_F_H_U_T,2),(2,'u'):('u',2),(2,Cent_B_H_R_T):(Cent_B_H_R_T,2),
            (2,'j'):('j',3),(2,'w'):('w',3),(3,'j'):('j',3),(3,'w'):('w',3),
            (3,'e'):('i',5),
            (3,'a'):('a',5),(3,Cent_C_L_U_NT):(Cent_C_L_U_NT,5),(3,'u'):('u',5),
            (3,Cent_B_H_R_T):(Cent_B_H_R_T,5),
            (3,'i'):('i',5),(3,Cent_F_H_U_T):(Cent_F_H_U_T,5),(3,'o'):('u',5),
            (3,Cent_B_M_R_T):(Cent_B_H_R_T,5),
            (4,'j'):('j',2),(4,'w'):('w',2),(4,'a'):('a',4),(4,Cent_C_L_U_NT):(Cent_C_L_U_NT,4),
            (4,'o'):('u',4),(4,'e'):('i',4),(4,Cent_B_M_R_T):(Cent_B_H_R_T,4),
            (4,'i'):('i',6),
            (4,Cent_F_H_U_T):(Cent_F_H_U_T,6),(4,'u'):('u',6),(4,Cent_B_H_R_T):(Cent_B_H_R_T,6),
            (5,'j'):('j',0),(5,'w'):('w',0),(5,'i'):('i',5),(5,'u'):('u',5),
            (5,'a'):('a',5),
            (5,Cent_F_H_U_T):(Cent_F_H_U_T,5),(5,Cent_B_H_R_T):(Cent_B_H_R_T,5),
            (5,Cent_C_L_U_NT):(Cent_C_L_U_NT,5),
            (5,'o'):('u',5),(5,'e'):('i',5),(5,Cent_B_M_R_T):(Cent_B_H_R_T,5),
            (6,'j'):('j',2),(6,'w'):('w',2),(6,'a'):('a',6),
            (6,Cent_C_L_U_NT):(Cent_C_L_U_NT,6),
            (6,'o'):('u',6),(6,'e'):('i',6),(6,Cent_B_M_R_T):(Cent_B_H_R_T,6),
            (6,'i'):('i',6),(6,Cent_F_H_U_T):(Cent_F_H_U_T,6),(6,'u'):('u',6),
            (6,Cent_B_H_R_T):(Cent_B_H_R_T,6)},
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets': "FST 26",
        'postprocess_dets':'Enter output into 26C',
        'notes': ['PLEASE INDICATE THAT A VOWEL IS STRESSED BY INCLUDING AN '
            'APOSTROPHE ("'") AFTER EACH STRESSED VOWEL (ex: kumpi"'"t)',
            'Vowel inventory is /i,e,a,o,u/, as well as their centralized variants',
            '/u/ becomes centralized when word-final; /i,e/ are produced as a '
            'schwa word-finally; /o/ becomes a high vowel word-finally, '
            'but is still thought of as /o/',
            'Within a one-vowel window, a stressed mid vowel raises before a high vowel '
            '(metaphony)',
            'Mid vowels raise before a stressed syllable with a high vowel or a '
            'prevocalic glide (j,w)','Word-final centralized /u/ triggers regressive '
            'centralization (also professed to be [-ATR] harmony); /e/ is transparent '
            'for this harmony ','/i,e,a,o,u/ are conceptualized as [+ATR] and their '
            'centralized counterparts are conceptualized as [-ATR]; '
            'in this way harmony involves ATR harmony/centralization'
            ],
        'harmony_feature':['Height'],
        'sc':False,
        'dr':False,
        'transparent':['a'],
        'opaque':None,
    },
 '26C':
    {
        'name': 'Pasiego centralization (-ATR harmony)',
        'states': {0:'',1:'',2:''},
        'alphabet': ['a','u','i','e','o',Cent_F_H_U_T,Cent_C_L_U_NT,
            Cent_B_M_R_T,Cent_B_H_R_T],
        'transitions':
            {(0,'?'):('?',2),(1,'?'):('?',1),(2,'?'):('?',2),
           (0,Cent_B_H_R_T):(Cent_B_H_R_T,1),
           (0,'i'):('i',2),(0,'e'):('e',2),(0,'o'):('o',2),(0,'a'):('a',2),
           (0,'u'):('u',2),(0,Cent_F_H_U_T):(Cent_F_H_U_T,2),(0,Cent_C_L_U_NT):(Cent_C_L_U_NT,2),
           (0,Cent_B_M_R_T):(Cent_B_M_R_T,2),
           (2,'i'):('i',2),(2,'e'):('e',2),(2,'o'):('o',2),(2,'a'):('a',2),
           (2,'u'):('u',2),(2,Cent_F_H_U_T):(Cent_F_H_U_T,2),(2,Cent_C_L_U_NT):(Cent_C_L_U_NT,2),
           (2,Cent_B_M_R_T):(Cent_B_M_R_T,2),(2,Cent_B_H_R_T):(Cent_B_H_R_T,2),
           (1,'u'):(Cent_B_H_R_T,1),(1,'i'):(Cent_F_H_U_T,1),(1,'a'):(Cent_C_L_U_NT,1),
           (1,'o'):(Cent_B_M_R_T,1),(1,'e'):('e',1),(1,Cent_B_H_R_T):(Cent_B_H_R_T,1),
           (1,Cent_F_H_U_T):(Cent_F_H_U_T,1),(1,Cent_C_L_U_NT):(Cent_C_L_U_NT,1),
           (1,Cent_B_M_R_T):(Cent_B_M_R_T,1)},#(0,'u'):('u',2) should be impossible, but I included it anyways
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets': "26B",
        'postprocess_dets':'Reverse the output; this is the final output',
        'notes': ['PLEASE INDICATE THAT A VOWEL IS STRESSED BY INCLUDING AN '
            'APOSTROPHE ("'") AFTER EACH STRESSED VOWEL (ex: kumpi"'"t)',
            'Vowel inventory is /i,e,a,o,u/, as well as their centralized variants',
            '/u/ becomes centralized when word-final; /i,e/ are produced as a '
            'schwa word-finally; /o/ becomes a high vowel word-finally, but is '
            'still thought of as /o/','Within a one-vowel window, a stressed mid '
            'vowel raises before a high vowel (metaphony)','Mid vowels raise before '
            'a stressed syllable with a high vowel or a prevocalic glide (j,w)',
            'Word-final centralized /u/ triggers regressive centralization '
            '(also professed to be [-ATR] harmony); /e/ is transparent for this harmony ',
            '/i,e,a,o,u/ are conceptualized as [+ATR] and their centralized counterparts'
            ' are conceptualized as [-ATR]; in this way harmony involves ATR '
            'harmony/centralization'
            ],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':False,
        'transparent':['e'],
        'opaque':None,
    },
27:
    {
        'name': 'Pulaar dialect of Fula (Niger-Congo) ATR harmony',
        'states': {0:'',1:'',2:''},
        'alphabet': ['i','u','e','o','a',F_M_U_NT,B_M_R_NT],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (0,'i'):('i',1),(0,'u'):('u',1),(0,'e'):('e',1),(0,'o'):('o',1),
            (0,'a'):('a',2),(0,F_M_U_NT):(F_M_U_NT,2),(0,B_M_R_NT):(B_M_R_NT,2),
            (1,'e'):('e',1),(1,'o'):('o',1),(1,F_M_U_NT):('e',1),(1,B_M_R_NT):('o',1),
            (1,'i'):('i',1),(1,'u'):('u',1),(1,'a'):('a',2),
            (2,'i'):('i',1),(2,'u'):('u',1),(2,'a'):('a',2),
            (2,F_M_U_NT):(F_M_U_NT,2),(2,B_M_R_NT):(B_M_R_NT,2),
            (2,'e'):(F_M_U_NT,2),(2,'o'):(B_M_R_NT,2),
            },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        'plus_prefix':False,
        'hyphenate_suffix':False,
        'preprocess_dets':'Reverse input, then enter into this FST',
        'postprocess_dets':'Reverse output',
        'notes': ['Regressive ATR (pharyngeal) harmony','/i,u,e,o/ are phonemes '
            'with a [+ATR] specification; /a,front-mid-unrounded-lax vowel,'
            'back-mid-rounded-lax vowel/ are [-ATR] phonemes',
            '/i,u,a/ are blockers that trigger harmony for their own [ATR] specification'],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':False,
        'transparent':[],
        'opaque':['/i,u,a/ are opaque blockers that trigger harmony for their own'
        ' ATR featural specificiation'],
    },
 28:
    {
        'name': 'Maasai (Eastern Nilotic) ATR harmony',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','u','e','o',B_L_U_NT,'I',B_H_R_NT,F_M_U_NT,B_M_R_NT,'!','&'],
        'transitions':
        #transitions (0,'&'):('&',0),(1,'&'):('&',0),(1,'!'):('!',1),
        # (2,'!'):('!',2),(3,'!'):('!',3),(4,'!'):('!',4),(4,'&'):('&',4)
        #should all be impossible, but I include them anyways to allow every
        # state to have a transition for each character in the alphabet
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),(4,'?'):('?',4),
            (0,'!'):('!',1),(2,'&'):('&',4),(3,'&'):('&',0),(0,'&'):('&',0),(1,'&'):('&',0),
            (1,'!'):('!',1),(2,'!'):('!',2),(3,'!'):('!',3),(4,'!'):('!',4),(4,'&'):('&',4),
            (0,'i'):('i',0),(0,'u'):('u',0),(0,'e'):('e',0),(0,'o'):('o',0),(0,'I'):('I',0),
            (0,B_H_R_NT):(B_H_R_NT,0),(0,F_M_U_NT):(F_M_U_NT,0),(0,B_M_R_NT):(B_M_R_NT,0),
            (0,B_L_U_NT):(B_L_U_NT,0),
            (1,'i'):('i',2),(1,'u'):('u',2),(1,'e'):('e',2),(1,'o'):('o',2),(1,'I'):('I',3),
            (1,B_H_R_NT):(B_H_R_NT,3),(1,F_M_U_NT):(F_M_U_NT,3),(1,B_M_R_NT):(B_M_R_NT,3),
            (1,B_L_U_NT):(B_L_U_NT,3),
            (2,'i'):('i',2),(2,'u'):('u',2),(2,'e'):('e',2),(2,'o'):('o',2),(2,B_H_R_NT):(B_H_R_NT,3),
            (2,F_M_U_NT):(F_M_U_NT,3),(2,B_M_R_NT):(B_M_R_NT,3),(2,B_L_U_NT):(B_L_U_NT,3),(2,'I'):('I',3),
            (3,'I'):('I',3),(3,B_H_R_NT):(B_H_R_NT,3),(3,F_M_U_NT):(F_M_U_NT,3),(3,B_M_R_NT):(B_M_R_NT,3),
            (3,B_L_U_NT):(B_L_U_NT,3),(3,'i'):('i',2),(3,'u'):('u',2),(3,'e'):('e',2),(3,'o'):('o',2),
            (4,'i'):('i',4),(4,'u'):('u',4),(4,'e'):('e',4),(4,'o'):('o',4),(4,B_H_R_NT):('u',4),
            (4,F_M_U_NT):('e',4),(4,B_M_R_NT):('o',4),(4,B_L_U_NT):('o',4),(4,'I'):('i',4),
            },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': True,
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix':True,
        'preprocess_dets':'Add "!" to the beginning of the root/stem and "&" to '
            'the end of the root/stem (Ex: For input /a+b+c+ddd-e-f/, should get '
            '/a+b+c+!ddd&-e-f/; This is the input for FST 28',
        'postprocess_dets':'Output should be reversed and run through 28B',
        'notes': [
            'Dominant [+ATR] harmony; words are never mixed (i.e., they never have a '
            '[+ATR] vowel and a [-ATR] vowel), except in many instances with '
            '/B_L_U_NT/ which can act as an opaque blocker',
            'Maasai has 9 vowel phonemes:/i,u,e,o/ are [+ATR],/I,B_H_R_NT,F_M_U_NT,'
            'B_M_R_NT/ are [-ATR],/B_L_U_NT/ is [-ATR] but has no archiphoneme '
            'and tends to act as an opaque neutral','B_L_U_NT harmonizes only when '
            'in a suffix and preceded by a [+ATR] vowel; it prevents spread of [+ATR] '
            'to the left when it precedes a [+ATR] vowel','Some argue that Maasai '
            'demonstrates a single bidirectional harmony, but others argue that it '
            'demonstrates two unidirectional harmony patterns; although we mark this '
            'FST as bidirectional, we take no real stance on this greater theory'],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':True,
        'transparent':[],
        'opaque':['[low,back,-ATR] vowel is opaque and blocks harmony, '
            'except when it is in a suffix and is preceded by a [-ATR] vowel '
            'in which case it manifests as [o]',],
    },
'28B':
    {
        'name': 'Maasai secondary FST for RtoL',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:''},
        'alphabet': ['i','u','e','o',B_L_U_NT,'I',B_H_R_NT,F_M_U_NT,B_M_R_NT,'!','&'],
        'transitions':
        #Many transitions that should be impossible were included
        #for the sake of having a transition for each alphabet symbol from each state
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),
            (5,'?'):('?',5),(6,'?'):('?',6),(7,'?'):('?',7),(8,'?'):('?',8),
            (0,'!'):('',0),
            (0,'&'):('',3),(1,'!'):('',1),(1,'&'):('',8),(2,'!'):('',2),(2,'&'):('',3),
            (8,'&'):('',8),(8,'!'):('',6),(3,'!'):('',7),(3,'&'):('',3),(4,'&'):('',4),
            (4,'!'):('',6),(5,'&'):('',5),(5,'!'):('',7),(6,'!'):('',6),(6,'&'):('',6),
            (7,'!'):('',7),(7,'&'):('',7),
            (0,'I'):('I',0),(0,B_H_R_NT):(B_H_R_NT,0),(0,F_M_U_NT):(F_M_U_NT,0),
            (0,B_M_R_NT):(B_M_R_NT,0),
            (0,'i'):('i',1),(0,'u'):('u',1),(0,'e'):('e',1),(0,'o'):('o',1),
            (0,B_L_U_NT):(B_L_U_NT,2),
            (1,'i'):('i',1),(1,'u'):('u',1),(1,'e'):('e',1),(1,'o'):('o',1),
            (1,B_L_U_NT):(B_L_U_NT,2),
            (1,'I'):('i',1),(1,B_H_R_NT):('u',1),(1,F_M_U_NT):('e',1),
            (1,B_M_R_NT):('o',1),
            (2,'i'):('i',1),(2,'u'):('u',1),(2,'e'):('e',1),(2,'o'):('o',1),
            (2,B_L_U_NT):(B_L_U_NT,2),
            (2,'I'):('I',2),(2,B_H_R_NT):(B_H_R_NT,2),(2,F_M_U_NT):(F_M_U_NT,2),
            (2,B_M_R_NT):(B_M_R_NT,2),
            (3,'i'):('i',4),(3,'u'):('u',4),(3,'e'):('e',4),(3,'o'):('o',4),
            (3,B_L_U_NT):(B_L_U_NT,5),
            (3,'I'):('I',5),(3,B_H_R_NT):(B_H_R_NT,5),(3,F_M_U_NT):(F_M_U_NT,5),
            (3,B_M_R_NT):(B_M_R_NT,5),
            (4,'i'):('i',4),(4,'u'):('u',4),(4,'e'):('e',4),(4,'o'):('o',4),
            (4,B_L_U_NT):(B_L_U_NT,5),
            (4,'I'):('I',5),(4,B_H_R_NT):(B_H_R_NT,5),(4,F_M_U_NT):(F_M_U_NT,5),
            (4,B_M_R_NT):(B_M_R_NT,5),
            (5,'i'):('i',4),(5,'u'):('u',4),(5,'e'):('e',4),(5,'o'):('o',4),
            (5,B_L_U_NT):(B_L_U_NT,5),
            (5,'I'):('I',5),(5,B_H_R_NT):(B_H_R_NT,5),(5,F_M_U_NT):(F_M_U_NT,5),
            (5,B_M_R_NT):(B_M_R_NT,5),
            (6,'i'):('i',6),(6,'u'):('u',6),(6,'e'):('e',6),(6,'o'):('o',6),
            (6,B_L_U_NT):(B_L_U_NT,7),
            (6,'I'):('i',6),(6,B_H_R_NT):('u',6),(6,F_M_U_NT):('e',6),
            (6,B_M_R_NT):('o',6),
            (7,'i'):('i',6),(7,'u'):('u',6),(7,'e'):('e',6),(7,'o'):('o',6),
            (7,B_L_U_NT):(B_L_U_NT,7),
            (7,'I'):('I',7),(7,B_H_R_NT):(B_H_R_NT,7),(7,F_M_U_NT):(F_M_U_NT,7),
            (7,B_M_R_NT):(B_M_R_NT,7),
            (8,'i'):('i',8),(8,'u'):('u',8),(8,'e'):('e',8),(8,'o'):('o',8),
            (8,B_L_U_NT):(B_L_U_NT,7),
            (8,'I'):('i',8),(8,B_H_R_NT):('u',8),(8,F_M_U_NT):('e',8),
            (8,B_M_R_NT):('o',8),
            },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix':True,
        'preprocess_dets':'Should have been processed and run through 28 accordingly; '
            'Reverse the output from 28 and enter into this FST',
        'postprocess_dets':'Reverse output, this is the final output to user',
        'notes': ['Dominant [+ATR] harmony; words are never mixed (i.e., they '
            'never have a [+ATR] vowel and a [-ATR] vowel), except in many '
            'instances with /B_L_U_NT/ which can act as an opaque blocker',
            'Maasai has 9 vowel phonemes:/i,u,e,o/ are [+ATR],/I,B_H_R_NT,F_M_U_NT,'
            'B_M_R_NT/ are [-ATR],/B_L_U_NT/ is [-ATR] but has no archiphoneme and '
            'tends to act as an opaque neutral','B_L_U_NT harmonizes only when in a '
            'suffix and preceded by a [+ATR] vowel; it prevents spread of [+ATR] to '
            'the left when it precedes a [+ATR] vowel','Some argue that Maasai '
            'demonstrates a single bidirectional harmony, but others argue that '
            'it demonstrates two unidirectional harmony patterns; although we mark '
            'this FST as bidirectional, we take no real stance on this greater theory'
        ],
        'harmony_feature':['ATR/RTR'],
        'sc':False,
        'dr':True,
        'transparent':[],
        'opaque':['[low,back,-ATR] vowel is opaque and blocks harmony, except '
            'when it is in a suffix and is preceded by a [-ATR] vowel in which '
            'case it manifests as [o]',],
    },
29:
    {
        'name': 'Kashaya (Pomoan) translaryngeal harmony',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''},
        'alphabet': ['i',Long_F_H_U_T,'u',Long_B_H_R_T,'e',Long_F_M_U_T,'o',
        Long_B_M_R_T,'a',Long_C_L_U_NT,'h','+','-',G_P_VL],
        'transitions':
        #VV sequence is prohibited in syllable structure,
        #but I included transtions to account for such anyways
        #(I assume that the second vowel does harmonize in such a sequence;
        #it is not possible to conclude if it would or not because such data isn't available
            {(0,'?'):('?',0),(1,'?'):('?',0),(2,'?'):('?',0),(3,'?'):('?',0),
            (4,'?'):('?',0),(5,'?'):('?',0),(6,'?'):('?',0),(7,'?'):('?',0),
            (8,'?'):('?',0),(9,'?'):('?',0),(10,'?'):('?',0),
            (0,'+'):('+',0),(1,'+'):('+',0),(2,'+'):('+',0),(3,'+'):('+',0),
            (4,'+'):('+',0),(5,'+'):('+',0),(6,'+'):('+',0),(7,'+'):('+',0),
            (8,'+'):('+',0),(9,'+'):('+',0),(10,'+'):('+',0),
            (0,'-'):('-',0),(1,'-'):('-',0),(2,'-'):('-',0),(3,'-'):('-',0),
            (4,'-'):('-',0),(5,'-'):('-',0),(6,'-'):('-',0),(7,'-'):('-',0),
            (8,'-'):('-',0),(9,'-'):('-',0),(10,'-'):('-',0),
            (0,'h'):('h',0),(1,'h'):('h',6),(2,'h'):('h',7),(3,'h'):('h',8),
            (4,'h'):('h',9),(5,'h'):('h',10),(6,'h'):('h',0),(7,'h'):('h',0),
            (8,'h'):('h',0),(9,'h'):('h',0),(10,'h'):('h',0),
            (0,G_P_VL):(G_P_VL,0),(1,G_P_VL):(G_P_VL,6),(2,G_P_VL):(G_P_VL,7),
            (3,G_P_VL):(G_P_VL,8),
            (4,G_P_VL):(G_P_VL,9),(5,G_P_VL):(G_P_VL,10),(6,G_P_VL):(G_P_VL,0),
            (7,G_P_VL):(G_P_VL,0),
            (8,G_P_VL):(G_P_VL,0),(9,G_P_VL):(G_P_VL,0),(10,G_P_VL):(G_P_VL,0),
            (0,'i'):('i',1),(0,Long_F_H_U_T):(Long_F_H_U_T,1),
            (0,'u'):('u',2),(0,Long_B_H_R_T):(Long_B_H_R_T,2),
            (0,'e'):('e',3),(0,Long_F_M_U_T):(Long_F_M_U_T,3),
            (0,'o'):('o',4),(0,Long_B_M_R_T):(Long_B_M_R_T,4),
            (0,'a'):('a',5),(0,Long_C_L_U_NT):(Long_C_L_U_NT,5),
            (1,'i'):('i',1),(1,Long_F_H_U_T):(Long_F_H_U_T,1),
            (1,'u'):('i',1),(1,Long_B_H_R_T):(Long_F_H_U_T,1),
            (1,'e'):('i',1),(1,Long_F_M_U_T):(Long_F_H_U_T,1),
            (1,'o'):('i',1),(1,Long_B_M_R_T):(Long_F_H_U_T,1),
            (1,'a'):('i',1),(1,Long_C_L_U_NT):(Long_F_H_U_T,1),
            (2,'i'):('u',2),(2,Long_F_H_U_T):(Long_B_H_R_T,2),
            (2,'u'):('u',2),(2,Long_B_H_R_T):(Long_B_H_R_T,2),
            (2,'e'):('u',2),(2,Long_F_M_U_T):(Long_B_H_R_T,2),
            (2,'o'):('u',2),(2,Long_B_M_R_T):(Long_B_H_R_T,2),
            (2,'a'):('u',2),(2,Long_C_L_U_NT):(Long_B_H_R_T,2),
            (3,'i'):('e',3),(3,Long_F_H_U_T):(Long_F_M_U_T,3),
            (3,'u'):('e',3),(3,Long_B_H_R_T):(Long_F_M_U_T,3),
            (3,'e'):('e',3),(3,Long_F_M_U_T):(Long_F_M_U_T,3),
            (3,'o'):('e',3),(3,Long_B_M_R_T):(Long_F_M_U_T,3),
            (3,'a'):('e',3),(3,Long_C_L_U_NT):(Long_F_M_U_T,3),
            (4,'i'):('o',4),(4,Long_F_H_U_T):(Long_B_M_R_T,4),
            (4,'u'):('o',4),(4,Long_B_H_R_T):(Long_B_M_R_T,4),
            (4,'e'):('o',4),(4,Long_F_M_U_T):(Long_B_M_R_T,4),
            (4,'o'):('o',4),(4,Long_B_M_R_T):(Long_B_M_R_T,4),
            (4,'a'):('o',4),(4,Long_C_L_U_NT):(Long_B_M_R_T,4),
            (5,'i'):('a',5),(5,Long_F_H_U_T):(Long_C_L_U_NT,5),
            (5,'u'):('a',5),(5,Long_B_H_R_T):(Long_C_L_U_NT,5),
            (5,'e'):('a',5),(5,Long_F_M_U_T):(Long_C_L_U_NT,5),
            (5,'o'):('a',5),(5,Long_B_M_R_T):(Long_C_L_U_NT,5),
            (5,'a'):('a',5),(5,Long_C_L_U_NT):(Long_C_L_U_NT,5),
            (6,'i'):('i',1),(6,Long_F_H_U_T):(Long_F_H_U_T,1),
            (6,'u'):('i',1),(6,Long_B_H_R_T):(Long_F_H_U_T,1),
            (6,'e'):('i',1),(6,Long_F_M_U_T):(Long_F_H_U_T,1),
            (6,'o'):('i',1),(6,Long_B_M_R_T):(Long_F_H_U_T,1),
            (6,'a'):('i',1),(6,Long_C_L_U_NT):(Long_F_H_U_T,1),
            (7,'i'):('u',2),(7,Long_F_H_U_T):(Long_B_H_R_T,2),
            (7,'u'):('u',2),(7,Long_B_H_R_T):(Long_B_H_R_T,2),
            (7,'e'):('u',2),(7,Long_F_M_U_T):(Long_B_H_R_T,2),
            (7,'o'):('u',2),(7,Long_B_M_R_T):(Long_B_H_R_T,2),
            (7,'a'):('u',2),(7,Long_C_L_U_NT):(Long_B_H_R_T,2),
            (8,'i'):('e',3),(8,Long_F_H_U_T):(Long_F_M_U_T,3),
            (8,'u'):('e',3),(8,Long_B_H_R_T):(Long_F_M_U_T,3),
            (8,'e'):('e',3),(8,Long_F_M_U_T):(Long_F_M_U_T,3),
            (8,'o'):('e',3),(8,Long_B_M_R_T):(Long_F_M_U_T,3),
            (8,'a'):('e',3),(8,Long_C_L_U_NT):(Long_F_M_U_T,3),
            (9,'i'):('o',4),(9,Long_F_H_U_T):(Long_B_M_R_T,4),
            (9,'u'):('o',4),(9,Long_B_H_R_T):(Long_B_M_R_T,4),
            (9,'e'):('o',4),(9,Long_F_M_U_T):(Long_B_M_R_T,4),
            (9,'o'):('o',4),(9,Long_B_M_R_T):(Long_B_M_R_T,4),
            (9,'a'):('o',4),(9,Long_C_L_U_NT):(Long_B_M_R_T,4),
            (10,'i'):('a',5),(10,Long_F_H_U_T):(Long_C_L_U_NT,5),
            (10,'u'):('a',5),(10,Long_B_H_R_T):(Long_C_L_U_NT,5),
            (10,'e'):('a',5),(10,Long_F_M_U_T):(Long_C_L_U_NT,5),
            (10,'o'):('a',5),(10,Long_B_M_R_T):(Long_C_L_U_NT,5),
            (10,'a'):('a',5),(10,Long_C_L_U_NT):(Long_C_L_U_NT,5),
            },
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'Run input through FST "29P" first; then run that output through here',
        'postprocess_dets':'',
        'notes':
            ['/i,e,u,o,a/ and their long variants are contrastive phonemes in Kashaya',
             'left-subsequential translaryngeal vowel identity harmony within an '
             'individual morpheme (for a sequence V1HV2,'
             ' wherein H is a laryngeal consonant, V2 manifests with the identity of V1)',
             'I assume that vowel length does not harmonize',
             'Kashaya has a CV(C) or CV: syllable structure, so consecutive Vs should be '
             'prohibited; despite this, however,'
             ' this FST assumes if VV does appear, identity harmony will occur; there is a '
             'lack of data to support this, of course',
             'Complete (identity) harmony only applies within native morphemes',
             'Only glottal consonants are considered laryngeal for this language',
             'Prior to performing identity harmony, a preliminary FST performs various '
             'relevant vowel rules that I assume occur prior to ID harmony'
             'in derivation of surface form; these "rules" are as follows: i->a/m-_ , '
             'i->u/d_ , V->a/uvular_; The last rule is somewhat'
             ' inadequate in that a vowel may manifest as [o] after a labialized uvular '
             'consonant, but the FST does not implement such'
             ' nuance and is thus somewhat inaccurate','This FST assumes harmony cannot '
             'occur across multiple laryngeal consonants',
             'Height harmony can also occur in Kashaya in that the vowel /u/ in an '
             'instrumental prefix manifests as [o] when'
             ' the following syllable contains /o/; this tool does not implement '
             'this height harmony pattern'],
        'harmony_feature':['Complete'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':['Non-"laryngeal" (in this case, non-glottal) '
            'consonants block this identity harmony'],
        },
'29P':
    {
        'name': 'Kashaya (Pomoan) preliminary vowel transformations',
        'states': {0:'',1:'',2:'',3:'',4:'',},
        'alphabet': ['m','d','q','i',Long_F_H_U_T,'u',Long_B_H_R_T,'e',
            Long_F_M_U_T,'o',Long_B_M_R_T,'a',Long_C_L_U_NT,'-'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',0),(2,'?'):('?',0),(3,'?'):('?',0),(4,'?'):('?',0),
            (0,'-'):('-',0),(1,'-'):('-',0),(2,'-'):('-',3),(3,'-'):('-',3),(4,'-'):('-',0),
            (0,'q'):('q',1),(1,'q'):('q',1),(2,'q'):('q',1),(3,'q'):('q',1),(4,'q'):('q',1),
            (0,'m'):('m',2),(1,'m'):('m',2),(2,'m'):('m',2),(3,'m'):('m',2),(4,'m'):('m',2),
            (0,'d'):('d',4),(1,'d'):('d',4),(2,'d'):('d',4),(3,'d'):('d',4),(4,'d'):('d',4),
            (0,'i'):('i',0),(0,Long_F_H_U_T):(Long_F_H_U_T,0),
            (0,'u'):('u',0),(0,Long_B_H_R_T):(Long_B_H_R_T,0),
            (0,'e'):('e',0),(0,Long_F_M_U_T):(Long_F_M_U_T,0),
            (0,'o'):('o',0),(0,Long_B_M_R_T):(Long_B_M_R_T,0),
            (0,'a'):('a',0),(0,Long_C_L_U_NT):(Long_C_L_U_NT,0),
            (1,'i'):('a',0),(1,Long_F_H_U_T):(Long_C_L_U_NT,0),
            (1,'u'):('a',0),(1,Long_B_H_R_T):(Long_C_L_U_NT,0),
            (1,'e'):('a',0),(1,Long_F_M_U_T):(Long_C_L_U_NT,0),
            (1,'o'):('a',0),(1,Long_B_M_R_T):(Long_C_L_U_NT,0),
            (1,'a'):('a',0),(1,Long_C_L_U_NT):(Long_C_L_U_NT,0),
            (2,'i'):('i',0),(2,Long_F_H_U_T):(Long_F_H_U_T,0),
            (2,'u'):('u',0),(2,Long_B_H_R_T):(Long_B_H_R_T,0),
            (2,'e'):('e',0),(2,Long_F_M_U_T):(Long_F_M_U_T,0),
            (2,'o'):('o',0),(2,Long_B_M_R_T):(Long_B_M_R_T,0),
            (2,'a'):('a',0),(2,Long_C_L_U_NT):(Long_C_L_U_NT,0),
            (3,'i'):('a',0),(3,Long_F_H_U_T):(Long_C_L_U_NT,0),
            (3,'u'):('u',0),(3,Long_B_H_R_T):(Long_B_H_R_T,0),
            (3,'e'):('e',0),(3,Long_F_M_U_T):(Long_F_M_U_T,0),
            (3,'o'):('o',0),(3,Long_B_M_R_T):(Long_B_M_R_T,0),
            (3,'a'):('a',0),(3,Long_C_L_U_NT):(Long_C_L_U_NT,0),
            (4,'i'):('u',0),(4,Long_F_H_U_T):(Long_B_H_R_T,0),
            (4,'u'):('u',0),(4,Long_B_H_R_T):(Long_B_H_R_T,0),
            (4,'e'):('e',0),(4,Long_F_M_U_T):(Long_F_M_U_T,0),
            (4,'o'):('o',0),(4,Long_B_M_R_T):(Long_B_M_R_T,0),
            (4,'a'):('a',0),(4,Long_C_L_U_NT):(Long_C_L_U_NT,0),
            },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':False,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'Reverse input before running through here',
        'postprocess_dets':'Reverse output; then run it through FST 29 to get final output to user',
        'notes':[''],
        'harmony_feature':[''],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':[],
        },
 30:
    {
        'name': 'Standard Hungarian palatal harmony of alternating suffixes',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:''},
        'alphabet': ['!','-','i',Long_F_H_U_T,Long_F_M_U_T,F_M_U_NT,'y',
            Long_F_H_R_T,F_M_R_T,Long_F_M_R_T,'u',Long_B_H_R_T,'o',Long_B_M_R_T,
            Long_C_L_U_NT,B_M_R_NT],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),(5,'?'):('?',5),(6,'?'):('?',6),(7,'?'):('?',7),
            (0,'!'):('',1),(1,'!'):('',1),(2,'!'):('',2),(3,'!'):('',3),
            (4,'!'):('',4),(5,'!'):('',5),(6,'!'):('',6),(7,'!'):('',7),
            (0,'-'):('-',6),(1,'-'):('-',6),(2,'-'):('-',6),(3,'-'):('-',7),
            (4,'-'):('-',7),(5,'-'):('-',6),(6,'-'):('-',6),(7,'-'):('-',7),
            (0,'i'):('i',0),(0,Long_F_H_U_T):(Long_F_H_U_T,0),
            (0,Long_F_M_U_T):(Long_F_M_U_T,0),
            (0,F_M_U_NT):(F_M_U_NT,0),(0,'y'):('y',0),(0,Long_F_H_R_T):(Long_F_H_R_T,0),
            (0,F_M_R_T):(F_M_R_T,0),(0,Long_F_M_R_T):(Long_F_M_R_T,0),(0,'u'):('u',0),
            (0,Long_B_H_R_T):(Long_B_H_R_T,0),(0,'o'):('o',0),
            (0,Long_B_M_R_T):(Long_B_M_R_T,0),
            (0,Long_C_L_U_NT):(Long_C_L_U_NT,0),(0,B_M_R_NT):(B_M_R_NT,0),
            (1,'i'):('i',1),(1,Long_F_H_U_T):(Long_F_H_U_T,1),
            (1,Long_F_M_U_T):(Long_F_M_U_T,1),
            (1,F_M_U_NT):(F_M_U_NT,1),(1,'y'):('y',2),(1,Long_F_H_R_T):(Long_F_H_R_T,2),
            (1,F_M_R_T):(F_M_R_T,2),(1,Long_F_M_R_T):(Long_F_M_R_T,2),(1,'u'):('u',3),
            (1,Long_B_H_R_T):(Long_B_H_R_T,3),(1,'o'):('o',3),
            (1,Long_B_M_R_T):(Long_B_M_R_T,3),
            (1,Long_C_L_U_NT):(Long_C_L_U_NT,3),(1,B_M_R_NT):(B_M_R_NT,3),
            (2,'i'):('i',2),(2,Long_F_H_U_T):(Long_F_H_U_T,2),
            (2,Long_F_M_U_T):(Long_F_M_U_T,2),
            (2,F_M_U_NT):(F_M_U_NT,2),(2,'y'):('y',2),(2,Long_F_H_R_T):(Long_F_H_R_T,2),
            (2,F_M_R_T):(F_M_R_T,2),(2,Long_F_M_R_T):(Long_F_M_R_T,2),(2,'u'):('u',3),
            (2,Long_B_H_R_T):(Long_B_H_R_T,3),(2,'o'):('o',3),
            (2,Long_B_M_R_T):(Long_B_M_R_T,3),
            (2,Long_C_L_U_NT):(Long_C_L_U_NT,3),(2,B_M_R_NT):(B_M_R_NT,3),
            (3,'i'):('i',4),(3,Long_F_H_U_T):(Long_F_H_U_T,4),
            (3,Long_F_M_U_T):(Long_F_M_U_T,4),
            (3,F_M_U_NT):(F_M_U_NT,4),(3,'y'):('y',2),(3,Long_F_H_R_T):(Long_F_H_R_T,2),
            (3,F_M_R_T):(F_M_R_T,2),(3,Long_F_M_R_T):(Long_F_M_R_T,2),(3,'u'):('u',3),
            (3,Long_B_H_R_T):(Long_B_H_R_T,3),(3,'o'):('o',3),
            (3,Long_B_M_R_T):(Long_B_M_R_T,3),
            (3,Long_C_L_U_NT):(Long_C_L_U_NT,3),(3,B_M_R_NT):(B_M_R_NT,3),
            (4,'i'):('i',5),(4,Long_F_H_U_T):(Long_F_H_U_T,5),
            (4,Long_F_M_U_T):(Long_F_M_U_T,5),
            (4,F_M_U_NT):(F_M_U_NT,5),(4,'y'):('y',2),(4,Long_F_H_R_T):(Long_F_H_R_T,2),
            (4,F_M_R_T):(F_M_R_T,2),(4,Long_F_M_R_T):(Long_F_M_R_T,2),(4,'u'):('u',3),
            (4,Long_B_H_R_T):(Long_B_H_R_T,3),(4,'o'):('o',3),
            (4,Long_B_M_R_T):(Long_B_M_R_T,3),
            (4,Long_C_L_U_NT):(Long_C_L_U_NT,3),(4,B_M_R_NT):(B_M_R_NT,3),
            (5,'i'):('i',5),(5,Long_F_H_U_T):(Long_F_H_U_T,5),
            (5,Long_F_M_U_T):(Long_F_M_U_T,5),
            (5,F_M_U_NT):(F_M_U_NT,5),(5,'y'):('y',2),(5,Long_F_H_R_T):(Long_F_H_R_T,2),
            (5,F_M_R_T):(F_M_R_T,2),(5,Long_F_M_R_T):(Long_F_M_R_T,2),(5,'u'):('u',3),
            (5,Long_B_H_R_T):(Long_B_H_R_T,3),(5,'o'):('o',3),
            (5,Long_B_M_R_T):(Long_B_M_R_T,3),
            (5,Long_C_L_U_NT):(Long_C_L_U_NT,3),(5,B_M_R_NT):(B_M_R_NT,3),
            (6,'i'):('i',6),(6,Long_F_H_U_T):(Long_F_H_U_T,6),
            (6,Long_F_M_U_T):(Long_F_M_U_T,6),
            (6,F_M_U_NT):(F_M_U_NT,6),(6,'y'):('y',6),(6,Long_F_H_R_T):(Long_F_H_R_T,6),
            (6,F_M_R_T):(F_M_R_T,6),(6,Long_F_M_R_T):(Long_F_M_R_T,6),(6,'u'):('y',6),
            (6,Long_B_H_R_T):(Long_F_H_R_T,6),(6,'o'):(F_M_R_T,6),
            (6,Long_B_M_R_T):(Long_F_M_R_T,6),
            (6,Long_C_L_U_NT):(Long_F_M_U_T,6),(6,B_M_R_NT):(F_M_U_NT,6),
            (7,'i'):('i',7),(7,Long_F_H_U_T):(Long_F_H_U_T,7),
            (7,Long_F_M_U_T):(Long_C_L_U_NT,7),
            (7,F_M_U_NT):(B_M_R_NT,7),(7,'y'):('u',7),
            (7,Long_F_H_R_T):(Long_B_H_R_T,7),
            (7,F_M_R_T):('o',7),(7,Long_F_M_R_T):(Long_B_M_R_T,7),(7,'u'):('u',7),
            (7,Long_B_H_R_T):(Long_B_H_R_T,7),(7,'o'):('o',7),
            (7,Long_B_M_R_T):(Long_B_M_R_T,7),
            (7,Long_C_L_U_NT):(Long_C_L_U_NT,7),(7,B_M_R_NT):(B_M_R_NT,7),
           },
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': True, #instruct user to hyphenate suffix if there is in fact a suffix in the input
        'preprocess_dets':"Add '!' at the beginning of "
            "the root/stem (ex: pre+pre+root-suf-suf -> pre+pre+!root-suf-suf); "
            "then enter into FST",
        'postprocess_dets':None,
        'notes':
        ['Std Hungarian also has labial vowel harmony, but it is not represented in this FST',
        'Hungarian suffixes are either fixed or alternating in backness; only alternating'
        ' suffixes harmonize, so non-alternating suffixes will produce invalid output with this FST',
        'Vowel phonemes are /i, i:, e:, y, y:,u, u:, o, o:, a:, back-mid-rounded-lax'
        ',front-mid-rounded-tense,long front-mid-rounded-tense, front-mid-unrounded-lax/',
        '/i,i:,e:,front-mid-unrounded-lax/ are quasi-neutrals','If the closest vowel to the'
        ' left of an alternating suffix is a non-neutral front vowel, then the suffix will front-harmonize',
        'If the closest vowel to the left of an alternating suffix is a back vowel, '
        'then the suffix will back-harmonize',
        'If the closest vowel to the left of an alternating suffix is a neutral vowel, '
        'it varies what palatal quality the suffix vowels will demonstrate:'
        'If the last non-neutral vowel was a front vowel, then the suffix will have front vowels; '
        'if the root has only neutral vowels,'
        'then the suffix will have front vowels; if the last non-neutral vowel is back, '
        'the quality of the vowels in the suffix depend'
        'on the number of neutrals between that back vowel and the suffix--such that more '
        'neutrals increase probability of front-harmony--'
        ',the height of the intervening neutral vowels--such that higher neutral vowels '
        'increase the likelihood of front-harmony--'
        ',and a variety of other factors; thus BECAUSE THE HARMONY IS PROBABILISTIC IN THIS CASE, '
        'THE FST WILL FAIL TO PERFECTLY REPRESENT THIS PHENOMENON',
        'Acknowledging the probabilistic nature of this harmony, various assumptions were made '
        'that make the FST potentially inaccurate; these'
        'manifest in the decision to make a root-final vowel sequence of BN lead to back-harmony, '
        'but a sequence of BNN or even more Ns produce front-harmony,'
        'thus avoiding a likelihood-based FST','Quasi-neutrals /e,F_M_U_NT/ alternate with '
        '/a:,B_M_R_NT/ in alternating suffixes',
        'In general, /y,y:,F_M_R_T,Long_F_M_R_T/ alternate with /u,u:,o,o:/,respectively, '
        'in alternating suffixes',
        'While this FST assumes binary suffixes, there are quaternary suffixes which alternate '
        'between four different vowels'
        ],
        'harmony_feature':['Palatal'],
        'sc':True,
        'dr':False,
        'transparent':['/i,e,F_M_U_NT/ are quasi-transparent as triggers'],
        'opaque':['/i,e,F_M_U_NT/sometimes "behave" opaquely, lending to front harmony']
    },
 31:
    {
        'name': 'Nawuri (North Guang) ATR harmony',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['i','u','e','o',B_L_U_NT,'I',B_H_R_NT,F_M_U_NT,B_M_R_NT,'!','-'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),(3,'?'):('?',3),
            (4,'?'):('?',4),(0,'-'):('-',0),(1,'-'):('-',4),(2,'-'):('-',3),
            (3,'-'):('-',3),(4,'-'):('-',4),
            (0,'i'):('i',0),(0,'u'):('u',0),(0,'e'):('e',0),(0,'o'):('o',0),
            (0,'I'):('I',0),(0,B_H_R_NT):(B_H_R_NT,0),(0,F_M_U_NT):(F_M_U_NT,0),
            (0,B_M_R_NT):(B_M_R_NT,0),
            (0,B_L_U_NT):(B_L_U_NT,0),
            (0,'!'):('',1),(1,'!'):('',1),(2,'!'):('',2),(3,'!'):('',3),
            (4,'!'):('',4),
            (1,'I'):('I',1),(1,B_H_R_NT):(B_H_R_NT,1),(1,F_M_U_NT):(F_M_U_NT,1),
            (1,B_M_R_NT):(B_M_R_NT,1),
            (1,B_L_U_NT):(B_L_U_NT,1),(1,'i'):('i',2),(1,'u'):('u',2),(1,'e'):('e',2),
            (1,'o'):('o',2),
            (2,'i'):('i',2),(2,'u'):('u',2),(2,'e'):('e',2),(2,'o'):('o',2),
            (2,'I'):('i',2),(2,B_H_R_NT):('u',2),(2,F_M_U_NT):('e',2),
            (2,B_M_R_NT):('o',2),
            (2,B_L_U_NT):(B_L_U_NT,1),
            (3,'i'):('i',3),(3,'u'):('u',3),(3,'e'):('e',3),(3,'o'):('o',3),
            (3,'I'):('i',3),(3,B_H_R_NT):('u',3),(3,F_M_U_NT):('e',3),
            (3,B_M_R_NT):('o',3),
            (3,B_L_U_NT):(B_L_U_NT,4),
            (4,'i'):('i',4),(4,'u'):('u',4),(4,'e'):('e',4),(4,'o'):('o',4),
            (4,'I'):('I',4),(4,B_H_R_NT):(B_H_R_NT,4),(4,F_M_U_NT):(F_M_U_NT,4),
            (4,B_M_R_NT):(B_M_R_NT,4),
            (4,B_L_U_NT):(B_L_U_NT,4),
           },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': True,
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix':True,
        'preprocess_dets':'Add "!" to the beginning of the root/stem and "&" '
                'to the end of the root/stem (Ex: For input /a+b+c+ddd-e-f/,'
                ' should get /a+b+c+!ddd&-e-f/; This is the input for FST 31',
        'postprocess_dets':'Output should be reversed and run through 31B',
        'notes': ['Dialect represented is that delineated in "Nawuri ATR harmony in typological perspective"'
                  'by Roderic Casali (2002)',
                  'Morpheme-internal cross-height ATR harmony',
                  'Casali conveys Nawuri as stem-control with [+ATR] dominant over [-ATR]',
                  'Nawuri has 9 vowel phonemes /i,u,e,o,I,B_H_R_NT,F_M_U_NT,B_M_R_NT,C_L_U_NT/,'
                  ' as well as long counterparts to many of them;the first four listed are'
                  '[+ATR], while the others are [-ATR]',
                 'Centralization, raising, and dipthongization phonetic vowel processes exist,'
                 ' but were not incorporated into this FST because we only included phonemic'
                  'representations','The decision to take a broad phonological parametrization'
                  'may contribute to ambiguity given that multiple phonemes may share an allophone'
                  '(ex: /a/ and /B_M_R_NT/ can both manifest as B_M_U_NT in particular contexts',
                 'Harmony only affects a subset of affixes: there are many harmonizing prefixes '
                 'and at least one harmonizing suffix','THIS FST ASSUMES ALL AFFIXES IN THE INPUT'
                  'ARE HARMONIZING AFFIXES, WHICH PRODUCES INACCURATE OUTPUTS WHEN SUCH IS NOT THE CASE',
                 'B_L_U_NT is a neutral vowel which sometimes behaves transparently and sometimes opaquely:'
                 'it blocks the rightward spreading of [+ATR], causing a following harmonizing suffix to manifest'
                 'as [-ATR] (i.e., if it is the last vowel of the root, the following suffix -if alternating- will'
                 ' have [-ATR] vowels; it does not block leftward [+ATR] spreading, however (i.e., if a root'
                 ' has [+ATR] vowels, but B_L_U_NT as its leftmost vowel, [+ATR] may still spread to the preceding prefixes',
                 'Some believe B_L_U_NT is not a neutral, but instead subtley phonetically raises before a [+ATR] vowel;'
                 'Because we are only employing phonemic representations, such is not practically relevant',
                 'There can also be [+ATR] assimilation across word boundaries and within compounds,'
                 ' but THIS FST CAN ONLY TREAT SIMPLE ROOTS WITH HARMONIZING AFFIXES',
                 'Nawuri also demonstrates labial harmony in some contexts, but this FST does not '
                 'incorporate it'],
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':True,
        'transparent':['B_L_U_NT seems to allow leftward spreading of [+ATR], behaving transparently'],
        'opaque':['B_L_U_NT seems to block rightward spreading of [+ATR],behaving opaquely'],
    },
'31B':
    {
        'name': 'Nawuri secondary FST for RtoL',
        'states': {0:'',1:'',2:'',},
        'alphabet': ['i','u','e','o',B_L_U_NT,'I',B_H_R_NT,F_M_U_NT,B_M_R_NT,'&'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (0,'i'):('i',0),(0,'u'):('u',0),(0,'e'):('e',0),(0,'o'):('o',0),
            (0,'I'):('I',0),(0,B_H_R_NT):(B_H_R_NT,0),(0,F_M_U_NT):(F_M_U_NT,0),
            (0,B_M_R_NT):(B_M_R_NT,0),
            (0,B_L_U_NT):(B_L_U_NT,0),
            (0,'&'):('',1),(1,'&'):('',1),(2,'&'):('',2),
            (1,'I'):('I',1),(1,B_H_R_NT):(B_H_R_NT,1),(1,F_M_U_NT):(F_M_U_NT,1),
            (1,B_M_R_NT):(B_M_R_NT,1),
            (1,B_L_U_NT):(B_L_U_NT,1),(1,'i'):('i',2),(1,'u'):('u',2),(1,'e'):('e',2),
            (1,'o'):('o',2),
            (2,'i'):('i',2),(2,'u'):('u',2),(2,'e'):('e',2),(2,'o'):('o',2),
            (2,'I'):('i',2),(2,B_H_R_NT):('u',2),(2,F_M_U_NT):('e',2),
            (2,B_M_R_NT):('o',2),
            (2,B_L_U_NT):(B_L_U_NT,2),
           },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': False,
        'bidir_subseq':True,
        'plus_prefix':True,
        'hyphenate_suffix':True,
        'preprocess_dets':'Should have been processed and run through 31 accordingly; '
            'Reverse the output from 31 and enter into this FST',
        'postprocess_dets':'Reverse output, this is the final output to user',
        'notes': [],
        'harmony_feature':['ATR/RTR'],
        'sc':True,
        'dr':True,
        'transparent':[],
        'opaque':[],
    },
 32:
    {
        'name': 'Kinendeule (Rufiji) height harmony for verbal extensions',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',12:'',13:'',14:''},
        'alphabet': ['a','u','i','e','o',F_M_U_NT,B_M_R_NT,'-'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (3,'?'):('?',3),(4,'?'):('?',4),(5,'?'):('?',5),
            (6,'?'):('?',6),(7,'?'):('?',7),(8,'?'):('?',8),
            (9,'?'):('?',9),(10,'?'):('?',10),(11,'?'):('?',11),
            (12,'?'):('?',12),(13,'?'):('?',13),(14,'?'):('?',14),
            (0,'-'):('-',14),(1,'-'):('-',8),(2,'-'):('-',9),
            (3,'-'):('-',10),(4,'-'):('-',11),(5,'-'):('-',12),
            (6,'-'):('-',13),(7,'-'):('-',14),(8,'-'):('-',8),
            (9,'-'):('-',9),(10,'-'):('-',10),(11,'-'):('-',11),
            (12,'-'):('-',12),(13,'-'):('-',13),(14,'-'):('-',14),
            (0,'i'):('i',1),(1,'i'):('i',1),(2,'i'):('i',1),
            (3,'i'):('i',1),(4,'i'):('i',1),(5,'i'):('i',1),
            (6,'i'):('i',1),(7,'i'):('i',1),
            (0,'e'):('e',2),(1,'e'):('e',2),(2,'e'):('e',2),
            (3,'e'):('e',2),(4,'e'):('e',2),(5,'e'):('e',2),
            (6,'e'):('e',2),(7,'e'):('e',2),
            (0,F_M_U_NT):(F_M_U_NT,3),(1,F_M_U_NT):(F_M_U_NT,3),
            (2,F_M_U_NT):(F_M_U_NT,3),(3,F_M_U_NT):(F_M_U_NT,3),
            (4,F_M_U_NT):(F_M_U_NT,3),(5,F_M_U_NT):(F_M_U_NT,3),
            (6,F_M_U_NT):(F_M_U_NT,3),(7,F_M_U_NT):(F_M_U_NT,3),
            (0,'u'):('u',4),(1,'u'):('u',4),(2,'u'):('u',4),
            (3,'u'):('u',4),(4,'u'):('u',4),(5,'u'):('u',4),
            (6,'u'):('u',4),(7,'u'):('u',4),
            (0,'o'):('o',5),(1,'o'):('o',5),(2,'o'):('o',5),
            (3,'o'):('o',5),(4,'o'):('o',5),(5,'o'):('o',5),
            (6,'o'):('o',5),(7,'o'):('o',5),
            (0,B_M_R_NT):(B_M_R_NT,6),(1,B_M_R_NT):(B_M_R_NT,6),
            (2,B_M_R_NT):(B_M_R_NT,6),(3,B_M_R_NT):(B_M_R_NT,6),
            (4,B_M_R_NT):(B_M_R_NT,6),(5,B_M_R_NT):(B_M_R_NT,6),
            (6,B_M_R_NT):(B_M_R_NT,6),(7,B_M_R_NT):(B_M_R_NT,6),
            (8,'i'):('i',8),(8,'e'):('i',8),(8,F_M_U_NT):('i',8),
            (8,'u'):('u',8),(8,'o'):('u',8),(8,B_M_R_NT):('u',8),
            (8,'a'):('a',8),
            (9,'e'):('e',9),(9,'i'):('e',9),(9,F_M_U_NT):('e',9),
            (9,'u'):('u',9),(9,'o'):('u',9),(9,B_M_R_NT):('u',9),
            (9,'a'):('a',9),
            (10,F_M_U_NT):(F_M_U_NT,10),(10,'i'):(F_M_U_NT,10),
            (10,'e'):(F_M_U_NT,10),(10,'u'):('u',10),
            (10,'o'):('u',10),(10,B_M_R_NT):('u',10),
            (10,'a'):('a',10),
            (11,'i'):('i',11),(11,'e'):('i',11),(11,F_M_U_NT):('i',11),
            (11,'u'):('u',11),(11,'o'):('u',11),(11,B_M_R_NT):('u',11),
            (11,'a'):('a',11),
            (12,'e'):('e',12),(12,'i'):('e',12),(12,F_M_U_NT):('e',12),
            (12,'u'):('o',12),(12,'o'):('o',12),(12,B_M_R_NT):('o',12),
            (12,'a'):('a',12),
            (13,F_M_U_NT):(F_M_U_NT,13),(13,'i'):(F_M_U_NT,13),
            (13,'e'):(F_M_U_NT,13),(13,'u'):(B_M_R_NT,13),
            (13,'o'):(B_M_R_NT,13),(13,B_M_R_NT):(B_M_R_NT,13),
            (13,'a'):('a',13),
            (14,'i'):('i',14),(14,'e'):('i',14),(14,F_M_U_NT):('i',14),
            (14,'u'):('u',14),(14,'o'):('u',14),(14,B_M_R_NT):('u',14),
            (14,'a'):('a',14),
            },
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': True,
        'preprocess_dets': '',
        'postprocess_dets':'',
        'notes': ['Vowel phonemes are /i,e,F_M_U_NT,u,o,B_M_R_NT,a/',
                  '/i,e,F_M_U_NT/ are front;/u,o,B_M_R_NT/ are back',
                  '/i,u/,/e,o/,/F_M_U_NT,B_M_R_NT/ "lie" at '
                  'different heights',
                  'Vowel harmony process represented here'
                  'is left-subsequential and stem-controlled',
                  'Process represented here is specifically suffixal harmony:'
                  'the harmonization of verbal extensions with the preceding root '
                  'radical',
                  'THUS, THIS FST IS ONLY ACCURATE WHEN THE INPUT IS A VERB '
                  'AND THE ROOT IS FOLLOWED BY HARMONIZING EXTENSIONS',
                  'THE VERBAL EXTENSIONS MUST BE HYPHENATED AS YOU WOULD SUFFIXES '
                  '(ex: dind-ul-a, wherein /u/ is the extension)',
                  'THIS FST WILL HARMONIZE ALL SUFFIXES FOLLOWING THE ROOT, '
                  'MEANING IT WILL PRODUCE INACCURACIES FOR NON-HARMONIZING SUFFIXES '
                  'THAT FOLLOW',
                  'For harmonizing extensions, those which alternate between '
                  'front vowels have /i/ as their default vowel quality, those '
                  'which alternate between back vowels have /u/ as their default, '
                  'and those with /a/ do not deviate from /a/',
                  'The trigger for extension harmony is the last vowel of the preceding'
                  'root, but potential triggers are constrained depending on the extension: '
                  'Harmony for extensions with front vowels can be triggered by front or back vowels'
                  ', but harmony for those with back vowels can only be triggered by back vowels',
                  'Height harmony manifests as alternation between the heights of /i,u/,/e,o/,'
                  ' and /F_M_U_NT,B_M_R_NT/',
                  '/a/ is transparent to harmony; because it cannot trigger height harmony, following'
                  'extensions must manifest with the default height (/i,u/)',
                  'Affixes before the root do not harmonize',
                  'Primary source is "Vowel Harmony in Kindendeule and Chingoni Languages '
                  '"of Tanzania" by Deo Ngonyani'
                 ],
        'harmony_feature':['Height'],
        'sc':True,
        'dr':False,
        'transparent':['a'],
        'opaque':None,
    },
 33:
    {
        'name': 'Chingoni (Rufiji) height harmony for verbal extensions',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''},
        'alphabet': ['a','u','i',F_M_U_NT,B_M_R_NT,'-'],
        'transitions':
            {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2),
            (3,'?'):('?',3),(4,'?'):('?',4),(5,'?'):('?',5),
            (6,'?'):('?',6),(7,'?'):('?',7),(8,'?'):('?',8),
            (9,'?'):('?',9),(10,'?'):('?',10),
            (0,'-'):('-',10),(1,'-'):('-',6),(2,'-'):('-',7),
            (3,'-'):('-',8),(4,'-'):('-',9),(5,'-'):('-',10),
            (6,'-'):('-',6),(7,'-'):('-',7),(8,'-'):('-',8),
            (9,'-'):('-',9),(10,'-'):('-',10),
            (0,'i'):('i',1),(1,'i'):('i',1),(2,'i'):('i',1),
            (3,'i'):('i',1),(4,'i'):('i',1),(5,'i'):('i',1),
            (0,F_M_U_NT):(F_M_U_NT,2),(1,F_M_U_NT):(F_M_U_NT,2),
            (2,F_M_U_NT):(F_M_U_NT,2),(3,F_M_U_NT):(F_M_U_NT,2),
            (4,F_M_U_NT):(F_M_U_NT,2),(5,F_M_U_NT):(F_M_U_NT,2),
            (0,'u'):('u',3),(1,'u'):('u',3),(2,'u'):('u',3),
            (3,'u'):('u',3),(4,'u'):('u',3),(5,'u'):('u',3),
            (0,B_M_R_NT):(B_M_R_NT,4),(1,B_M_R_NT):(B_M_R_NT,4),
            (1,B_M_R_NT):(B_M_R_NT,4),(3,B_M_R_NT):(B_M_R_NT,4),
            (4,B_M_R_NT):(B_M_R_NT,4),(5,B_M_R_NT):(B_M_R_NT,4),
            (0,'a'):('a',5),(1,'a'):('a',5),(2,'a'):('a',5),
            (3,'a'):('a',5),(4,'a'):('a',5),(5,'a'):('a',5),
            (6,'i'):('i',6),(6,'u'):('u',6),(6,F_M_U_NT):('i',6),
            (6,'a'):('a',6),(6,B_M_R_NT):('u',6),
            (7,'i'):(F_M_U_NT,7),(7,'u'):('u',7),(7,F_M_U_NT):(F_M_U_NT,7),
            (7,B_M_R_NT):('u',7),(7,'a'):('a',7),
            (8,'i'):('i',8),(8,'u'):('u',8),(8,F_M_U_NT):('i',8),
            (8,'a'):('a',8),(8,B_M_R_NT):('u',8),
            (9,'i'):(F_M_U_NT),(9,'u'):(B_M_R_NT,9),(9,F_M_U_NT):(F_M_U_NT,9,
            (9,B_M_R_NT):(B_M_R_NT,9),(9,'a'):('a',9),                                                     
            (10,'i'):('i'10),(10,'u'):('u',10),(10,F_M_U_NT):('i',10),
            (10,'a'):('a',10),(10,B_M_R_NT):('u',10),
            },
        'preprocess_req': False,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': True,
        'preprocess_dets': '',
        'postprocess_dets':'',
        'notes': ['Vowel phonemes are /i,F_M_U_NT,u,B_M_R_NT,a/',
                  '/i,F_M_U_NT/ are front;/u,B_M_R_NT/ are back',
                  '/i,u/,/F_M_U_NT,B_M_R_NT/,/a/ "lie" at '
                  'different heights',
                  'Vowel harmony process represented here'
                  'is left-subsequential and stem-controlled',
                  'Process represented here is specifically suffixal harmony:'
                  'the harmonization of verbal extensions with the preceding root '
                  'radical',
                  'THUS, THIS FST IS ONLY ACCURATE WHEN THE INPUT IS A VERB '
                  'AND THE ROOT IS FOLLOWED BY HARMONIZING EXTENSIONS',
                  'THE VERBAL EXTENSIONS MUST BE HYPHENATED AS YOU WOULD SUFFIXES ',                  
                  'THIS FST WILL HARMONIZE ALL SUFFIXES FOLLOWING THE ROOT, '
                  'MEANING IT WILL PRODUCE INACCURACIES FOR NON-HARMONIZING SUFFIXES '
                  'THAT FOLLOW',
                  'For harmonizing extensions, those which alternate between '
                  'front vowels have /i/ as their default vowel quality, those '
                  'which alternate between back vowels have /u/ as their default, '
                  'and those with /a/ do not deviate from /a/',
                  'The trigger for extension harmony is the last vowel of the preceding'
                  'root, but potential triggers are constrained depending on the extension: '
                  'Harmony for extensions with front vowels can be triggered by front or back vowels'
                  ', but harmony for those with back vowels can only be triggered by back vowels',
                  'Height harmony manifests as alternation between the heights of /i,u/'
                  ' and /F_M_U_NT,B_M_R_NT/',
                  '/a/ is transparent to harmony; because it cannot trigger height harmony, following'
                  'extensions must manifest with the default height (/i,u/)',
                  'Affixes before the root do not harmonize',
                  'Primary source is "Vowel Harmony in Kindendeule and Chingoni Languages '
                  '"of Tanzania" by Deo Ngonyani'
            ],
        'harmony_feature':['Height'],
        'sc':True,
        'dr':False,
        'transparent':['a'],
        'opaque':None,
    },
 '34P': #eliminates '+' symbols in the string as a side-effect of how FST is designed; shouldn't matter, though
    {
        'name': 'Yawelmani vowel epenthesis',
        'states': {0:'',1:'',2:'',3:'',4:''},
        'alphabet': ['+','-','#','i','u','e','o','a',Long_F_H_U_T,Long_F_M_U_T,Long_B_H_R_T,Long_B_M_R_T,Long_C_L_U_NT],
        'transitions':
        {(0,'-'):('-',0),(0,'+'):('',0),(0,'#'):('#',4),(0,'?'):('?',1),
         (1,'+'):('',1),(1,'-'):('-',1),(1,'#'):('#',4),(1,'?'):('',2),
         (2,'+'):('',2),(2,'-'):('',3),(2,'?'):('i?'),(2,'#'):('?#',4),
         (3,'+'):('',3),(3,'-'):('',3),(3,'?'):('i?-',2),(3,'#'):('?#',4),
         (4,'+'):('',4),(4,'-'):('',4),(4,'?'):('',4), #any transition from 4 is pointless but included for sake of having transition for each alphabet symbol for each state
         (4,'#'):('',4),
         (4,'i'):('',4),(0,'i'):('i',0),(1,'i'):('i',0),(2,'i'):('?i',0),
         (3,'i'):('?-i',0),
         (4,'u'):('',4),(0,'u'):('u',0),(1,'u'):('u',0),(2,'u'):('?u',0),
         (3,'u'):('?-u',0),
         (4,'e'):('',4),(0,'e'):('e',0),(1,'e'):('e',0),(2,'e'):('?e',0),
         (3,'e'):('?-e',0),
         (4,'o'):('',4),(0,'o'):('o',0),(1,'o'):('o',0),(2,'o'):('?o',0),
         (3,'o'):('?-o',0),
         (4,'a'):('',4),(0,'a'):('a',0),(1,'a'):('a',0),(2,'a'):('?a',0),
         (3,'a'):('?-a',0),
         (4,Long_F_H_U_T):('',4),(0,Long_F_H_U_T):(Long_F_H_U_T,0),(1,Long_F_H_U_T):(Long_F_H_U_T,0),(2,Long_F_H_U_T):('?'+Long_F_H_U_T,0),
         (3,Long_F_H_U_T):('?-'+Long_F_H_U_T,0),
         (4,Long_F_M_U_T):('',4),(0,Long_F_M_U_T):(Long_F_M_U_T,0),(1,Long_F_M_U_T):(Long_F_M_U_T,0),(2,Long_F_M_U_T):('?'+Long_F_M_U_T,0),
         (3,Long_F_M_U_T):('?-'+Long_F_M_U_T,0),
         (4,Long_B_H_R_T):('',4),(0,Long_B_H_R_T):(Long_B_H_R_T,0),(1,Long_B_H_R_T):(Long_B_H_R_T,0),(2,Long_B_H_R_T):('?'+Long_B_H_R_T,0),
         (3,Long_B_H_R_T):('?-'+Long_B_H_R_T,0),
         (4,Long_B_M_R_T):('',4),(0,Long_B_M_R_T):(Long_B_M_R_T,0),(1,Long_B_M_R_T):(Long_B_M_R_T,0),(2,Long_B_M_R_T):('?'+Long_B_M_R_T,0),
         (3,Long_B_M_R_T):('?-'+Long_B_M_R_T,0),
         (4,Long_C_L_U_NT):('',4),(0,Long_C_L_U_NT):(Long_C_L_U_NT,0),(1,Long_C_L_U_NT):(Long_C_L_U_NT,0),(2,Long_C_L_U_NT):('?'+Long_C_L_U_NT,0),
         (3,Long_C_L_U_NT):('?-'+Long_C_L_U_NT,0),
         },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Append "#" to end of input',
        'postprocess_dets':'Run through 34',
        'notes': [''],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
    },  
 34:
    {
        'name': 'Yawelmani palatal and labial suffixal harmony',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',},
        'alphabet': ['-','i','u','e','o','a',Long_F_H_U_T,Long_F_M_U_T,Long_B_H_R_T,Long_B_M_R_T,Long_C_L_U_NT],
        'transitions':
        {(0,'?'):('?',0),(1,'?'):('?',1),(2,'?'):('?',2), (3,'?'):('?',3),
         (4,'?'):('?',4),(5,'?'):('?',5),(6,'?'):('?',6), (7,'?'):('?',7),
         (8,'?'):('?',8),(9,'?'):('?',9),(10,'?'):('?',10), (11,'?'):('?',11),
         (0,'-'):('-',6),(1,'-'):('-',6),(2,'-'):('-',8),(3,'-'):('-',9),
         (4,'-'):('-',10),(5,'-'):('-',11),(6,'-'):('-',6),(7,'-'):('-',7),
         (8,'-'):('-',8),(9,'-'):('-',9),(10,'-'):('-',10),(11,'-'):('-',11),
         (0,'i'):('i',1),(0,Long_F_H_U_T):(Long_F_H_U_T,1),
         (1,'i'):('i',1),(1,Long_F_H_U_T):(Long_F_H_U_T,1),
         (2,'i'):('i',1),(2,Long_F_H_U_T):(Long_F_H_U_T,1),
         (3,'i'):('i',1),(3,Long_F_H_U_T):(Long_F_H_U_T,1),
         (4,'i'):('i',1),(4,Long_F_H_U_T):(Long_F_H_U_T,1),
         (5,'i'):('i',1),(5,Long_F_H_U_T):(Long_F_H_U_T,1),
         (0,'u'):('u',2),(0,Long_B_H_R_T):(Long_B_H_R_T,2),
         (1,'u'):('u',2),(1,Long_B_H_R_T):(Long_B_H_R_T,2),
         (2,'u'):('u',2),(2,Long_B_H_R_T):(Long_B_H_R_T,2),
         (3,'u'):('u',2),(3,Long_B_H_R_T):(Long_B_H_R_T,2),
         (4,'u'):('u',2),(4,Long_B_H_R_T):(Long_B_H_R_T,2),
         (5,'u'):('u',2),(5,Long_B_H_R_T):(Long_B_H_R_T,2),
         (0,'e'):('e',3),(0,Long_F_M_U_T):(Long_F_M_U_T,3),
         (1,'e'):('e',3),(1,Long_F_M_U_T):(Long_F_M_U_T,3),
         (2,'e'):('e',3),(2,Long_F_M_U_T):(Long_F_M_U_T,3),
         (3,'e'):('e',3),(3,Long_F_M_U_T):(Long_F_M_U_T,3),
         (4,'e'):('e',3),(4,Long_F_M_U_T):(Long_F_M_U_T,3),
         (5,'e'):('e',3),(5,Long_F_M_U_T):(Long_F_M_U_T,3),
         (0,'o'):('o',4),(0,Long_B_M_R_T):(Long_B_M_R_T,4),
         (1,'o'):('o',4),(1,Long_B_M_R_T):(Long_B_M_R_T,4),
         (2,'o'):('o',4),(2,Long_B_M_R_T):(Long_B_M_R_T,4),
         (3,'o'):('o',4),(3,Long_B_M_R_T):(Long_B_M_R_T,4),
         (4,'o'):('o',4),(4,Long_B_M_R_T):(Long_B_M_R_T,4),
         (5,'o'):('o',4),(5,Long_B_M_R_T):(Long_B_M_R_T,4),
         (0,'a'):('a',5),(0,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         (1,'a'):('a',5),(1,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         (2,'a'):('a',5),(2,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         (3,'a'):('a',5),(3,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         (4,'a'):('a',5),(4,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         (5,'a'):('a',5),(5,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         
         (6,'u'):('i',6),(6,Long_B_H_R_T):(Long_F_H_U_T,6),
         (6,'i'):('i',6),(6,Long_F_H_U_T):(Long_F_H_U_T,6),
         (6,'e'):('e',7),(6,Long_F_M_U_T):(Long_F_M_U_T,7),
         (6,'o'):('o',7),(6,Long_B_M_R_T):(Long_B_M_R_T,7),
         (6,'a'):('a',7),(6,Long_C_L_U_NT):(Long_C_L_U_NT,7),
         (7,'i'):('i',7),(7,Long_F_H_U_T):(Long_F_H_U_T,7),
         (7,'u'):('u',7),(7,Long_B_H_R_T):(Long_B_H_R_T,7),
         (7,'e'):('e',7),(7,Long_F_M_U_T):(Long_F_M_U_T,7),
         (7,'o'):('o',7),(7,Long_B_M_R_T):(Long_B_M_R_T,7),
         (7,'a'):('a',7),(7,Long_C_L_U_NT):(Long_C_L_U_NT,7),
         (8,'u'):('u',8),(8,Long_B_H_R_T):(Long_B_H_R_T,8),
         (8,'i'):('u',8),(8,Long_F_H_U_T):(Long_B_H_R_T,8),
         (8,'e'):('e',7),(8,Long_F_M_U_T):(Long_F_M_U_T,7),
         (8,'o'):('o',7),(8,Long_B_M_R_T):(Long_B_M_R_T,7),
         (8,'a'):('a',7),(8,Long_C_L_U_NT):(Long_C_L_U_NT,7),
         (9,'a'):('e',9),(9,Long_C_L_U_NT):(Long_F_M_U_T,9),
         (9,'e'):('e',9),(9,Long_F_M_U_T):(Long_F_M_U_T,9),
         (9,'o'):('e',9),(9,Long_B_M_R_T):(Long_F_M_U_T,9),
         (9,'i'):('i',7),(9,Long_F_H_U_T):(Long_F_H_U_T,7),
         (9,'u'):('u',7),(9,Long_B_H_R_T):(Long_B_H_R_T,7),
         (10,'o'):('o',10),(10,Long_B_M_R_T):(Long_B_M_R_T,10),
         (10,'e'):('o',10),(10,Long_F_M_U_T):(Long_B_M_R_T,10),
         (10,'a'):('o',10),(10,Long_C_L_U_NT):(Long_B_M_R_T,10),
         (10,'i'):('i',7),(10,Long_F_H_U_T):(Long_F_H_U_T,7),
         (10,'u'):('u',7),(10,Long_B_H_R_T):(Long_B_H_R_T,7),
         (11,'a'):('a',11),(11,Long_C_L_U_NT):(Long_C_L_U_NT,11),
         (11,'e'):('a',11),(11,Long_F_M_U_T):(Long_C_L_U_NT,11),
         (11,'o'):('a',11),(11,Long_B_M_R_T):(Long_C_L_U_NT,11),
         (11,'i'):('i',7),(11,Long_F_H_U_T):(Long_F_H_U_T,7),
         (11,'u'):('u',7),(11,Long_B_H_R_T):(Long_B_H_R_T,7),
         
       },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Run through 34P first and enter the final output from there into here',
        'postprocess_dets':'Input this output into 34B',
        'notes': ['Vowel phoneme inventory is considered to be /i,i:,u,u:,e,e:,o,o:,a,a:/'
                  'Although i: and u: generally do not manifest phonetically, '
                  'except in contexts wherin [iy],[uw] contract in closed syllables'
                  ', I treat them as phonemic in that their particular vowel quality'
                  'is salient, despite eventually lowering to /e:,o:/ generally ',
                  'This incorporates vowel epenthesis, labial/palatal harmony, lowering,'
                  ' and shortening vowel processes in that order using four FSTs',
                  'The epenthetic process involves inserting /i/ after the first consonant'
                  ' in a sequence of 3 consonants (i.e., CCC->CiCC)',
                 'The harmony process involves labial(rounding) and palatal(backness) suffixal'
                  ' harmony in which the trigger is the final vowel of the stem,'
                  ' however the trigger and targets must be of identical height for'
                  ' harmony to occur; a target which differs in height from the last'
                  ' vowel of the stem will actually block this harmony process',
                 'Potential flaw: This FST carries out this harmony process for all'
                  ' suffixes, but it is possible it should only occur for the first'
                  ' suffix after the stem',
                 '/i,u,i:,u:/ and /e,e:,o,o:,a,a:/ are the two height groupings',
                 'The shortening vowel process involves the shortening of long '
                  'vowels before a consonant cluster (i.e., V:CC->VCC)',
                 'The lowering process incorporated is the lowering of'
                  '/u:/ and /i:/ to o: and e:; this FST does so indiscriminately,'
                  ' although in reality there are contexts where this should not occur',
                 'Although the ordering of epenthesis and vowel harmony in the overall derivation'
                  ' is highly tenable, the ordering of the shortening and lowering processes is '
                  'made more equivocally and we encourage criticism',
                 'Sources: 1) Yawelmani: Some Basic Rules- '
                  'https://www.ling.upenn.edu/~gene/courses/530/readings/Kenstowicz1994_yawelmani.pdf '
                  '2) Restricting Multilevel Constraint Evaluation: Opaque Rule Interaction in'
                  ' Yawelmani Vowel Harmony by Cole & Kisseberth',
                  'The prefix and suffix demarcators "+" and "-" get removed as these FSTs operate '
                  ', so will be absent from the output',
                  ],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':['Any suffixal vowel that disagrees in height with the ultimate vowel '
                  'of the stem behaves opaquely']
    },
 '34B':
    {
        'name': 'Yawelmani vowel shortening',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',},
        'alphabet': ['-','#','i','u','e','o','a',Long_F_H_U_T,Long_B_H_R_T,Long_F_M_U_T,Long_B_M_R_T,Long_C_L_U_NT],
        'transitions':
        {#what to do word-finally
         (0,'#'):('',11),(1,'#'):(Long_F_H_U_T,11),(2,'#'):(Long_B_H_R_T,11), 
         (3,'#'):(Long_F_M_U_T,11),(4,'#'):(Long_B_M_R_T,11),(5,'#'):(Long_C_L_U_NT,11),
         (6,'#'):(Long_F_H_U_T+'?',11),(7,'#'):(Long_B_H_R_T+'?',11),(8,'#'):(Long_F_M_U_T+'?',11),
         (9,'#'):(Long_B_M_R_T+'?',11),(10,'#'):(Long_C_L_U_NT+'?',11),
         #anything from 11 should be impossible, but is included anyways
         (11,'-'):('',11),(11,'#'):('',11),(11,'i'):('',11), 
         (11,'u'):('',11),(11,'e'):('',11),(11,'o'):('',11),
         (11,'a'):('',11),(11,Long_F_H_U_T):('',11),(11,Long_F_M_U_T):('',11),
         (11,Long_B_H_R_T):('',11),(11,Long_B_M_R_T):('',11),
         (11,Long_C_L_U_NT):('',11),(11,'?'):('',11),
         #'-' is nullified at each state; should be fine because is no longer needed
         (0,'-'):('',0),(1,'-'):('',1),(2,'-'):('',2),(3,'-'):('',3),
         (4,'-'):('',4),(5,'-'):('',5),(6,'-'):('',6),(7,'-'):('',7),
         (8,'-'):('',8),(9,'-'):('',9),(10,'-'):('',10),
         #what ? calls for at each state
         (0,'?'):('?',0),(1,'?'):('',6),(6,'?'):('i??',0), 
         (2,'?'):('',7),(7,'?'):('u??',0),
         (3,'?'):('',8),(8,'?'):('e??',0),
         (4,'?'):('',9),(9,'?'):('o??',0),
         (5,'?'):('',10),(10,'?'):('a??',0),
         #i for each state
         (0,'i'):('i',0),(1,'i'):(Long_F_H_U_T+'i',0),
         (2,'i'):(Long_B_H_R_T+'i',0),(3,'i'):(Long_F_M_U_T+'i',0),
         (4,'i'):(Long_B_M_R_T+'i',0),(5,'i'):(Long_C_L_U_NT+'i',0),
         (6,'i'):(Long_F_H_U_T+'?i',0),(7,'i'):(Long_B_H_R_T+'?i',0),
         (8,'i'):(Long_F_M_U_T+'?i',0),(9,'i'):(Long_B_M_R_T+'?i',0),
         (10,'i'):(Long_C_L_U_NT+'?i',0),
         #u for each state
         (0,'u'):('u',0),(1,'u'):(Long_F_H_U_T+'u',0),
         (2,'u'):(Long_B_H_R_T+'u',0),(3,'u'):(Long_F_M_U_T+'u',0),
         (4,'u'):(Long_B_M_R_T+'u',0),(5,'u'):(Long_C_L_U_NT+'u',0),
         (6,'u'):(Long_F_H_U_T+'?u',0),(7,'u'):(Long_B_H_R_T+'?u',0),
         (8,'u'):(Long_F_M_U_T+'?u',0),(9,'u'):(Long_B_M_R_T+'?u',0),
         (10,'u'):(Long_C_L_U_NT+'?u',0),
         #e for each state
         (0,'e'):('e',0),(1,'e'):(Long_F_H_U_T+'e',0),
         (2,'e'):(Long_B_H_R_T+'e',0),(3,'e'):(Long_F_M_U_T+'e',0),
         (4,'e'):(Long_B_M_R_T+'e',0),(5,'e'):(Long_C_L_U_NT+'e',0),
         (6,'e'):(Long_F_H_U_T+'?e',0),(7,'e'):(Long_B_H_R_T+'?e',0),
         (8,'e'):(Long_F_M_U_T+'?e',0),(9,'e'):(Long_B_M_R_T+'?e',0),
         (10,'e'):(Long_C_L_U_NT+'?e',0),
         #o for each state
         (0,'o'):('o',0),(1,'o'):(Long_F_H_U_T+'o',0),
         (2,'o'):(Long_B_H_R_T+'o',0),(3,'o'):(Long_F_M_U_T+'o',0),
         (4,'o'):(Long_B_M_R_T+'o',0),(5,'o'):(Long_C_L_U_NT+'o',0),
         (6,'o'):(Long_F_H_U_T+'?o',0),(7,'o'):(Long_B_H_R_T+'?o',0),
         (8,'o'):(Long_F_M_U_T+'?o',0),(9,'o'):(Long_B_M_R_T+'?o',0),
         (10,'o'):(Long_C_L_U_NT+'?o',0),
         #a for each state
         (0,'a'):('a',0),(1,'a'):(Long_F_H_U_T+'a',0),
         (2,'a'):(Long_B_H_R_T+'a',0),(3,'a'):(Long_F_M_U_T+'a',0),
         (4,'a'):(Long_B_M_R_T+'a',0),(5,'a'):(Long_C_L_U_NT+'a',0),
         (6,'a'):(Long_F_H_U_T+'?a',0),(7,'a'):(Long_B_H_R_T+'?a',0),
         (8,'a'):(Long_F_M_U_T+'?a',0),(9,'a'):(Long_B_M_R_T+'?a',0),
         (10,'a'):(Long_C_L_U_NT+'?a',0),
         #Long_F_H_U_T for each state
         (0,Long_F_H_U_T):('',1),(1,Long_F_H_U_T):(Long_F_H_U_T,1),
         (2,Long_F_H_U_T):(Long_B_H_R_T,1),(3,Long_F_H_U_T):(Long_F_M_U_T,1),
         (4,Long_F_H_U_T):(Long_B_M_R_T,1),(5,Long_F_H_U_T):(Long_C_L_U_NT,1),
         (6,Long_F_H_U_T):(Long_F_H_U_T+'?',1),(7,Long_F_H_U_T):(Long_B_H_R_T+'?',1),
         (8,Long_F_H_U_T):(Long_F_M_U_T+'?',1),(9,Long_F_H_U_T):(Long_B_M_R_T+'?',1),
         (10,Long_F_H_U_T):(Long_C_L_U_NT+'?',1),
         #Long_B_H_R_T for each state
         (0,Long_B_H_R_T):('',2),(1,Long_B_H_R_T):(Long_F_H_U_T,2),
         (2,Long_B_H_R_T):(Long_B_H_R_T,2),(3,Long_B_H_R_T):(Long_F_M_U_T,2),
         (4,Long_B_H_R_T):(Long_B_M_R_T,2),(5,Long_B_H_R_T):(Long_C_L_U_NT,2),
         (6,Long_B_H_R_T):(Long_F_H_U_T+'?',2),(7,Long_B_H_R_T):(Long_B_H_R_T+'?',2),
         (8,Long_B_H_R_T):(Long_F_M_U_T+'?',2),(9,Long_B_H_R_T):(Long_B_M_R_T+'?',2),
         (10,Long_B_H_R_T):(Long_C_L_U_NT+'?',2),
         #Long_F_M_U_T for each state
         (0,Long_F_M_U_T):('',3),(1,Long_F_M_U_T):(Long_F_H_U_T,3),
         (2,Long_F_M_U_T):(Long_B_H_R_T,3),(3,Long_F_M_U_T):(Long_F_M_U_T,3),
         (4,Long_F_M_U_T):(Long_B_M_R_T,3),(5,Long_F_M_U_T):(Long_C_L_U_NT,3),
         (6,Long_F_M_U_T):(Long_F_H_U_T+'?',3),(7,Long_F_M_U_T):(Long_B_H_R_T+'?',3),
         (8,Long_F_M_U_T):(Long_F_M_U_T+'?',3),(9,Long_F_M_U_T):(Long_B_M_R_T+'?',3),
         (10,Long_F_M_U_T):(Long_C_L_U_NT+'?',3),
         #Long_B_M_R_T for each state
         (0,Long_B_M_R_T):('',4),(1,Long_B_M_R_T):(Long_F_H_U_T,4),
         (2,Long_B_M_R_T):(Long_B_H_R_T,4),(3,Long_B_M_R_T):(Long_F_M_U_T,4),
         (4,Long_B_M_R_T):(Long_B_M_R_T,4),(5,Long_B_M_R_T):(Long_C_L_U_NT,4),
         (6,Long_B_M_R_T):(Long_F_H_U_T+'?',4),(7,Long_B_M_R_T):(Long_B_H_R_T+'?',4),
         (8,Long_B_M_R_T):(Long_F_M_U_T+'?',4),(9,Long_B_M_R_T):(Long_B_M_R_T+'?',4),
         (10,Long_B_M_R_T):(Long_C_L_U_NT+'?',4),
         #Long_C_L_U_NT for each state
         (0,Long_C_L_U_NT):('',5),(1,Long_C_L_U_NT):(Long_F_H_U_T,5),
         (2,Long_C_L_U_NT):(Long_B_H_R_T,5),(3,Long_C_L_U_NT):(Long_F_M_U_T,5),
         (4,Long_C_L_U_NT):(Long_B_M_R_T,5),(5,Long_C_L_U_NT):(Long_C_L_U_NT,5),
         (6,Long_C_L_U_NT):(Long_F_H_U_T+'?',5),(7,Long_C_L_U_NT):(Long_B_H_R_T+'?',5),
         (8,Long_C_L_U_NT):(Long_F_M_U_T+'?',5),(9,Long_C_L_U_NT):(Long_B_M_R_T+'?',5),
         (10,Long_C_L_U_NT):(Long_C_L_U_NT+'?',5),
       },
        'preprocess_req': True,
        'postprocess_req': True,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Should have already been run through 34P and 34,
        'postprocess_dets':'Enter output from here into 34C',
        'notes': [''],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
    }, 
 '34C':
    {
        'name': 'Yawelmani vowel lowering',
        'states': {0:'',},
        'alphabet': [Long_F_H_U_T,Long_F_M_U_T,Long_B_H_R_T,Long_B_M_R_T],
        'transitions':
        {(0,'?'):('?',0),(0,Long_B_M_R_T):(Long_B_M_R_T,0),(0,Long_F_M_U_T):(Long_F_M_U_T,0),
         (0,Long_F_H_U_T):(Long_F_M_U_T,0),(0,Long_B_H_R_T):(Long_B_M_R_T,0),
       },
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'hyphenate_suffix': False,
        'preprocess_dets':'Should have already been run through 34P,34,34B; output from here will be final output to user',
        'postprocess_dets':None,
        'notes': [''],
        'harmony_feature':['Palatal','Labial'],
        'sc':True,
        'dr':False,
        'transparent':None,
        'opaque':None
    },   
 35:
    {
        'name': 'Claro complete harmony/assimilation on unstressed final /a/',
        'states': {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',
                   10:'',11:'',12:'',13:'',14:'',15:'',16:'',},
        'alphabet': ['i','e',F_M_U_NT,B_M_R_NT,'o','u','a',"'",'#',],
        'transitions':
           {#any character after # is nullified because should be impossible
            (16,'i'):('',16),(16,'e'):('',16),(16,F_M_U_NT):('',16),
            (16,B_M_R_NT):('',16),(16,'o'):('',16),(16,'u'):('',16),
            (16,'a'):('',16),(16,"'"):('',16),(16,'#'):('',16),
            (16,'?'):('',16),
            #? for each state
            (0,'?'):('?',0),(1,'?'):('?',0),(2,'?'):('?',2),
            (3,'?'):('?',3),(4,'?'):('?',4),(5,'?'):('?',5),
            (6,'?'):('?',6),(7,'?'):('?',7),(8,'?'):('?',8),
            (9,'?'):('a?',0),(10,'?'):('a?',0),(11,'?'):('a?',0),
            (12,'?'):('a?',0),(13,'?'):('a?',0),(14,'?'):('a?',0),
            (15,'?'):('a?',0),
            # ' for each state
            (0,"'"):("'",1),(1,"'"):("'",1),(2,"'"):("'",1),
            (3,"'"):("'",1),(4,"'"):("'",1),(5,"'"):("'",1),
            (6,"'"):("'",1),(7,"'"):("'",1),(8,"'"):("'",1),
            (9,"'"):("a'",1),(10,"'"):("a'",1),(11,"'"):("a'",1),
            (12,"'"):("a'",1),(13,"'"):("a'",1),(14,"'"):("a'",1),
            (15,"'"):("a'",1),
            # a for each state
            (0,'a'):('a',0),(1,'a'):('a',8),(2,'a'):('',9),
            (3,'a'):('',10),(4,'a'):('',11),(5,'a'):('',12),
            (6,'a'):('',13),(7,'a'):('',14),(8,'a'):('',15),
            (9,'a'):('aa',0),(10,'a'):('aa',0),(11,'a'):('aa',0),
            (12,'a'):('aa',0),(13,'a'):('aa',0),(14,'a'):('aa',0),
            (15,'a'):('aa',0),
            # '#' for each state
            (0,'#'):('',16),
            },
        'preprocess_req': True,
        'postprocess_req': False,
        'left_subseq': True,
        'bidir_subseq':False,
        'plus_prefix':True,
        'hyphenate_suffix': True,
        'preprocess_dets':'Append "#" to end of input before entering into FST',
        'postprocess_dets':'',
        'notes':
            ['USER MUST INDICATE STRESSED VOWELS BY INCLUDING AN APOSTROPHE "'" '
             'BEFORE EACH STRESSED VOWEL IN THE INPUT',
             'Swiss Italian dialect (northern Italo-Romance)',
             'Vowel inventory: /i,e,F_M_U_NT,B_M_R_NT,o,u,a/',
            'Trigger= stressed penultimate vowel',
            'Target= unstressed word-final /a/',
            'Is arguably assimilation - not harmony',
            'Identity/complete harmony in which word-final unstressed /a/ '
             'adopts the vowel quality of the penultimate stressed vowel',
            "Ex: /l'ima/->/l'imi/",
            ],
        'harmony_feature':['Complete'],
        'sc':False,
        'dr':False,
        'transparent':None,
        'opaque':None,
        },                                                                 
 }
