import os
import sys

SAMPLES={"GluGluHToWWTo2L2NuPowheg_M125_private","DYJetsToLL_M-50__part0","DYJetsToLL_M-50__part1","DYJetsToLL_M-50__part2","DYJetsToLL_M-50__part3","DYJetsToLL_M-50__part4","DYJetsToLL_M-50__part5","DYJetsToLL_M-50__part6","DYJetsToLL_M-50__part7","DYJetsToLL_M-50__part8","DYJetsToLL_M-50__part9","DYJetsToLL_M-50__part10","DYJetsToLL_M-50__part11","DYJetsToLL_M-50__part12","DYJetsToLL_M-50__part13","DYJetsToLL_M-50__part14","DYJetsToLL_M-50__part15","DYJetsToLL_M-50__part16","DYJetsToLL_M-50__part17","DYJetsToLL_M-50__part18","DYJetsToLL_M-50__part19","DYJetsToLL_M-50__part20","ST_tW_top","TTTo2L2Nu__part0","TTTo2L2Nu__part1","TTTo2L2Nu__part2","TTToSemileptonic__part0","TTToSemileptonic__part1","WJetsToLNu-LO__part0","WJetsToLNu-LO__part1","WJetsToLNu-LO__part2","WWTo2L2Nu"}

#SAMPLES={"GluGluHToWWTo2L2NuPowheg_M125_private","DYJetsToLL_M-50__part0","DYJetsToLL_M-50__part1","DYJetsToLL_M-50__part2","DYJetsToLL_M-50__part3","DYJetsToLL_M-50__part4","DYJetsToLL_M-50__part5","DYJetsToLL_M-50__part6","DYJetsToLL_M-50__part7","DYJetsToLL_M-50__part8","DYJetsToLL_M-50__part9","DYJetsToLL_M-50__part10","DYJetsToLL_M-50__part11","DYJetsToLL_M-50__part12","DYJetsToLL_M-50__part13","DYJetsToLL_M-50__part14","DYJetsToLL_M-50__part15","DYJetsToLL_M-50__part16","DYJetsToLL_M-50__part17","DYJetsToLL_M-50__part18","DYJetsToLL_M-50__part19","DYJetsToLL_M-50__part20","ST_tW_top","TTTo2L2Nu__part0","TTTo2L2Nu__part1","TTTo2L2Nu__part2","TTToSemileptonic__part0","TTToSemileptonic__part1","WJetsToLNu-LO__part0","WJetsToLNu-LO__part1","WJetsToLNu-LO__part2","WWTo2L2Nu","DoubleEG_Run2017B-31Mar2018-v1","SingleElectron_Run2017D-31Mar2018-v1__part0","SingleMuon_Run2017D-31Mar2018-v1__part4","DoubleEG_Run2017C-31Mar2018-v1__part0","SingleElectron_Run2017D-31Mar2018-v1__part1","SingleMuon_Run2017D-31Mar2018-v1__part5","DoubleEG_Run2017C-31Mar2018-v1__part1","SingleElectron_Run2017E-31Mar2018-v1__part0","SingleMuon_Run2017E-31Mar2018-v1__part0","DoubleEG_Run2017D-31Mar2018-v1","SingleElectron_Run2017E-31Mar2018-v1__part1","SingleMuon_Run2017E-31Mar2018-v1__part10","DoubleEG_Run2017E-31Mar2018-v1","SingleElectron_Run2017E-31Mar2018-v1__part2","SingleMuon_Run2017E-31Mar2018-v1__part11","DoubleEG_Run2017F-31Mar2018-v1__part0","SingleElectron_Run2017E-31Mar2018-v1__part3","SingleMuon_Run2017E-31Mar2018-v1__part12","DoubleEG_Run2017F-31Mar2018-v1__part1","SingleElectron_Run2017F-31Mar2018-v1__part0","SingleMuon_Run2017E-31Mar2018-v1__part1","DoubleMuon_Run2017B-31Mar2018-v1__part0","SingleElectron_Run2017F-31Mar2018-v1__part1","SingleMuon_Run2017E-31Mar2018-v1__part2","DoubleMuon_Run2017B-31Mar2018-v1__part1","SingleElectron_Run2017F-31Mar2018-v1__part2","SingleMuon_Run2017E-31Mar2018-v1__part3","DoubleMuon_Run2017C-31Mar2018-v1__part0","SingleElectron_Run2017F-31Mar2018-v1__part3","SingleMuon_Run2017E-31Mar2018-v1__part4","DoubleMuon_Run2017C-31Mar2018-v1__part1","SingleElectron_Run2017F-31Mar2018-v1__part4","SingleMuon_Run2017E-31Mar2018-v1__part5","DoubleMuon_Run2017C-31Mar2018-v1__part2","SingleMuon_Run2017B-31Mar2018-v1__part0","SingleMuon_Run2017E-31Mar2018-v1__part6","DoubleMuon_Run2017D-31Mar2018-v1__part0","SingleMuon_Run2017B-31Mar2018-v1__part1","SingleMuon_Run2017E-31Mar2018-v1__part7","DoubleMuon_Run2017D-31Mar2018-v1__part1","SingleMuon_Run2017B-31Mar2018-v1__part2","SingleMuon_Run2017E-31Mar2018-v1__part8","DoubleMuon_Run2017E-31Mar2018-v1__part0","SingleMuon_Run2017B-31Mar2018-v1__part3","SingleMuon_Run2017E-31Mar2018-v1__part9","DoubleMuon_Run2017E-31Mar2018-v1__part1","SingleMuon_Run2017B-31Mar2018-v1__part4","SingleMuon_Run2017F-31Mar2018-v1__part0","DoubleMuon_Run2017E-31Mar2018-v1__part2","SingleMuon_Run2017B-31Mar2018-v1__part5","SingleMuon_Run2017F-31Mar2018-v1__part10","DoubleMuon_Run2017E-31Mar2018-v1__part3","SingleMuon_Run2017B-31Mar2018-v1__part6","SingleMuon_Run2017F-31Mar2018-v1__part11","DoubleMuon_Run2017F-31Mar2018-v1__part0","SingleMuon_Run2017B-31Mar2018-v1__part7","SingleMuon_Run2017F-31Mar2018-v1__part12","DoubleMuon_Run2017F-31Mar2018-v1__part1","SingleMuon_Run2017B-31Mar2018-v1__part8","SingleMuon_Run2017F-31Mar2018-v1__part13","DoubleMuon_Run2017F-31Mar2018-v1__part2","SingleMuon_Run2017C-31Mar2018-v1__part0","SingleMuon_Run2017F-31Mar2018-v1__part14","DoubleMuon_Run2017F-31Mar2018-v1__part3","SingleMuon_Run2017C-31Mar2018-v1__part10","SingleMuon_Run2017F-31Mar2018-v1__part15","DoubleMuon_Run2017F-31Mar2018-v1__part4","SingleMuon_Run2017C-31Mar2018-v1__part11","SingleMuon_Run2017F-31Mar2018-v1__part16","DoubleMuon_Run2017F-31Mar2018-v1__part5","SingleMuon_Run2017C-31Mar2018-v1__part12","SingleMuon_Run2017F-31Mar2018-v1__part17","MuonEG_Run2017B-31Mar2018-v1","SingleMuon_Run2017C-31Mar2018-v1__part1","SingleMuon_Run2017F-31Mar2018-v1__part18","MuonEG_Run2017C-31Mar2018-v1","SingleMuon_Run2017C-31Mar2018-v1__part2","SingleMuon_Run2017F-31Mar2018-v1__part19","MuonEG_Run2017D-31Mar2018-v1","SingleMuon_Run2017C-31Mar2018-v1__part3","SingleMuon_Run2017F-31Mar2018-v1__part1","MuonEG_Run2017E-31Mar2018-v1","SingleMuon_Run2017C-31Mar2018-v1__part4","SingleMuon_Run2017F-31Mar2018-v1__part2","MuonEG_Run2017F-31Mar2018-v1__part0","SingleMuon_Run2017C-31Mar2018-v1__part5","SingleMuon_Run2017F-31Mar2018-v1__part3","MuonEG_Run2017F-31Mar2018-v1__part1","SingleMuon_Run2017C-31Mar2018-v1__part6","SingleMuon_Run2017F-31Mar2018-v1__part4","SingleElectron_Run2017B-31Mar2018-v1__part0","SingleMuon_Run2017C-31Mar2018-v1__part7","SingleMuon_Run2017F-31Mar2018-v1__part5","SingleElectron_Run2017B-31Mar2018-v1__part1","SingleMuon_Run2017C-31Mar2018-v1__part8","SingleMuon_Run2017F-31Mar2018-v1__part6","SingleElectron_Run2017C-31Mar2018-v1__part0","SingleMuon_Run2017C-31Mar2018-v1__part9","SingleMuon_Run2017F-31Mar2018-v1__part7","SingleElectron_Run2017C-31Mar2018-v1__part1","SingleMuon_Run2017D-31Mar2018-v1__part0","SingleMuon_Run2017F-31Mar2018-v1__part8","SingleElectron_Run2017C-31Mar2018-v1__part2","SingleMuon_Run2017D-31Mar2018-v1__part1","SingleMuon_Run2017F-31Mar2018-v1__part9","SingleElectron_Run2017C-31Mar2018-v1__part3","SingleMuon_Run2017D-31Mar2018-v1__part2","SingleElectron_Run2017C-31Mar2018-v1__part4","SingleMuon_Run2017D-31Mar2018-v1__part3"}

#SAMPLES={"GluGluHToWWTo2L2NuPowheg_M125_private"}

#WPS={"Medium","Medium_HWW","Tight","Tight_HWW"}

WPS={"Tight_HWW", "mvaFall17noIso_WPL", "mvaFall17Iso_WPL", "mvaFall17noIso_WP80", "mvaFall17Iso_WP80", "mvaFall17noIso_WP90", "mvaFall17Iso_WP90", "mvaFall17noIso_WPL_HWW", "mvaFall17Iso_WPL_HWW", "mvaFall17noIso_WP80_HWW", "mvaFall17Iso_WP80_HWW", "mvaFall17noIso_WP90_HWW", "mvaFall17Iso_WP90_HWW"}

#CH = {"em","mm"}
CH = {"em"}


P2 = {"high","low"}
#P2 = {"high"}

JET = {"0j","1j"}
#JET = {"0j"}


for s in SAMPLES:
    for wp in WPS:
        for ch in CH:
            for pt in P2:
                for j in JET:
                    print 'bsub -q 2nd -u pipo12345 submit_Higgs_eleWP.sh ' + s + ' ' + wp + ' ' + ch + ' ' + pt + ' ' + j

                    


