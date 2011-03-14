import FWCore.ParameterSet.Config as cms

#!
#! JET & REFERENCE KINEMATIC CUTS
#!
import JetMETAnalysis.JetAnalyzers.Defaults_cff as Defaults;

Defaults.JetPtEta = cms.PSet(
    etaMin = cms.double(-5.0),
    etaMax = cms.double(5.0),
    ptMin  = cms.double(1.0)
)
Defaults.RefPtEta = cms.PSet(
    etaMin = cms.double(-5.0),
    etaMax = cms.double(5.0),
    ptMin = cms.double(10.0)
)
Defaults.JetResponseParameters.doComposition = True


#!
#! PROCESS
#!
process = cms.Process("JRA")


#!
#! CONDITIONS (DELIVERING JEC BY DEFAULT!)
#!
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "START311_V2::All"


#!
#! INPUT
#!
qcdFiles = cms.untracked.vstring(
    '/store/relval/CMSSW_3_11_2/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_311_V2-v1/0004/B47EA9F2-BE44-E011-8C0B-00261894383C.root',
    '/store/relval/CMSSW_3_11_2/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_311_V2-v1/0001/FA74E93C-3F44-E011-B0FD-00261894398D.root',
    '/store/relval/CMSSW_3_11_2/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_311_V2-v1/0001/C0A9CEFC-3F44-E011-8834-00261894389E.root',
    '/store/relval/CMSSW_3_11_2/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_311_V2-v1/0001/7C73B75E-3D44-E011-B567-00248C55CC62.root',
    '/store/relval/CMSSW_3_11_2/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_311_V2-v1/0001/6EF4FDD7-3C44-E011-A7C3-002618FDA237.root'
    )

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))
process.source = cms.Source("PoolSource", fileNames = qcdFiles )


#!
#! SERVICES
#!
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('CommonTools.UtilAlgos.TFileService_cfi')
process.TFileService.fileName=cms.string('JRA.root')


#!
#! CHOOSE ALGORITHMS
#!
from JetMETAnalysis.JetAnalyzers.addAlgorithm import addAlgorithm

algorithms = []

algorithms.append('ak5calo')
algorithms.append('ak7calo')
algorithms.append('kt4calo')
algorithms.append('kt6calo')
algorithms.append('ak5pf')
algorithms.append('ak7pf')
algorithms.append('kt4pf')
algorithms.append('kt6pf')
algorithms.append('ak5jpt')

algorithms.append('ak5calol2l3')
algorithms.append('ak7calol2l3')
algorithms.append('kt4calol2l3')
algorithms.append('kt6calol2l3')
algorithms.append('ak5pfl2l3')
algorithms.append('ak7pfl2l3')
algorithms.append('kt4pfl2l3')
algorithms.append('kt6pfl2l3')
algorithms.append('ak5jptl2l3')

algorithms.append('ak5calol1l2l3')
algorithms.append('ak7calol1l2l3')
algorithms.append('kt4calol1l2l3')
algorithms.append('kt6calol1l2l3')
algorithms.append('ak5pfl1l2l3')
algorithms.append('ak7pfl1l2l3')
algorithms.append('kt4pfl1l2l3')
algorithms.append('kt6pfl1l2l3')
algorithms.append('ak5jptl1l2l3')


#
# taus
# ----
# require additional tags in CMSSW_3_8_6:
#
# V01-00-01 DataFormats/TauReco
# V01-00-11 RecoTauTag/Configuration
# V01-00-19 RecoTauTag/RecoTau
# V01-00-03 RecoTauTag/TauTagTools
#
# [runs but does not wirk in CMSSW_3_11_2]
#
#algorithms.append('ak5tauAll')
#algorithms.append('ak5tauHpsLoose')
#algorithms.append('ak5tauHpsMedium')
#algorithms.append('ak5tauHpsTight')
#algorithms.append('ak5tauTaNCLoose')
#algorithms.append('ak5tauTaNCMedium')
#algorithms.append('ak5tauTaNCTight')
#algorithms.append('ak5tauCombinedLoose')
#algorithms.append('ak5tauCombinedMedium')
#algorithms.append('ak5tauCombinedTight')



# set to False to use jets from the input file (NOT RECOMMENDED)
doJetReco = True

for algorithm in algorithms:
    addAlgorithm(process,algorithm,doJetReco)


#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!
