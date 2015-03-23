import FWCore.ParameterSet.Config as cms

process = cms.Process("Ana")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MCRUN2_74_V7'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	'file:../../step3_RAW2DIGI_L1Reco_RECO.root',
    )
)

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("test.root"))

process.hltanalyzer = cms.EDAnalyzer('TriggerAnalyzer',
				     hltresults = cms.InputTag("TriggerResults","","HLT"),
)

process.p = cms.Path(process.hltanalyzer)
