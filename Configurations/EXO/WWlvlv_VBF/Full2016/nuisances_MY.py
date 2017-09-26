
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################


#########################################################
import os.path
import copy

massesAndModelsFile = "massesAndModels.py"

regions0j = ['hww2l2v_13TeV_top_of0j',             
             'hww2l2v_13TeV_dytt_of0j',             
             'hwwhm_13TeV_of_0j',
             ]

regions1j = ['hww2l2v_13TeV_top_of1j',             
             'hww2l2v_13TeV_dytt_of1j',             
             'hwwhm_13TeV_of_1j',
             ]

regions2j = ['hww2l2v_13TeV_top_of2j',             
             'hww2l2v_13TeV_dytt_of2j',
             'hwwhm_13TeV_of_2j',
             ]

regions2j_VBF = ['hww2l2v_13TeV_top_of2j_VBF',
                 'hww2l2v_13TeV_dytt_of2j_VBF',
                 'hwwhm_13TeV_of_2j_VBF',
                 ]

regions0j_of = [ item for item in regions0j if "of" in item]
regions1j_of = [ item for item in regions1j if "of" in item]
regions2j_of = [ item for item in regions2j if "of" in item]
regions2j_VBF_of = [ item for item in regions2j_VBF if "of" in item]

regions0j_sf = [ item for item in regions0j if "of" not in item]
regions1j_sf = [ item for item in regions1j if "of" not in item]
regions2j_sf = [ item for item in regions2j if "of" not in item]
regions2j_VBF_sf = [ item for item in regions2j_VBF if "of" not in item]


massesAndModelsFile = "massesAndModels.py"
if os.path.exists(massesAndModelsFile) :
  handle = open(massesAndModelsFile,'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file ", massesAndModelsFile, " does not exist."



Top_pTrw   = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topLHEpt) * TMath::Exp(0.0615-0.0005*antitopLHEpt) ) )'
Top_pTrwUp = '1.'
Top_pTrwDo = '1./(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topLHEpt) * TMath::Exp(0.0615-0.0005*antitopLHEpt) ) )'

nuisances['TopPtRew']  = {
                'name'  : 'TopPtRew',   # Theory uncertainty
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'top'  : [Top_pTrwUp+"/"+Top_pTrw,
                               Top_pTrwDo+"/"+Top_pTrw]
                }

}


weightMetDY ='((0.306383+0.0270402*metPfType1)*(njet==0)'
weightMetDY+='+(0.304908+0.023131 *metPfType1)*(njet==1)'
weightMetDY+='+(0.503422+0.0153159*metPfType1)*(njet>=2 && (mjj < 500 || detajj<3.5))'
weightMetDY+='+(0.524127+0.0318181*metPfType1)*(njet>=2 && (mjj > 500 && detajj>3.5)))'

# up variation is p0+error + (p1-error) * met
weightMetDYUp ='((0.306383+0.0585451+(0.0270402-0.0021439) *metPfType1)*(njet==0)'
weightMetDYUp+='+(0.304908+0.0324019+(0.023131-0.00112073) *metPfType1)*(njet==1)'
weightMetDYUp+='+(0.503422+0.0327627+(0.0153159-0.00105088)*metPfType1)*(njet>=2 && (mjj < 500 || detajj<3.5))'
weightMetDYUp+='+(0.524127+0.209824+(0.0318181-0.00636618) *metPfType1)*(njet>=2 && (mjj > 500 && detajj>3.5)))'

# down variation is p0-error + (p1+error) * met
weightMetDYDo ='((0.306383-0.0585451+(0.0270402+0.0021439) *metPfType1)*(njet==0)'
weightMetDYDo+='+(0.304908-0.0324019+(0.023131+0.00112073) *metPfType1)*(njet==1)'
weightMetDYDo+='+(0.503422-0.0327627+(0.0153159+0.00105088)*metPfType1)*(njet>=2 && (mjj < 500 || detajj<3.5))'
weightMetDYDo+='+(0.524127-0.209824+(0.0318181+0.00636618) *metPfType1)*(njet>=2 && (mjj > 500 && detajj>3.5)))'



################################## theory uncertainties ##############################################

nuisances['QCDscale_VW']  = {
               'name'  : 'QCDscale_VW', 
               'samples'  : {
                   'VW' : '1.03',
                   },
               'type'  : 'lnN'
              }


from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

#CTRL!!!!

#Mancano le QCDscale_hm ......................vedi L 227

####################QCD scale uncertainties for Higgs signals other than ggH, ci servono?

nuisances['QCDscale_ggH']  = {
               'name'  : 'QCDscale_ggH', 
               'samples'  : {
                   #'ggH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.0','scale','sm'), ----> already included in jet bin migration QCD uncertainty?
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.0','scale','sm'),
                   'H_htt'   : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }


nuisances['QCDscale_qqH']  = {
               'name'  : 'QCDscale_qqH', 
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','scale','sm'),
                   #'qqH_hww_750_NWA' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','750','scale','bsm'),
                   },
               'type'  : 'lnN',
              }

#?  per  ggH no?
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['QCDscale_qqH']['samples'].update({'qqH_hww_'+m+'_'+model_name:HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH',m,'scale','bsm')})
   


nuisances['QCDscale_WH']  = {
               'name'  : 'QCDscale_WH', 
               'samples'  : {
                   'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }



nuisances['QCDscale_ZH']  = {
               'name'  : 'QCDscale_ZH', 
               'samples'  : {
                   'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.0','scale','sm'),
                   },
               'type'  : 'lnN',
              }



nuisances['QCDscale_ggZH']  = {
               'name'  : 'QCDscale_ggZH', 
               'samples'  : {
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','scale','sm'),                  
                   },
               'type'  : 'lnN',
              }

########################################################


#Ok!
nuisances['QCDscale_qqbar_accept']  = {
               'name'  : 'QCDscale_qqbar_accept', 
               'type'  : 'lnN',
               'samples'  : {
                   #'qqH_hww' : '1.02',
                   #'qqH_htt' : '1.02',
                   #'WH_hww'  : '1.02',
                   #'ZH_hww'  : '1.02',
                   #
                   #'WW'      : '1.015', -> not included since part of weights from WWqscale0j and WWqscale1j
                   'qqH_hww' : '1.007',
                   'qqH_htt' : '1.007',
                   'WH_hww'  : '1.05',
                   'ZH_hww'  : '1.04',
                   'VZ'      : '1.029',
                   'qqH_hww_750_NWA' : '1.02'
                   },
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['QCDscale_qqbar_accept']['samples'].update({'qqH_hww_'+m+'_'+model_name:'1.02'})


#Ok!
nuisances['QCDscale_gg_accept']  = {
               'name'  : 'QCDscale_gg_accept', 
               'samples'  : {
                   #'ggWW'    : '1.03',
                   #'ggH_hww' : '1.03',
                   #'ggH_htt' : '1.03',
                   #'H_htt'   : '1.03',
                   #'ggZH_hww': '1.03',                   
                   #
                   'ggWW'    : '1.027',
                   'ggH_hww' : '1.027',
                   'ggH_htt' : '1.027',
                   'H_htt'   : '1.027',
                   'ggZH_hww': '1.027',                   
                   'ggH_hww_750_NWA' : '1.027',
                   },
               'type'  : 'lnN',
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['QCDscale_gg_accept']['samples'].update({'ggH_hww_'+m+'_'+model_name:'1.027'})
    nuisances['QCDscale_gg_accept']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:'1.027'})




####QCD scale
#Tutti 1???

nuisances['QCDscale']  = {
                'name'  : 'QCDscale',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww' : ['1.', 
                                '1.'],
                },                
                'cuts'  : [
                          'hwwhm_13TeV_of_0j',
                          'hwwhm_13TeV_of_1j',
                          'hwwhm_13TeV_of_2j',
                          'hwwhm_13TeV_of_2j_VBF',
                         

                         ],

}                                       

nuisances['QCDscale1in']  = {
                'name'  : 'QCDscale1in',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww' : ['1.',
                                '1.'],
                },
                'cuts'  : [
                          'hwwhm_13TeV_of_0j',
                          'hwwhm_13TeV_of_1j',
                          'hwwhm_13TeV_of_2j',
                          'hwwhm_13TeV_of_2j_VBF',
                         
                         ],

}

nuisances['QCDscale2in']  = {
                'name'  : 'QCDscale2in',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww' : ['1.',
                                '1.'],
                },
                'cuts'  : [
                          'hwwhm_13TeV_of_0j',
                          'hwwhm_13TeV_of_1j',
                          'hwwhm_13TeV_of_2j',
                          'hwwhm_13TeV_of_2j_VBF',
                         
                         ],

}

nuisances['QCDscale3in']  = {
                'name'  : 'QCDscale3in',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'ggH_hww' : ['1.',
                                '1.'],
                },
                'cuts'  : [
                          'hwwhm_13TeV_of_0j',
                          'hwwhm_13TeV_of_1j',
                          'hwwhm_13TeV_of_2j',
                          'hwwhm_13TeV_of_2j_VBF',

                         ],

}



############################ pdf uncertainty ################ ok!

nuisances['pdf_gg']  = {
               'name'  : 'pdf_gg', 
               'samples'  : {
                   #'ggWW'    : '1.05',    # --> no, since absorbed into k-scale factor
                   'ggH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'H_htt'   : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,'125.0','pdf','sm'),
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','pdf','sm'),                   
                   'ggH_hww_750_NWA' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','750','pdf','bsm'),
                   },
               'type'  : 'lnN',
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['pdf_gg']['samples'].update({'ggH_hww_'+m+'_'+model_name: HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,m,'pdf','bsm')})
    nuisances['pdf_gg']['samples'].update({'ggH_hww_INT'+m+'_'+model_name: HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggH' ,m,'pdf','bsm')})


nuisances['pdf_qqbar']  = {
               'name'  : 'pdf_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'qqH_hww_750_NWA' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','750','pdf','bsm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH','125.0','pdf','sm'),
                   'WH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','WH' ,'125.0','pdf','sm'),
                   'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH' ,'125.0','pdf','sm'),
                   'VZ'      : '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
                   },
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['pdf_qqbar']['samples'].update({'qqH_hww_'+m+'_'+model_name:HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','vbfH',m,'pdf','bsm')})
             

nuisances['pdf_gg_accept']  = {
               'name'  : 'pdf_gg_accept', 
               'samples'  : {
                   'ggWW'    : '1.005',    
                   'ggH_hww' : '1.005',
                   'ggH_htt' : '1.005',
                   'H_htt'   : '1.005',
                   'ggZH_hww': '1.005', 
                   'ggH_hww_750_NWA' :  '1.005',
                   },
               'type'  : 'lnN',
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['pdf_gg_accept']['samples'].update({'ggH_hww_'+m+'_'+model_name:'1.005'})
    nuisances['pdf_gg_accept']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:'1.005'})


nuisances['pdf_qqbar_accept']  = {
               'name'  : 'pdf_qqbar_accept', 
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'qqH_hww' : '1.011',
                   'qqH_hww_750_NWA' : '1.011',
                   'qqH_htt' : '1.011',
                   'WH_hww'  : '1.007',
                   'ZH_hww'  : '1.012',
                   'VZ'      : '1.005',                   
                   },
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['pdf_qqbar_accept']['samples'].update({'qqH_hww_'+m+'_'+model_name:'1.011'})




####################################### ok!

# ggww and interference

nuisances['kfactggww']  = {
               'name'  : 'kfactggww', 
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW' : '1.15',
                   },
              }


#nuisances['kfactggwwInt']  = {
               #'name'  : 'kfactggwwInt', 
               #'type'  : 'lnN',
               #'samples'  : {
                   #'ggWW_Int' : '1.25',
                   #},
              #}

#  - WW shaping
nuisances['WWresum0j']  = {
                'name'  : 'WWresum0j',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
               'cuts'  : regions0j 
                
                }


nuisances['WWresum1j']  = {
                'name'  : 'WWresum1j',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
               'cuts'  : regions1j 
                }

nuisances['WWresum2j']  = {
                'name'  : 'WWresum2j',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
               'cuts'  : regions2j + regions2j_VBF
                }

nuisances['WWqscale0j']  = {
                'name'  : 'WWqscale0j',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : regions0j 
                }


nuisances['WWqscale1j']  = {
                'name'  : 'WWqscale1j',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : regions1j
                }

nuisances['WWqscale2j']  = {
                'name'  : 'WWqscale2j',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : regions2j + regions2j_VBF 
                }




###############################################

#CTRL!!!!!
# PS/UE
# PS

#nuisances['PS']  = {
#                'name'  : 'PS', 
#                'kind'  : 'tree',
#                'type'  : 'shape',
#                'samples'  : {
#                   'WW' :  ['1./1.03295', '1.'],  # latino_WWTo2L2NuHerwigPS.root moved with different name in __PS folder
#                },
# 
##                'folderUp'   : 'root://eosuser.cern.ch//eos/user/r/rodrigo/HWW2016/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel__PS',
##                'folderDown' : 'root://eosuser.cern.ch//eos/user/r/rodrigo/HWW2016/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel__PS' 
#                }
# 

nuisances['UE']  = {
                'name'  : 'UE', 
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW' :  ['1/0.978817', '1/1.0192'], 
                },
                }

####################################


nuisances['WgStarScale']  = {
               'name'  : 'WgStarScale', 
               'type'  : 'lnN',
               'samples'  : {
                   'WgS' : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   'VgS' : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   },
                }
 

nuisances['DYttnorm0j']  = {
               'name'  : 'ICHEP_DYttnorm0j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions0j_of
              }

nuisances['DYttnorm1j']  = {
               'name'  : 'ICHEP_DYttnorm1j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions1j_of 
              }

nuisances['DYttnorm2j']  = {
               'name'  : 'ICHEP_DYttnorm2j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j_of 
              }

nuisances['DYttnorm2jVBF']  = {
               'name'  : 'ICHEP_DYttnorm2jVBF',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j_VBF_of 
              }

nuisances['DYnorm0j']  = {
               'name'  : 'ICHEP_DYnorm0j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions0j_sf 
              }

nuisances['DYnorm1j']  = {
               'name'  : 'ICHEP_DYnorm1j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions1j_sf 
              }

nuisances['DYnorm2j']  = {
               'name'  : 'ICHEP_DYnorm2j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j_sf 
              }

nuisances['DYnorm2jVBF']  = {
               'name'  : 'ICHEP_DYnorm2jVBF',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j_VBF_sf 
              }

nuisances['WWnorm0j']  = {
               'name'  : 'ICHEP_WWnorm0j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions0j 
              }

nuisances['WWnorm1j']  = {
               'name'  : 'ICHEP_WWnorm1j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions1j 
              }

nuisances['WWnorm2j']  = {
               'name'  : 'ICHEP_WWnorm2j',
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j 
              }

nuisances['WWnorm2jVBF']  = {
               'name'  : 'ICHEP_WWnorm2jVBF',
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j_VBF 
              }

nuisances['Topnorm0j']  = {
               'name'  : 'ICHEP_Topnorm0j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  :  regions0j
              }

nuisances['Topnorm1j']  = {
               'name'  : 'ICHEP_Topnorm1j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions1j 
              }

nuisances['Topnorm2j']  = {
               'name'  : 'ICHEP_Topnorm2j',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j 
              }

nuisances['Topnorm2jVBF']  = {
               'name'  : 'ICHEP_Topnorm2jVBF',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : regions2j_VBF
              }






nuisances['tttwTh']  = {
                'name'  : 'tttwTh',   # Theory uncertainty
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {  # up              down
                   'top'     : ['((dataset==15 || dataset==16) * 1.0816 + (dataset==17 || dataset==18 || dataset==19))',
                                '((dataset==15 || dataset==16) * 0.9184 + (dataset==17 || dataset==18 || dataset==19))'],
                }
                # tt = 17/18/19 depending on the sample/generator
                # tW = 15/16
                
}
  
nuisances['TopPS']  = {
                'name'  : 'TopPS',   # Theory uncertainty
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'top'  : ['(1+0.000067*mTi*0.5)','1/(1+0.000067*mTi*0.5)']
                }

} 



###############################################################################
#### Luminosity
nuisances['lumi']  = {
               'name'  : 'lumi_13TeV',
               'samples'  : {
                   'DY'       : '1.023',    
                   'top'      : '1.023',    
                   'WW'       : '1.023',    
                   'ggWW'     : '1.023',
                   'Vg'       : '1.023',
                   'VgS'      : '1.023',
                   'VZ'       : '1.023',
                   'VVV'      : '1.023',
                   'ggH_hww'  : '1.023',
                   'qqH_hww'  : '1.023',
                   'ZH_hww'   : '1.023',
                   'ggZH_hww' : '1.023',
                   'WH_hww'   : '1.023',
                   'bbH_hww'  : '1.023',
                   'H_htt'    : '1.023',
                   },
               'type'  : 'lnN',
              }




############################ FAKES ###################################################################################### ok!

if Nlep == '2' :
  # already divided by central values in formulas !
  fakeW_EleUp       = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp'
  fakeW_EleDown     = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown'
  fakeW_MuUp        = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp'
  fakeW_MuDown      = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown'
  fakeW_statEleUp   = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp'
  fakeW_statEleDown = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown'
  fakeW_statMuUp    = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp'
  fakeW_statMuDown  = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown'

else:
  fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'

nuisances['fake_syst']  = {
               'name'  : 'fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
}

nuisances['fake_ele']  = {
                'name'  : 'fake_ele_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'fake_ele_stat_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statEleUp , fakeW_statEleDown ]
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'fake_mu_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'fake_mu_stat_hww',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_statMuUp , fakeW_statMuDown ]
                             },
}


####################### B-tagger ################################################################ OK,ma CTRL!

nuisances['btagbc']  = {
                'name'  : 'Full2016_btag_bc',
                'kind'  : 'weight',
               'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WW'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggWW'    : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VVV'     : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VZ'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'top'     : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'Vg'      : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'VgS'     : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ggH_hww' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'qqH_hww' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'WH_hww'  : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'ZH_hww'  : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'H_htt'   : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                   'bbH_hww' : ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')'],
                }
}

#CTRL
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['btagbc']['samples'].update({'ggH_hww_'+m+'_'+model_name: ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')']})
    nuisances['btagbc']['samples'].update({'qqH_hww_'+m+'_'+model_name: ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')']}) 
    nuisances['btagbc']['samples'].update({'ggH_hww_INT'+m+'_'+model_name: ['('+bSF+'_bc_up)/('+bSF+')', '('+bSF+'_bc_down)/('+bSF+')']}) 

#OLD
#for m in masses:
#  for model in models:
#    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
#    nuisances['btagbc']['samples'].update({'ggH_hww_'+m+'_'+model_name:['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)']})
#    nuisances['btagbc']['samples'].update({'qqH_hww_'+m+'_'+model_name:['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)']}) 
#    nuisances['btagbc']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)']}) 




nuisances['btagudsg']  = {
                'name'  : 'Full2016_btag_udsg',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VVV'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VZ'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WW'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggWW'    : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'top'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'Vg'      : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'VgS'     : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ggH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'qqH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'WH_hww'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'ZH_hww'  : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'bbH_hww' : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                   'H_htt'   : ['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')'],
                }
}


#CTRL
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['btagudsg']['samples'].update({'ggH_hww_'+m+'_'+model_name:['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')']})
    nuisances['btagudsg']['samples'].update({'qqH_hww_'+m+'_'+model_name:['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')']}) 
    nuisances['btagudsg']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['('+bSF+'_udsg_up)/('+bSF+')', '('+bSF+'_udsg_down)/('+bSF+')']}) 


# OLD
#for m in masses:
#  for model in models:
#    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
#    nuisances['btagudsg']['samples'].update({'ggH_hww_'+m+'_'+model_name:['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)']})
#    nuisances['btagudsg']['samples'].update({'qqH_hww_'+m+'_'+model_name:['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)']}) 
#    nuisances['btagudsg']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)']}) 



############################ Trigger Efficiency ###########OK!!

if   Nlep == '2' : trig_syst = ['(effTrigW_Up)/(effTrigW)', '(effTrigW_Down)/(effTrigW)']
elif Nlep == '3' : trig_syst = ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)']
# !!!!! We don't have the trigger formula implemented for 4l !!!! -> Use 3l but not correct
elif Nlep == '4' : trig_syst = ['(effTrigW3l_Up)/(effTrigW3l)', '(effTrigW3l_Down)/(effTrigW3l)']

nuisances['trigg']  = {
                'name'  : 'trigger',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : trig_syst ,
                   'VVV'     : trig_syst ,
                   'VZ'      : trig_syst ,
                   'ggWW'    : trig_syst ,
                   'WW'      : trig_syst ,
                   'top'     : trig_syst ,
                   'Vg'      : trig_syst ,
                   'VgS'     : trig_syst ,
                   'ggH_hww' : trig_syst ,
                   'qqH_hww' : trig_syst ,
                   'WH_hww'  : trig_syst ,
                   'ZH_hww'  : trig_syst ,
                   'ggZH_hww': trig_syst ,
                   'bbH_hww' : trig_syst ,
                   'H_htt'   : trig_syst ,
                },
}


for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['trigg']['samples'].update({'ggH_hww_'+m+'_'+model_name: trig_syst })
    nuisances['trigg']['samples'].update({'qqH_hww_'+m+'_'+model_name:  trig_syst})
    nuisances['trigg']['samples'].update({'ggH_hww_INT'+m+'_'+model_name: trig_syst})



################### Electron Efficiency and energy scale ##########ok!

id_syst_ele = [ 'LepSF'+Nlep+'l__ele_'+eleWP+'__Up' , 'LepSF'+Nlep+'l__ele_'+eleWP+'__Do' ]

nuisances['idiso_ele']  = {
                'name'  : 'idiso_ele',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_ele ,
                   'VVV'     : id_syst_ele ,
                   'VZ'      : id_syst_ele ,
                   'ggWW'    : id_syst_ele ,
                   'WW'      : id_syst_ele ,
                   'top'     : id_syst_ele ,
                   'Vg'      : id_syst_ele ,
                   'VgS'     : id_syst_ele ,
                   'ggH_hww' : id_syst_ele ,
                   'qqH_hww' : id_syst_ele ,
                   'WH_hww'  : id_syst_ele ,
                   'ZH_hww'  : id_syst_ele ,
                   'ggZH_hww': id_syst_ele ,
                   'bbH_hww' : id_syst_ele ,
                   'H_htt'   : id_syst_ele ,
                },
}

for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['idiso_ele']['samples'].update({'ggH_hww_'+m+'_'+model_name: id_syst_ele })
    nuisances['idiso_ele']['samples'].update({'qqH_hww_'+m+'_'+model_name: id_syst_ele })
    nuisances['idiso_ele']['samples'].update({'ggH_hww_INT'+m+'_'+model_name: id_syst_ele })



nuisances['electronpt']  = {
                'name'  : 'scale_e',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY' :  ['1', '1'],
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  :  ['1', '1'],
                   'ZH_hww'  :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                 },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepElepTup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepElepTdo'+skim,
}



for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['electronpt']['samples'].update({'ggH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['electronpt']['samples'].update({'qqH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['electronpt']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['1', '1']})                



############# Muon Efficiency and energy scale  ####### ok!

id_syst_mu = [ 'LepSF'+Nlep+'l__mu_'+muWP+'__Up' , 'LepSF'+Nlep+'l__mu_'+muWP+'__Do' ]

nuisances['idiso_mu']  = {
                'name'  : 'idiso_mu',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_mu ,
                   'VVV'     : id_syst_mu ,
                   'VZ'      : id_syst_mu ,
                   'ggWW'    : id_syst_mu ,
                   'WW'      : id_syst_mu ,
                   'top'     : id_syst_mu ,
                   'Vg'      : id_syst_mu ,
                   'VgS'     : id_syst_mu ,
                   'ggH_hww' : id_syst_mu ,
                   'qqH_hww' : id_syst_mu ,
                   'WH_hww'  : id_syst_mu ,
                   'ZH_hww'  : id_syst_mu ,
                   'ggZH_hww': id_syst_mu ,
                   'bbH_hww' : id_syst_mu ,
                   'H_htt'   : id_syst_mu ,
                },
}



for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['idiso_mu']['samples'].update({'ggH_hww_'+m+'_'+model_name: id_syst_mu })
    nuisances['idiso_mu']['samples'].update({'qqH_hww_'+m+'_'+model_name: id_syst_mu })
    nuisances['idiso_mu']['samples'].update({'ggH_hww_INT'+m+'_'+model_name: id_syst_mu })


nuisances['muonpt']  = {
                'name'  : 'scale_m',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepMupTup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__LepMupTdo'+skim,
}



for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['muonpt']['samples'].update({'ggH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['muonpt']['samples'].update({'qqH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['muonpt']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['1', '1']})



##### Jet energy scale

nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESdo'+skim,
}


for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['jes']['samples'].update({'ggH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['jes']['samples'].update({'qqH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['jes']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['1', '1']})



##### MET energy scale########## ok!

nuisances['met']  = {
                'name'  : 'scale_met',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__METup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__METdo'+skim,
}


for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['met']['samples'].update({'ggH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['met']['samples'].update({'qqH_hww_'+m+'_'+model_name:['1', '1']})
    nuisances['met']['samples'].update({'ggH_hww_INT'+m+'_'+model_name:['1', '1']})








#CTRL cosa sono....
# statistical fluctuation
# on MC/data
# "stat" is a special word to identify this nuisance
nuisances['stat']  = {
                # apply to the following samples: name of samples here must match keys in samples.py
               'samples'  : {
                   
                   'ttbar': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'singletop': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
                    
                   'top': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
                    
                   'DY': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
                    
                   'ggWW': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
                    
                   'ggWW_Int': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
                    
                   'WW': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'VZ': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'WZ': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'VVV': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'H_hww': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'ggH_hww': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'qqH_hww': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'WH_hww': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'ZH_hww': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'H_htt': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'ggH_htt': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'qqH_htt': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'WH_htt': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'ZH_htt': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'ggZH_hww': {
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
                   
                   'Fake': {  # needed? da rimettere
                         'typeStat' : 'bbb',
                         },
                   
                   'Vg': {  
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },

                   'VgS':{  
                         'typeStat' : 'bbb',
                         'zeroMCError' : '0',
                         },
#                   'ggH_hww_750_NWA' : {
#                         'typeStat' : 'bbb',
#                         },
#                   'qqH_hww_750_NWA' : {
#                         'typeStat' : 'bbb',
#                         },
                 },
               'type'  : 'shape'
              }
for m in masses:
  for model in models:
    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
    nuisances['stat']['samples'].update({'ggH_hww_'+m+'_'+model_name:{'typeStat' : 'bbb'}})
    nuisances['stat']['samples'].update({'qqH_hww_'+m+'_'+model_name:{'typeStat' : 'bbb'}})

if os.path.exists("STUnc.py") :
  handle = open("STUnc.py",'r')
  exec(handle)
  handle.close()
else:
  print "!!! ERROR file STUnc.py does not exist."



#####################################

# 
#def findClosestMass(m):
#  mindistance=99999
#  for mass in STUnc.keys():
#    if abs(float(mass) - float(m)) < mindistance:
#      thekey=mass
#      mindistance = abs(float(mass) - float(m))
#  
#  return STUnc[thekey]
# 
#for m in masses:
#  unc=findClosestMass(m)
#  for model in models:
#    model_name = model.replace("cprime","c").replace(".","").replace("BRnew","brn")
#    unc0jet=str(unc["QCDscale"]["0jet"])
#    unc1jet=str(unc["QCDscale"]["1jet"])
#    unc2jet=str(unc["QCDscale"]["2jet"])
#    unc3jet=str(unc["QCDscale"]["VBF"])
#    nuisances['QCDscale']['samples'].update({'ggH_hww_'+m+'_'+model_name:[
#         "("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30 ) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30)*(mjj>500 && detajj>3.5))",
#         "(1./("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30 ) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30)*(mjj>500 && detajj>3.5)))"
#                                                                         ]
#                                            })
#    
# 
#    unc0jet=str(unc["QCDscale1in"]["0jet"])
#    unc1jet=str(unc["QCDscale1in"]["1jet"])
#    unc2jet=str(unc["QCDscale1in"]["2jet"])
#    unc3jet=str(unc["QCDscale1in"]["VBF"])
#    nuisances['QCDscale1in']['samples'].update({'ggH_hww_'+m+'_'+model_name:[
#         "("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30 )*(mjj>500 && detajj>3.5))",
#         "(1./("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30 )*(mjj>500 && detajj>3.5)))"
#                                                                         ]
#                                            })
#    
#    unc0jet=str(unc["QCDscale2in"]["0jet"])
#    unc1jet=str(unc["QCDscale2in"]["1jet"])
#    unc2jet=str(unc["QCDscale2in"]["2jet"])
#    unc3jet=str(unc["QCDscale2in"]["VBF"])
#    nuisances['QCDscale2in']['samples'].update({'ggH_hww_'+m+'_'+model_name:[
#         "("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30 )*(mjj>500 && detajj>3.5))",
#         "(1./("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30 )*(mjj>500 && detajj>3.5)))"
#                                                                         ]
#                                            })
# 
#    unc0jet=str(unc["QCDscale3in"]["0jet"])
#    unc1jet=str(unc["QCDscale3in"]["1jet"])
#    unc2jet=str(unc["QCDscale3in"]["2jet"])
#    unc3jet=str(unc["QCDscale3in"]["VBF"])
#    nuisances['QCDscale3in']['samples'].update({'ggH_hww_'+m+'_'+model_name:[
#         "("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30 )*(mjj>500 && detajj>3.5))",
#         "(1./("+unc0jet+"*(std_vector_jet_pt[0] < 30)+"+unc1jet+"*(std_vector_jet_pt[0] > 30 && std_vector_jet_pt[1] < 30)+"+unc2jet+"*((std_vector_jet_pt[1]> 30) && (mjj<500 || detajj<3.5))+"+unc3jet+"*(std_vector_jet_pt[1]> 30 )*(mjj>500 && detajj>3.5)))"
#                                                                         ]
#                                            })
