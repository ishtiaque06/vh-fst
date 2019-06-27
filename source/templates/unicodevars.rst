Variables for Unicode Characters
================================

This project makes use of IPA characters represented as variables. These variables
can be loaded by importing the :code:`unicode_variable_repr` module. They are also loaded
in whenever the :code:`app.py` command-line tool is run. This is useful since whenever
the command-line tool is ready to take a word input, the letters in the word can be
formatted using this convention.

The variable details are below.

Key
+++

| Consonants are represented in the following manner:
| :code:`<Place>_<Manner>_<Voicing>`
| For example, :code:`R_P_VL` represents ʈ, the Retroflex Plosive VoiceLess consonant.

The shorthands are described as follows:

* Place:
      * L=labial,
      * LD=labiodental,
      * D=dental,
      * A=alveolar,
      * R=retroflex,
      * PA=postalveolar,
      * P=palatal,
      * V=velar,
      * U=uvular,
      * PH=pharyngeal,
      * G=glottal

* Manner:
      * P=plosive,
      * N=nasal,
      * TR=trill,
      * TF=tap/flap,
      * F=fricative,
      * LF=lateral fricative,
      * A=approximant,
      * LA=lateral approximant

* Voicing:
      * VL=voiceless,
      * V=voiced

Vowels are represented in a similar manner, with the shorthands as below:

* front/back:
      * F=+front,-back,
      * B=-front,+back,
      * C=-front,-back

* high/low:
      * H=+high,-low,
      * M=-high,-low,
      * L=-high,+low

* rounding:
      * R=rounded,
      * U=unrounded

* tense:
      * T=+tense,
      * NT=lax


For long vowels, you can just add :code:`Long_` in front of the vowel's representation.
For example, F_M_R_T = ø, the Front Mid Rounded Tense vowel. If you want to
make this vowel long, the variable name would be :code:`Long_F_M_R_T = øː`

All the actual variables are listed below:

Variables
+++++++++

Consonants:

.. code-block::

  R_P_VL = ʈ
  R_P_V = ɖ
  P_P_V = ɟ
  G_P_VL = ʔ
  LD_N_V = ɱ
  R_N_V = ɳ
  P_N_V = ɲ
  V_N_V = ŋ
  A_TF_V = ɾ
  R_TF_V = ɽ
  L_F_VL = ɸ
  L_F_V = β
  D_F_VL = θ
  D_F_V = ð
  R_F_VL = ʂ
  R_F_V = ʐ
  P_F_VL = ç
  P_F_V = ʝ
  V_F_V = ɣ
  U_F_VL = χ
  U_F_V = ʁ
  PH_F_VL = ħ
  PH_F_V = ʕ
  G_F_V = ɦ
  A_LF_VL = ɬ
  A_LF_V = ɮ
  PA_LF_VL = ʃ
  PA_LF_V = ʒ
  LD_A_V = ʋ
  A_A_V = ɹ
  R_A_V = ɻ
  V_A_V = ɰ
  R_LA_V = ɭ
  P_LA_V = ʎ

Vowels:

.. code-block::

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
  F_L_U_T: æ
  C_L_R_T: ɐ
  C_L_R_NT: ɶ
  B_L_U_NT: ɑ
  B_L_R_NT: ɒ
  Long_F_H_U_T: iː
  Long_F_H_R_T: yː
  Long_B_H_R_T: uː
  Long_F_M_U_T: eː
  Long_F_M_R_T: øː
  Long_B_M_R_T: oː
  Long_C_L_U_NT: aː
