# Outputs string representation of a unicode hex representation
def uc(hex):
    return chr(int(hex))


'''CONSONANTS. Format: Place_Manner_Voicing;

    Place:
        L=labial, LD=labiodental, D=dental, A=alveolar, R=retroflex,
        PA=postalveolar, P=palatal, V=velar, U=uvular, PH=pharyngeal, G=glottal;

    Manner:
        P=plosive, N=nasal, TR=trill, TF=tap/flap, F=fricative,
        LF=lateral fricative, A=approximant, LA=lateral approximant;

    Voicing:
        VL=voiceless, V=voiced
'''
R_P_VL=uc(0x0288)
R_P_V=uc(0x0256)
P_P_V=uc(0x025)
G_P_VL=uc(0x0294)
LD_N_V=uc(0x0271)
R_N_V=uc(0x0273)
P_N_V=uc(0x0272)
V_N_V=uc(0x014B)
A_TF_V=uc(0x027E)
R_TF_V=uc(0x027D)
L_F_VL=uc(0x0278)
L_F_V=uc(0x03B2)
D_F_VL=uc(0x03B8)
D_F_V=uc(0x00F0)
R_F_VL=uc(0x0282)
R_F_V=uc(0x0290)
P_F_VL=uc(0x00E7)
P_F_V=uc(0x029D)
V_F_V=uc(0x0263)
U_F_VL=uc(0x03C7)
U_F_V=uc(0x0281)
PH_F_VL=uc(0x0127)
PH_F_V=uc(0x0295)
G_F_V=uc(0x0266)
A_LF_VL=uc(0x026C)
A_LF_V=uc(0x026E)
PA_LF_VL=uc(0x0283)
PA_LF_V=uc(0x0292)
LD_A_V=uc(0x028B)
A_A_V=uc(0x0279)
R_A_V=uc(0x027B)
V_A_V=uc(0x0270)
R_LA_V=uc(0x026D)
P_LA_V=uc(0x028E)

# To print in help menu
cons_as_dict = {
    'R_P_VL':R_P_VL,
    'R_P_V': R_P_V,
    'P_P_V': P_P_V,
    'G_P_VL': G_P_VL,
    'LD_N_V': LD_N_V,
    'R_N_V': R_N_V,
    'P_N_V': P_N_V,
    'V_N_V': V_N_V,
    'A_TF_V': A_TF_V,
    'R_TF_V': R_TF_V,
    'L_F_VL': L_F_VL,
    'L_F_V': L_F_V,
    'D_F_VL': D_F_VL,
    'D_F_V': D_F_V,
    'R_F_VL': R_F_VL,
    'R_F_V': R_F_V,
    'P_F_VL': P_F_VL,
    'P_F_V': P_F_V,
    'V_F_V': V_F_V,
    'U_F_VL': U_F_VL,
    'U_F_V': U_F_V,
    'PH_F_VL': PH_F_VL,
    'PH_F_V': PH_F_V,
    'G_F_V': G_F_V,
    'A_LF_VL': A_LF_VL,
    'A_LF_V': A_LF_V,
    'PA_LF_VL': PA_LF_VL,
    'PA_LF_V': PA_LF_V,
    'LD_A_V': LD_A_V,
    'A_A_V': A_A_V,
    'R_A_V': R_A_V,
    'V_A_V': V_A_V,
    'R_LA_V': R_LA_V,
    'P_LA_V': P_LA_V,
}


'''VOWELS. front/back_high/low_rounding_tense;

    front/back: F=+front,-back, B=-front,+back, C=-front,-back;

    high/low: H=+high,-low, M=-high,-low, L=-high,+low;

    rounding: R=rounded, U=unrounded;

    tense: T=+tense, NT=lax
'''
C_H_U_T=uc(0x0268)
C_H_R_T=uc(0x0289)
B_H_U_T=uc(0x026F)
B_H_R_NT=uc(0x028A)
F_M_R_T=uc(0x00F8)
C_M_U_T=uc(0x0258)
C_M_R_T=uc(0x0275)
B_M_U_T=uc(0x0264)
schwa=uc(0x0259)
F_M_U_NT=uc(0x025B)
F_M_R_NT=uc(0x0153)
C_M_U_NT=uc(0x025C)
C_M_R_NT=uc(0x025E)
B_M_U_NT=uc(0x028C)
B_M_R_NT=uc(0x0254)
F_L_UR_T=uc(0x00E6)
C_L_R_T=uc(0x0250)
C_L_R_NT=uc(0x0276)
B_L_U_NT=uc(0x0251)
B_L_R_NT=uc(0x0252)

# To print in help menu
vowels_as_dict = {
    'C_H_U_T': C_H_U_T,
    'C_H_R_T': C_H_R_T,
    'B_H_U_T': B_H_U_T,
    'B_H_R_NT': B_H_R_NT,
    'F_M_R_T': F_M_R_T,
    'C_M_U_T': C_M_U_T,
    'C_M_R_T': C_M_R_T,
    'B_M_U_T': B_M_U_T,
    'schwa': schwa,
    'F_M_U_NT': F_M_U_NT,
    'F_M_R_NT': F_M_R_NT,
    'C_M_U_NT': C_M_U_NT,
    'C_M_R_NT': C_M_R_NT,
    'B_M_U_NT': B_M_U_NT,
    'B_M_R_NT': B_M_R_NT,
    'F_L_UR_T': F_L_UR_T,
    'C_L_R_T': C_L_R_T,
    'C_L_R_NT': C_L_R_NT,
    'B_L_U_NT': B_L_U_NT,
    'B_L_R_NT': B_L_R_NT
}
