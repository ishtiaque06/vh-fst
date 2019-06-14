# Vowel Harmony Finite State Transducer

This FST class is designed to be able generate expected pronunciations of
words in a certain set of vowel harmony patterns that exist in natural languages. Many of these languages and their vowel-harmony
patterns are described in Andrew Nevins' book [Locality in Vowel Harmony](https://mitpress.mit.edu/books/locality-vowel-harmony).

This project is the collaborative summer project of Travis Herringshaw and Ahmed Ishtiaque,
under the supervision of Professor Jane Chandlee at Haverford College.

The FST tries to remain as close as possible to the description provided by Nevins
in the languages he describes in his book.

So far, the following vowel-harmony patterns have been recorded:
1. Kisa applicative suffix Vlɑ
2. Kisa reversative suffix Vlɑ
3. Sibe vowel rounding harmony
4. Tuvan backness harmony
5. Uyghur backness harmony
6. Uyghur plural suffix -lVr
7. Uyghur dative suffixʁV
8. Halh (Mongolic) rounding harmony
9. Jingulu nominal root with non-neuter gender suffix
10. Jingulu adjectivial root with non-neuter gender suffix
11. Jingulu verbal root with subject agreement-marking suffix
12. Jingulu verbal root with motion-imperative suffix
13. Jingulu verbal root with negative imperative suffix

### Usage
This repository provides a command-line tool that you can interact with and use the transducers that generate IPA equivalents of words in the above VH patterns.

To run the tool, you need [Python 3](https://www.python.org/) installed on your
computer.

Once you have that installed, you can clone this repository and run the tool
using your favorite python 3 interpreter (IDLE, the python3 command, etc.). For
example, from command line, the commands would look like this:

```bash
  $ git clone https://github.com/ishtiaque06/vh-fst.git
  $ cd vh-fst
  $ python3 app.py
```

This will present you with an interactive command-line tool that you can choose
the VH pattern you want to work with, and then input words to check what the
expected output might be. The command-line tool looks like this:

```bash
$ python3 app.py
Welcome to the Vowel Harmony FST Command-line Interface.
This program lets you choose a vowel harmony pattern from several and
attempts to give you the correct phonetic representation of valid words
in the pattern of your choosing.

These are patterns that this program supports at the moment:
1. Kisa applicative suffix Vlɑ
2. Kisa reversative suffix Vlɑ
3. Sibe vowel rounding harmony
4. Tuvan backness harmony
5. Uyghur backness harmony
6. Uyghur plural suffix -lVr
7. Uyghur dative suffixʁV
8. Halh (Mongolic) rounding harmony
9. Jingulu nominal root with non-neuter gender suffix
10. Jingulu adjectivial root with non-neuter gender suffix
11. Jingulu verbal root with subject agreement-marking suffix
12. Jingulu verbal root with motion-imperative suffix
13. Jingulu verbal root with negative imperative suffix
==============================================================
Vowel Harmony FST Command-line Interface for Phonologists
==============================================================
Select a vowel harmony pattern (Ex: 1)
Enter q to quit, l to list all patterns
>>> _
```

This tool accepts space-delimited strings, possibly with suffixes for providing
 the right output for each word. One cool thing is that if you have access to
 Unicode IPA characters, you can use those to represent your words as well.
 Added to that, the output words are also represented in IPA. To make things
 relatively easier for you, we provide a set of variables you can use to
 represent IPA characters, as provided below:

 ```bash
Consonants. Format: Place_Manner_Voicing;

    Place:
        L=labial, LD=labiodental, D=dental, A=alveolar, R=retroflex,
        PA=postalveolar, P=palatal, V=velar, U=uvular, PH=pharyngeal, G=glottal;

    Manner:
        P=plosive, N=nasal, TR=trill, TF=tap/flap, F=fricative,
        LF=lateral fricative, A=approximant, LA=lateral approximant;

    Voicing:
        VL=voiceless, V=voiced
R_P_VL: ʈ
R_P_V: ɖ
P_P_V: %
G_P_VL: ʔ
LD_N_V: ɱ
R_N_V: ɳ
P_N_V: ɲ
V_N_V: ŋ
A_TF_V: ɾ
R_TF_V: ɽ
L_F_VL: ɸ
L_F_V: β
D_F_VL: θ
D_F_V: ð
R_F_VL: ʂ
R_F_V: ʐ
P_F_VL: ç
P_F_V: ʝ
V_F_V: ɣ
U_F_VL: χ
U_F_V: ʁ
PH_F_VL: ħ
PH_F_V: ʕ
G_F_V: ɦ
A_LF_VL: ɬ
A_LF_V: ɮ
PA_LF_VL: ʃ
PA_LF_V: ʒ
LD_A_V: ʋ
A_A_V: ɹ
R_A_V: ɻ
V_A_V: ɰ
R_LA_V: ɭ
P_LA_V: ʎ

Vowels. Format: front/back_high/low_rounding_tense;

    front/back: F=+front,-back, B=-front,+back, C=-front,-back;

    high/low: H=+high,-low, M=-high,-low, L=-high,+low;

    rounding: R=rounded, U=unrounded;

    tense: T=+tense, NT=lax
C_H_U_T: ɨ
C_H_R_T: ʉ
B_H_U_T: ɯ
B_H_R_NT: ʊ
F_M_R_T: ø
C_M_U_T: ɘ
C_M_R_T: ɵ
B_M_U_T: ɤ
schwa: ə
F_M_U_NT: ɛ
F_M_R_NT: œ
C_M_U_NT: ɜ
C_M_R_NT: ɞ
B_M_U_NT: ʌ
B_M_R_NT: ɔ
F_L_UR_T: æ
C_L_R_T: ɐ
C_L_R_NT: ɶ
B_L_U_NT: ɑ
B_L_R_NT: ɒ
```

For example, if you want to test the word `tsomilɑ`, you can input either of
the following strings to the tool:
  * `t s o m i l ɑ`, i.e. the unicode representation
  * `t s o m i l B_L_U_NT`

where `B_L_U_NT` stands for `ɑ`, the "Back Low Unrounded Not Tense (Lax)" vowel.

### Sources Used
* [Locality in Vowel Harmony by Andrew Nevins](https://mitpress.mit.edu/books/locality-vowel-harmony)
* [Harmony Systems by Sharon Rose and Rachel Walker] (http://idiom.ucsd.edu/~rose/RoseWalkerHarmonysystemsch8.pdf)
* [Disharmony and derived transparency in Uyghur Vowel Harmony by Bert Vaux]  (https://web.archive.org/web/20060208045946/http://www.uwm.edu/~vaux/uyghur.pdf)
* [The Typology of Uyghur Harmony and Consonants by Kelsie Patillo] (https://pdfs.semanticscholar.org/d75f/6ee2d45b03b446cff1c0fbce5c173f026899.pdf)
* [Vowel Harmony in Jingulu by Rob Pensalfini] (http://www.ai.mit.edu/projects/dm/featgeom/pensalfini-harmony.pdf)
* [Turkish Vowel Harmony by B. Kabak] (https://onlinelibrary.wiley.com/doi/full/10.1002/9781444335262.wbctp0118)
* [Variation in Finnish Vowel Harmony: An OT Account by C.O. Ringen and Orvoki Heinamaki] (https://link.springer.com/content/pdf/10.1023%2FA%3A1006158818498.pdf)
