# cuts


#supercut = 'mll>12  \
#            && Lepton_pt[0]>25 && Lepton_pt[1]>20 \
#            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
#            && PuppiMET_pt > 30 \
#            && abs(Lepton_eta[0] - Lepton_eta[1])<2.0 \
#            '

supercut = 'mll>12  \
            && Lepton_pt[0]>25 && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && bVeto \
            && PuppiMET_pt > 30 \
            && mlljj20_whss > 50. \
            && abs(Lepton_eta[0] - Lepton_eta[1])<2.0 \
            '

cuts['testout1'] = 'WlepPt_whssv1>0 && WlepPt_whssv1<=40'
cuts['testout2'] = 'WlepPt_whssv1>40 && WlepPt_whssv1<=80'
cuts['testout3'] = 'uu[0]'
cuts['testout4'] = 'oneJet'
cuts['testout5'] = 'uu[0] && oneJet'
cuts['testout6'] = 'uu[0] && oneJet && WlepPt_whssv1>20'
 
'''
cuts['presel'] = {
    'expr': 'sr',
    'categories': {
        'presel1' : '1==1',
        'presel111': '1==1',
        'presel11': 'WlepPt_whssv1>40',
        'presel12': 'pTWW>40',
        'presel2' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*11)',
        'presel3' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*11) && oneJet',
        'presel4' : 'WlepPt_whssv1>40',
        'presel5' : 'ee[0]',
        'presel6' : 'ee[0] && WlepPt_whssv1<=30',
    }
}
'''

'''
cuts['whwwSS_13TeV'] = {
    'expr': 'sr',
    #Define the sub categorization of sr
    'categories': {
        #ee
        'ee_ptw0_75'         : 'ee[0] && WlepPt_whss<=75',
        'ee_ptw75_150'       : 'ee[0] && WlepPt_whss>75 && WlepPt_whss<=150',
        'ee_of0j_ptw150_250' : 'ee[0] && zeroJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'ee_of1j_ptw150_250' : 'ee[0] && oneJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'ee_ptw250'          : 'ee[0] && WlepPt_whss>400',
        #uu
        'uu_ptw0_75'         : 'uu[0] && WlepPt_whss<=75',
        'uu_ptw75_150'       : 'uu[0] && WlepPt_whss>75 && WlepPt_whss<=150',
        'uu_of0j_ptw150_250' : 'uu[0] && zeroJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'uu_of1j_ptw150_250' : 'uu[0] && oneJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'uu_ptw250'          : 'uu[0] && WlepPt_whss>400',
        #eu
        'eu_ptw0_75'         : 'eu[0] && WlepPt_whss<=75',
        'eu_ptw75_150'       : 'eu[0] && WlepPt_whss>75 && WlepPt_whss<=150',
        'eu_of0j_ptw150_250' : 'eu[0] && zeroJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'eu_of1j_ptw150_250' : 'eu[0] && oneJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'eu_ptw250'          : 'eu[0] && WlepPt_whss>400',
    }
}
'''

'''
cuts['whwwSS_13TeV'] = {
    'expr': 'sr',
    #Define the sub categorization of sr
    'categories': {
        #uu
        #bin 0-jet
        'ee_of0j_ptw0_75'    : 'ee[0] && zeroJet && WlepPt_whss<=75',
        'ee_of0j_ptw75_150'  : 'ee[0] && zeroJet && WlepPt_whss>75 && WlepPt_whss<=150',
        'ee_of0j_ptw150_250' : 'ee[0] && zeroJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'ee_of0j_ptw250_400' : 'ee[0] && zeroJet && WlepPt_whss>250 && WlepPt_whss<=400',
        'ee_of0j_ptwGT400'   : 'ee[0] && zeroJet && WlepPt_whss>400',
        #bin 1-jet
        'ee_of1j_ptw0_75'    : 'ee[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss<=75',
        'ee_of1j_ptw75_150'  : 'ee[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>75 && WlepPt_whss<=150',
        'ee_of1j_ptw150_250' : 'ee[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>150 && WlepPt_whss<=250',
        'ee_of1j_ptw250_400' : 'ee[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>250 && WlepPt_whss<=400',
        'ee_of1j_ptwGT400'   : 'ee[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>400',
        #bin >=2-jet
        'ee_of0j_ptw0_75'    : 'ee[0] && twoJetOrMore && WlepPt_whss<=75',
        'ee_of0j_ptw75_150'  : 'ee[0] && twoJetOrMore && WlepPt_whss>75 && WlepPt_whss<=150',
        'ee_of0j_ptw150_250' : 'ee[0] && twoJetOrMore && WlepPt_whss>150 && WlepPt_whss<=250',
        'ee_of0j_ptw250_400' : 'ee[0] && twoJetOrMore && WlepPt_whss>250 && WlepPt_whss<=400',
        'ee_of0j_ptwGT400'   : 'ee[0] && twoJetOrMore && WlepPt_whss>400',

        #uu
        #bin 0-jet
        'uu_of0j_ptw0_75'    : 'uu[0] && zeroJet && WlepPt_whss<=75',
        'uu_of0j_ptw75_150'  : 'uu[0] && zeroJet && WlepPt_whss>75 && WlepPt_whss<=150',
        'uu_of0j_ptw150_250' : 'uu[0] && zeroJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'uu_of0j_ptw250_400' : 'uu[0] && zeroJet && WlepPt_whss>250 && WlepPt_whss<=400',
        'uu_of0j_ptwGT400'   : 'uu[0] && zeroJet && WlepPt_whss>400',
        #bin 1-jet
        'uu_of1j_ptw0_75'    : 'uu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss<=75',
        'uu_of1j_ptw75_150'  : 'uu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>75 && WlepPt_whss<=150',
        'uu_of1j_ptw150_250' : 'uu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>150 && WlepPt_whss<=250',
        'uu_of1j_ptw250_400' : 'uu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>250 && WlepPt_whss<=400',
        'uu_of1j_ptwGT400'   : 'uu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>400',
        #bin >=2-jet
        'uu_of0j_ptw0_75'    : 'uu[0] && twoJetOrMore && WlepPt_whss<=75',
        'uu_of0j_ptw75_150'  : 'uu[0] && twoJetOrMore && WlepPt_whss>75 && WlepPt_whss<=150',
        'uu_of0j_ptw150_250' : 'uu[0] && twoJetOrMore && WlepPt_whss>150 && WlepPt_whss<=250',
        'uu_of0j_ptw250_400' : 'uu[0] && twoJetOrMore && WlepPt_whss>250 && WlepPt_whss<=400',
        'uu_of0j_ptwGT400'   : 'uu[0] && twoJetOrMore && WlepPt_whss>400',
        
        #eu
        #bin 0-jet
        'eu_of0j_ptw0_75'    : 'eu[0] && zeroJet && WlepPt_whss<=75',
        'eu_of0j_ptw75_150'  : 'eu[0] && zeroJet && WlepPt_whss>75 && WlepPt_whss<=150',
        'eu_of0j_ptw150_250' : 'eu[0] && zeroJet && WlepPt_whss>150 && WlepPt_whss<=250',
        'eu_of0j_ptw250_400' : 'eu[0] && zeroJet && WlepPt_whss>250 && WlepPt_whss<=400',
        'eu_of0j_ptwGT400'   : 'eu[0] && zeroJet && WlepPt_whss>400',
        #bin 1-jet
        'eu_of1j_ptw0_75'    : 'eu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss<=75',
        'eu_of1j_ptw75_150'  : 'eu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>75 && WlepPt_whss<=150',
        'eu_of1j_ptw150_250' : 'eu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>150 && WlepPt_whss<=250',
        'eu_of1j_ptw250_400' : 'eu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>250 && WlepPt_whss<=400',
        'eu_of1j_ptwGT400'   : 'eu[0] && oneJet && Alt$(CleanJet_pt[1], 0) < 30. && WlepPt_whss>400',
        #bin >=2-jet
        'eu_of0j_ptw0_75'    : 'eu[0] && twoJetOrMore && WlepPt_whss<=75',
        'eu_of0j_ptw75_150'  : 'eu[0] && twoJetOrMore && WlepPt_whss>75 && WlepPt_whss<=150',
        'eu_of0j_ptw150_250' : 'eu[0] && twoJetOrMore && WlepPt_whss>150 && WlepPt_whss<=250',
        'eu_of0j_ptw250_400' : 'eu[0] && twoJetOrMore && WlepPt_whss>250 && WlepPt_whss<=400',
        'eu_of0j_ptwGT400'   : 'eu[0] && twoJetOrMore && WlepPt_whss>400',
    }
}
'''
