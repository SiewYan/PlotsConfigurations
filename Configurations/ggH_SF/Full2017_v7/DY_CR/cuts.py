supercut = '    mll>12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>10 \
            && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13) \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
           '

# DY Control Regions: ee/uu * (0/1/2 jet + VBF + VH)

cuts['0j'] = {
   'expr': 'zeroJet && bVeto' ,
   'categories' : {
       'ee_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak',
       'mm_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak',
       'df_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak',
       'ee_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto',
       'mm_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto',
       'df_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto',
       'tight_ee_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak && dymva_alt_dnn_0j > 0.8',
       'tight_mm_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak && dymva_alt_dnn_0j > 0.8',
       'tight_df_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak && dymva_alt_dnn_0j > 0.8',
       'tight_ee_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto && dymva_alt_dnn_0j > 0.8',
       'tight_mm_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto && dymva_alt_dnn_0j > 0.8',
       'tight_df_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto && dymva_alt_dnn_0j > 0.8',
   }
}

cuts['1j'] = {
   'expr': 'oneJet && bVeto' ,
   'categories' : {
       'ee_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak',
       'mm_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak',
       'df_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak',
       'ee_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto',
       'mm_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto',
       'df_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto',
       'tight_ee_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak && dymva_alt_dnn_1j > 0.8',
       'tight_mm_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak && dymva_alt_dnn_1j > 0.8',
       'tight_df_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak && dymva_alt_dnn_1j > 0.8',
       'tight_ee_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto && dymva_alt_dnn_1j > 0.8',
       'tight_mm_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto && dymva_alt_dnn_1j > 0.8',
       'tight_df_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto && dymva_alt_dnn_1j > 0.8',
   }
}

cuts['2j'] = {
   'expr': '2jggH && bVeto' ,
   'categories' : {
       'ee_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak',
       'mm_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak',
       'df_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak',
       'ee_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto',
       'mm_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto',
       'df_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto',
       'tight_ee_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak && dymva_alt_dnn_2j > 0.8',
       'tight_mm_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak && dymva_alt_dnn_2j > 0.8',
       'tight_df_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak && dymva_alt_dnn_2j > 0.8',
       'tight_ee_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto && dymva_alt_dnn_2j > 0.8',
       'tight_mm_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto && dymva_alt_dnn_2j > 0.8',
       'tight_df_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto && dymva_alt_dnn_2j > 0.8',
   }
}

cuts['VBF'] = {
   'expr': '2jVBF && bVeto' ,
   'categories' : {
       'ee_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak',
       'mm_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak',
       'df_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak',
       'ee_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto',
       'mm_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto',
       'df_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto',
       'tight_ee_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak && dymva_alt_dnn_VBF > 0.8',
       'tight_mm_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak && dymva_alt_dnn_VBF > 0.8',
       'tight_df_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak && dymva_alt_dnn_VBF > 0.8',
       'tight_ee_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto && dymva_alt_dnn_VBF > 0.8',
       'tight_mm_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto && dymva_alt_dnn_VBF > 0.8',
       'tight_df_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto && dymva_alt_dnn_VBF > 0.8',
   }
}

cuts['VH'] = {
   'expr': '2jVH && bVeto' ,
   'categories' : {
       'ee_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak',
       'mm_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak',
       'df_in'         : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak',
       'ee_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto',
       'mm_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto',
       'df_out'        : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto',
       'tight_ee_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Zpeak && dymva_alt_dnn_VH > 0.8',
       'tight_mm_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Zpeak && dymva_alt_dnn_VH > 0.8',
       'tight_df_in'   : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && Zpeak && dymva_alt_dnn_VH > 0.8',
       'tight_ee_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && ZVeto && dymva_alt_dnn_VH > 0.8',
       'tight_mm_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && ZVeto && dymva_alt_dnn_VH > 0.8',
       'tight_df_out'  : '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && ZVeto && dymva_alt_dnn_VH > 0.8',
   }
}
