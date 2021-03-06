import os
import copy
import inspect

#XSWeight*SFweight*METFilter_MC*btagSF[0]
#XSWeight*SFweight*METFilter_MC*PromptGenLepMatch1l
#Match check:
#XSWeight => v
#METFilter_MC => v
#SFweight => changed

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals
signal_file = '2HDMa_signal.py'
if os.path.exists(signal_file) :
    handle = open(signal_file,'r')
    exec(handle)
    handle.close()
else:
    raise IOError('FILE NOT FOUND: '+signal_file+'does not exist.')


mc = [skey for skey in samples if skey not in ('FAKE', 'DATA')]
new_mc = []
for mp in signal:
    new_mc.append(mp)
new_mc += ['WW', 'WZqcd', 'VBF-V', 'ZZ', 'missing_top'] #WWewk
old_mc = [sample for sample in mc if sample not in new_mc]

#new_samples = new_mc + ['FAKE'] 
new_samples = new_mc 
old_samples = [skey for skey in samples if skey not in new_samples]

eleWP    = 'mvaFall17V1Iso_WP90'
muWP     = 'cut_Tight_HWWW'

LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0] > 0.5 \
            || Lepton_isTightMuon_'+muWP+'[0] > 0.5)'

Lep1WPCut='(Alt$(Lepton_isTightElectron_'+eleWP+'[1], 0) > 0.5 \
            || Alt$(Lepton_isTightMuon_'+muWP+'[1], 0) > 0.5)'

aliases['LepWPCut'] = {
    'expr': LepWPCut
}

aliases['Lep1WPCut'] = {
    'expr': Lep1WPCut
}
aliases['nTightLep'] = {
    'expr': '(Sum$(Lepton_isTightElectron_'+eleWP+') + Sum$(Lepton_isTightMuon_'+muWP+'))',
}
aliases['1tlVeto'] = {
    'expr': '(nTightLep[0] == 1)', 
}


###### PromptGenMatch ######

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch1l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0], 0)',
    'samples': mc
}

###### SFweight ######

aliases['LepSF1l__ele_wp__mu_wp'] = {
    'expr': 'Lepton_tightElectron_'+eleWP+'_IdIsoSF[0]*Lepton_tightMuon_'+muWP+'_IdIsoSF[0]',
    'samples': mc
}

# data/MC scale factors
aliases['SFweight1l'] = {
    'expr': ' * '.join(['puWeight', 'TriggerEffWeight_1l', 'Lepton_RecoSF[0]', 'EMTFbug_veto']),
    'samples': mc
}
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight1l[0]', 'LepSF1l__ele_wp__mu_wp[0]', 'PrefireWeight']),
    'samples': mc
}
# # variations of tight lepton WP
aliases['SFweightEleUp'] = {
    'expr': '((TMath::Abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF_Up[0]/Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (TMath::Abs(Lepton_pdgId[0]) == 13))',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': '((TMath::Abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF_Down[0]/Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (TMath::Abs(Lepton_pdgId[0]) == 13))',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': '((TMath::Abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF_Up[0]/Lepton_tightMuon_'+muWP+'_TotSF[0]) + (TMath::Abs(Lepton_pdgId[0]) == 11))',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': '((TMath::Abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF_Down[0]/Lepton_tightMuon_'+muWP+'_TotSF[0]) + (TMath::Abs(Lepton_pdgId[0]) == 11))',
    'samples': mc
}



aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

aliases['GenLHE'] = {
'expr': '(Sum$(LHEPart_pdgId == 21) == 0)',
'samples': ['qqWWqq', 'WW2J']
}


###### bVeto ######

# Fix no longer needed since Full201Xv6
#aliases['Jet_btagSF_shapeFix'] = {
#    'linesToAdd': [
#        'gSystem->Load("libCondFormatsBTauObjects.so");',
#        'gSystem->Load("libCondToolsBTau.so");',
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#        '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE')
#    ],
#    'class': 'BtagSF',
#    'args': (btagSFSource,),
#    'samples': mc
#}

#bJetV_req = '(CleanJet_pt > 20 && abs(CleanJet_eta) < 2.5)'
#bJetR_req = '(CleanJet_pt > 30 && abs(CleanJet_eta) < 2.5)'

# Exclude W candidates from b tagging check
#bJetV_req = '(CleanJet_pt > 20 && abs(CleanJet_eta) < 2.5 && CleanJet_jetIdx != CleanJet_jetIdx[idx_j1] && CleanJet_jetIdx != CleanJet_jetIdx[idx_j2])'
#bJetR_req = '(CleanJet_pt > 30 && abs(CleanJet_eta) < 2.5 && CleanJet_jetIdx != CleanJet_jetIdx[idx_j1] && CleanJet_jetIdx != CleanJet_jetIdx[idx_j2])'

# Clash fix
aliases['idx_j1'] = {
    'expr': 'HM_idx_j1',
    'samples': new_samples
}
aliases['idx_j2'] = {
    'expr': 'HM_idx_j2',
    'samples': new_samples
}

aliases['ori_idx_j1'] = {
    #'expr': 'Alt$(CleanJet_jetIdx[idx_j1], -9989.)'
    'expr': '(idx_j1>-0.5)*(CleanJet_jetIdx[MaxIf$(idx_j1, idx_j1>0)]) + -9989*(idx_j1<-0.5)'
}
aliases['ori_idx_j2'] = {
    #'expr': 'Alt$(CleanJet_jetIdx[idx_j2], -9989.)'
    'expr': '(idx_j2>-0.5)*(CleanJet_jetIdx[MaxIf$(idx_j2, idx_j2>0)]) + -9989*(idx_j2<-0.5)'
}

aliases['Jet_btagSF_shape'] = {
    'expr': 'Jet_btagSF_deepcsv_shape',
    'samples': new_mc
}
for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
    aliases['Jet_btagSF_shape_up_'+shift] = {
        'expr': 'Jet_btagSF_deepcsv_shape_up_'+shift,
        'samples': new_mc
    }
    aliases['Jet_btagSF_shape_down_'+shift] = {
        'expr': 'Jet_btagSF_deepcsv_shape_down_'+shift,
        'samples': new_mc
    }

bJetV_req = '(CleanJet_pt > 20 && abs(CleanJet_eta) < 2.5 && CleanJet_jetIdx != ori_idx_j1[0] && CleanJet_jetIdx != ori_idx_j2[0])'
bJetR_req = '(CleanJet_pt > 30 && abs(CleanJet_eta) < 2.5 && CleanJet_jetIdx != ori_idx_j1[0] && CleanJet_jetIdx != ori_idx_j2[0])'

aliases['bVeto'] = {
    'expr': 'Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522 && '+bJetV_req+' ) == 0',
}

aliases['bReq'] = {
    'expr': 'Sum$(Jet_btagDeepB[CleanJet_jetIdx] > 0.1522 && '+bJetR_req+' ) >= 1',
}
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log('+bJetV_req+'*Jet_btagSF_shape[CleanJet_jetIdx]+1*(!'+bJetV_req+'))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log('+bJetR_req+'*Jet_btagSF_shape[CleanJet_jetIdx]+1*(!'+bJetR_req+'))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVetoSF[0]*bVeto[0] + bReqSF[0]*bReq[0])',
    'samples': mc
}

for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
    for targ in ['bVeto', 'bReq']:
        #alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        #alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
        # alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_up_%s' % shift)
        aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        aliases['%sSF%sup' % (targ, shift)]['expr'] = aliases['%sSF%sup' % (targ, shift)]['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

        #alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        #alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
        # alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_down_%s' % shift)
        aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        aliases['%sSF%sdown' % (targ, shift)]['expr'] = aliases['%sSF%sdown' % (targ, shift)]['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': '(bVetoSF{shift}up[0]*bVeto[0] + bReqSF{shift}up[0]*bReq[0])'.format(shift = shift),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': '(bVetoSF{shift}down[0]*bVeto[0] + bReqSF{shift}down[0]*bReq[0])'.format(shift = shift),
        'samples': mc
    }


# FIXME top stuff
# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && (GenPart_statusFlags & %d)) == 2' % lastcopy,
    'samples': ['top', 'missing_top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && (GenPart_statusFlags & %d)) == 1' % lastcopy,
    'samples': ['top', 'missing_top']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && (GenPart_statusFlags & %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top', 'missing_top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && (GenPart_statusFlags & %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top', 'missing_top']
}

TF_a = '-2.02274e-01'
TF_b = '1.09734e-04'
TF_c = '-1.30088e-07'
TF_d = '5.83494e+01'
TF_e = '1.96252e+02'

aliases['Top_pTrw'] = {
    # top pt re-weighting: https://indico.cern.ch/event/904971/contributions/3857701/attachments/2036949/3410728/TopPt_20.05.12.pdf
    'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt(TMath::Exp('+TF_a+' + '+TF_b+'*topGenPtOTF + '+TF_c+'*topGenPtOTF*topGenPtOTF + '+TF_d+'/(topGenPtOTF+'+TF_e+')) * TMath::Exp('+TF_a+' + '+TF_b+'*antitopGenPtOTF + '+TF_c+'*antitopGenPtOTF*antitopGenPtOTF + '+TF_d+'/(antitopGenPtOTF+'+TF_e+')))) + (topGenPtOTF * antitopGenPtOTF <= 0.)',
    #'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt(TMath::Exp(-2.02274e-01 + 1.09734e-04*topGenPtOTF - 1.30088e-07*topGenPtOTF*topGenPtOTF + 5.83494e+01/(topGenPtOTF+1.96252e+02)) * TMath::Exp(-2.02274e-01 + 1.09734e-04*antitopGenPtOTF - 1.30088e-07*antitopGenPtOTF*antitopGenPtOTF + 5.83494e+01/(antitopGenPtOTF+1.96252e+02)))) + (topGenPtOTF * antitopGenPtOTF <= 0.)',
    'samples': ['top', 'missing_top']
}



# PU jet Id SF
puidSFSource = '{}/src/PlotsConfigurations/Configurations/patches/PUID_81XTraining_EffSFandUncties.root'.format(os.getenv('CMSSW_BASE'))

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/patches/pujetidsf_event_new.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'PUJetIdEventSFnew',
    'args': (puidSFSource, '2017', 'loose'),
    'samples': mc
}
#puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')
#
#aliases['PUJetIdSF'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        '.L %s/src/PlotsConfigurations/Configurations/patches/pujetidsf_event.cc+' % os.getenv('CMSSW_BASE')
#    ],
#    'class': 'PUJetIdEventSF',
#    'args': (puidSFSource, '2017', 'loose'),
#    'samples': mc
#}

# WJets Xsec fix
aliases['WJets_0J_xsFix'] = {
    'expr': '49264.92/Xsec', # 49264.92/54611.6   0.90209625793
    'samples': ['WJetsToLNu-0J']
}
aliases['WJets_1J_xsFix'] = {
    'expr': '8280.36/Xsec',  # 8280.36/8966.2     0.92350828667
    'samples': ['WJetsToLNu-1J']
}
aliases['WJets_2J_xsFix'] = {
    'expr': '3118.08/Xsec',  #3118.08/3643.12     0.85588177166
    'samples': ['WJetsToLNu-2J']
}

aliases['EWKnloW'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/monoHWW/SemiLep/Full2017_v6/2HDMa/EWKnloW.cc' % os.getenv('CMSSW_BASE')
    ],
    'class': 'EWKnloW',
    'samples': "Wjets"
}

# adapted to full OTF fake
for mu_et in [20]:
    for el_et in [25, 35, 45]:
        corr_file = "%s/src/PlotsConfigurations/Configurations/monoHWW/SemiLep/Full2017_v6/2HDMa/fakeweight_correction.root" % os.getenv('CMSSW_BASE')
        el_fr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/EleFR_jet"+str(el_et)+".root"
        mu_fr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/MuonFR_jet"+str(mu_et)+".root"
        el_pr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/ElePR.root"
        mu_pr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/MuonPR.root"

        aliases['FW_mu'+str(mu_et)+'_el'+str(el_et)] = {
            'class': 'FakeWeightOTF',
            'args': (corr_file, eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file)), 
            'linesToAdd' : [
                'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                '.L %s/src/PlotsConfigurations/Configurations/monoHWW/SemiLep/Full2017_v6/2HDMa/fakeweight_OTF.cc+' % os.getenv('CMSSW_BASE')
             ],
            'samples': ["FAKE"]
        }

for mu_et in [10, 30]:
    for el_et in [35]:
        corr_file = "%s/src/PlotsConfigurations/Configurations/monoHWW/SemiLep/Full2017_v6/2HDMa/fakeweight_correction.root" % os.getenv('CMSSW_BASE')
        el_fr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/EleFR_jet"+str(el_et)+".root"
        mu_fr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/MuonFR_jet"+str(mu_et)+".root"
        el_pr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/ElePR.root"
        mu_pr_file = os.getenv('CMSSW_BASE') + "/src/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1IsoWP90/MuonPR.root"

        aliases['FW_mu'+str(mu_et)+'_el'+str(el_et)] = {
            'class': 'FakeWeightOTF',
            'args': (corr_file, eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file)), 
            'linesToAdd' : [
                'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                '.L %s/src/PlotsConfigurations/Configurations/monoHWW/SemiLep/Full2017_v6/2HDMa/fakeweight_OTF.cc+' % os.getenv('CMSSW_BASE')
             ],
            'samples': ["FAKE"]
        }

for mu_et in [20]:
    aliases['FW_mu'+str(mu_et)+'_EleUp'] = {
        'expr': '((TMath::Abs(Lepton_pdgId[0]) == 11)*(FW_mu'+str(mu_et)+'_el45[0]/FW_mu'+str(mu_et)+'_el35[0]) + (TMath::Abs(Lepton_pdgId[0]) == 13))',
        'samples': ["FAKE"]
    }
    aliases['FW_mu'+str(mu_et)+'_EleDown'] = {
        'expr': '((TMath::Abs(Lepton_pdgId[0]) == 11)*(FW_mu'+str(mu_et)+'_el25[0]/FW_mu'+str(mu_et)+'_el35[0]) + (TMath::Abs(Lepton_pdgId[0]) == 13))',
        'samples': ["FAKE"]
    }
    
    aliases['FW_mu'+str(mu_et)+'_MuUp'] = {
        'expr': '((TMath::Abs(Lepton_pdgId[0]) == 13)*(FW_mu'+str(mu_et+10)+'_el35[0]/FW_mu'+str(mu_et)+'_el35[0]) + (TMath::Abs(Lepton_pdgId[0]) == 11))',
        'samples': ["FAKE"]
    }
    aliases['FW_mu'+str(mu_et)+'_MuDown'] = {
        'expr': '((TMath::Abs(Lepton_pdgId[0]) == 13)*(FW_mu'+str(mu_et-10)+'_el35[0]/FW_mu'+str(mu_et)+'_el35[0]) + (TMath::Abs(Lepton_pdgId[0]) == 11))',
        'samples': ["FAKE"]
    }

aliases['FWglobalSF'] = {
    'expr': '((TMath::Abs(Lepton_pdgId[0]) == 13)*3.61 + (TMath::Abs(Lepton_pdgId[0]) == 11)*2.06)',
    'samples': ["FAKE"]
}

aliases['WptOvHak4M_OTF'] = {
    'expr': 'TMath::Min(MHlnjj_pt_lmet, MHlnjj_pt_jj)/MHlnjj_m_lmetjj'
}

aliases['projMET'] = {
    'expr': 'TMath::Sin(MHlnjj_dphi_lVmet)*PuppiMET_pt*(MHlnjj_dphi_lVmet < 3.141592653/2.) + PuppiMET_pt*(MHlnjj_dphi_lVmet >= 3.141592653/2.)'
}
