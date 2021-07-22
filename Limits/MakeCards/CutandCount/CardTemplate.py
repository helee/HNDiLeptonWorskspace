import os


def GetNuisances(nFake):
    if (nFake==0.):
        return "21"
    else:
        return "20"

### The datacards used for 2016 analysis are located here : /data6/Users/jalmond/Limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton

### MuMu_Bin1/HNMuMu_100.txt
def WriteTemplateMMSR1LM(limitfile, flavour, SR, nCF, nFake):
    
    limitfile.write("Stat    lnN     1.2101  1.1087  -       1.0278 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
    limitfile.write("MuonPt  lnN     1.0087  -       -       1.0037 \n")
    limitfile.write("MuonID  lnN     1.021   -       -       1.0302 \n")
    limitfile.write("ElectronE       lnN     1.0047  -       -       1.0032 \n")
    limitfile.write("ElectronID      lnN     1.0023  -       -       1.0038 \n")
    limitfile.write("Trigger lnN     1.0036  -       -       1.0075 \n")
    limitfile.write("PU      lnN     1.0312  -       -       1.0197 \n")
    limitfile.write("JES     lnN     1.0807  -       -       1.0129 \n")
    limitfile.write("JER     lnN     1.0987  -       -       1.0178 \n")
    limitfile.write("Uncl    lnN     1.0601  -       -       1.0189 \n")
    limitfile.write("BEff    lnN     1.0241  -       -       1.0022 \n")
    limitfile.write("BMiss   lnN     1.0102  -       -       1.006 \n")
    limitfile.write("JMS     lnN     1.0393  -       -       1.0029 \n")
    limitfile.write("JMR     lnN     1.0039  -       -       1.0024 \n")
    limitfile.write("Tau21   lnN     1.0031  -       -       1.0027 \n")
    limitfile.write("MCNorm  lnN     1.1779  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")
    
    return


### MuMu_Bin1/HNMuMu_1000_VBF.txt
def WriteTemplateMMSR1HM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.1573  -       -       1.027 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.026 \n")
    limitfile.write("MuonPt  lnN     1.0042  -       -       1.0049 \n")
    limitfile.write("MuonID  lnN     1.0313  -       -       1.0335 \n")
    limitfile.write("ElectronE       lnN     1.0205  -       -       1.001 \n")
    limitfile.write("ElectronID      lnN     1.0136  -       -       1.0013 \n")
    limitfile.write("Trigger lnN     1.0186  -       -       1.0014 \n")
    limitfile.write("PU      lnN     1.0308  -       -       1.0026 \n")
    limitfile.write("JES     lnN     1.8857  -       -       1.0173 \n")
    limitfile.write("JER     lnN     1.4283  -       -       1.0145 \n")
    limitfile.write("Uncl    lnN     1.2319  -       -       1.0089 \n")
    limitfile.write("BEff    lnN     1.0042  -       -       1.0038 \n")
    limitfile.write("BMiss   lnN     1.0268  -       -       1.0033 \n")
    limitfile.write("JMS     lnN     1.0185  -       -       1.0009 \n")
    limitfile.write("JMR     lnN     1.003   -       -       1.0047 \n")
    limitfile.write("Tau21   lnN     1.0052  -       -       1.0013 \n")
    limitfile.write("MCNorm  lnN     1.6275  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -       -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


### MuMu_Bin1/HNMuMu_100.txt
#def WriteTemplateMMSR1HM(limitfile, flavour, SR, nCF, nFake):
#
#    limitfile.write("Stat    lnN     1.1573  -       -       1.0228 \n")
#    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
#    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
#    limitfile.write("MuonPt  lnN     1.0042  -       -       1.0076 \n")
#    limitfile.write("MuonID  lnN     1.0313  -       -       1.0331 \n")
#    limitfile.write("ElectronE       lnN     1.0205  -       -       1.0008 \n")
#    limitfile.write("ElectronID      lnN     1.0136  -       -       1.0015 \n")
#    limitfile.write("Trigger lnN     1.0186  -       -       1.0056 \n")
#    limitfile.write("PU      lnN     1.0308  -       -       1.004 \n")
#    limitfile.write("JES     lnN     1.8857  -       -       1.0105 \n")
#    limitfile.write("JER     lnN     1.4283  -       -       1.0094 \n")
#    limitfile.write("Uncl    lnN     1.2319  -       -       1.0057 \n")
#    limitfile.write("BEff    lnN     1.0042  -       -       1.0015 \n")
#    limitfile.write("BMiss   lnN     1.0268  -       -       1.0069 \n")
#    limitfile.write("JMS     lnN     1.0185  -       -       1.0014 \n")
#    limitfile.write("JMR     lnN     1.003   -       -       1.0028 \n")
#    limitfile.write("Tau21   lnN     1.0052  -       -       1.0034 \n")
#    limitfile.write("MCNorm  lnN     1.6275  -       -       - \n")
#    limitfile.write("CF      lnN     -       -       -       - \n")
#    if (nFake==0.):
#        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
#        limitfile.write("Fake    lnN     -       -       -       - \n") 
#    else:
#        limitfile.write("Fake    lnN     -       1.3     -       - \n")
#
#    return


### MuMu_Bin2/HNMuMu_100.txt
def WriteTemplateMMSR2LM(limitfile, flavour, SR, nCF, nFake):
    
    limitfile.write("Stat    lnN     1.2887  1.3591  -       1.5071 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
    limitfile.write("MuonPt  lnN     1.0063  -       -       1.0 \n")
    limitfile.write("MuonID  lnN     1.023   -       -       1.0318 \n")
    limitfile.write("ElectronE       lnN     1.0017  -       -       1.0 \n")
    limitfile.write("ElectronID      lnN     1.0019  -       -       1.0 \n")
    limitfile.write("Trigger lnN     1.005   -       -       1.0062 \n")
    limitfile.write("PU      lnN     1.0386  -       -       1.0083 \n")
    limitfile.write("JES     lnN     1.0678  -       -       1.0 \n")
    limitfile.write("JER     lnN     1.0048  -       -       1.0 \n")
    limitfile.write("Uncl    lnN     1.0173  -       -       1.0 \n")
    limitfile.write("BEff    lnN     1.006   -       -       1.0 \n")
    limitfile.write("BMiss   lnN     1.0113  -       -       1.0 \n")
    limitfile.write("JMS     lnN     1.0305  -       -       1.0 \n")
    limitfile.write("JMR     lnN     1.0381  -       -       1.185 \n")
    limitfile.write("Tau21   lnN     1.072   -       -       1.0721 \n")
    limitfile.write("MCNorm  lnN     1.3924  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")
    
    return 


### MuMu_Bin2/HNMuMu_1000_VBF.txt
def WriteTemplateMMSR2HM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.1583  -       -       1.0099 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.03 \n")
    limitfile.write("MuonPt  lnN     1.1391  -       -       1.0034 \n")
    limitfile.write("MuonID  lnN     1.0756  -       -       1.0349 \n")
    limitfile.write("ElectronE       lnN     1.028   -       -       1.0017 \n")
    limitfile.write("ElectronID      lnN     1.0408  -       -       1.0009 \n")
    limitfile.write("Trigger lnN     1.0262  -       -       1.0056 \n")
    limitfile.write("PU      lnN     1.0345  -       -       1.009 \n")
    limitfile.write("JES     lnN     1.0691  -       -       1.0032 \n")
    limitfile.write("JER     lnN     1.0528  -       -       1.0019 \n")
    limitfile.write("Uncl    lnN     1.0744  -       -       1.0017 \n")
    limitfile.write("BEff    lnN     1.0215  -       -       1.0049 \n")
    limitfile.write("BMiss   lnN     1.0159  -       -       1.004 \n")
    limitfile.write("JMS     lnN     1.0574  -       -       1.0008 \n")
    limitfile.write("JMR     lnN     1.0659  -       -       1.0014 \n")
    limitfile.write("Tau21   lnN     1.1537  -       -       1.0797 \n")
    limitfile.write("MCNorm  lnN     1.6169  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


### MuMu_Bin2/HNMuMu_1000.txt
#def WriteTemplateMMSR2HM(limitfile, flavour, SR, nCF, nFake):
#
#    limitfile.write("Stat    lnN     1.1583  -       -       1.008 \n")
#    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
#    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
#    limitfile.write("MuonPt  lnN     1.1391  -       -       1.0025 \n")
#    limitfile.write("MuonID  lnN     1.0756  -       -       1.0357 \n")
#    limitfile.write("ElectronE       lnN     1.028   -       -       1.0007 \n")
#    limitfile.write("ElectronID      lnN     1.0408  -       -       1.0008 \n")
#    limitfile.write("Trigger lnN     1.0262  -       -       1.0048 \n")
#    limitfile.write("PU      lnN     1.0345  -       -       1.0103 \n")
#    limitfile.write("JES     lnN     1.0691  -       -       1.0019 \n")
#    limitfile.write("JER     lnN     1.0528  -       -       1.0017 \n")
#    limitfile.write("Uncl    lnN     1.0744  -       -       1.0009 \n")
#    limitfile.write("BEff    lnN     1.0215  -       -       1.0038 \n")
#    limitfile.write("BMiss   lnN     1.0159  -       -       1.004 \n")
#    limitfile.write("JMS     lnN     1.0574  -       -       1.0009 \n")
#    limitfile.write("JMR     lnN     1.0659  -       -       1.0011 \n")
#    limitfile.write("Tau21   lnN     1.1537  -       -       1.0817 \n")
#    limitfile.write("MCNorm  lnN     1.6169  -       -       - \n")
#    limitfile.write("CF      lnN     -       -       -       - \n")
#    if (nFake==0.):
#        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
#        limitfile.write("Fake    lnN     -       -     -       - \n")
#    else:
#        limitfile.write("Fake    lnN     -       1.3     -       - \n")
#
#    return


### ElEl_Bin1/HNElEl_100.txt
def WriteTemplateEESR1LM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.2414  1.1977  1.019   1.0404 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n") 
    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
    limitfile.write("MuonPt  lnN     1.0066  -       -       1.0116 \n")
    limitfile.write("MuonID  lnN     1.02    -       -       1.0054 \n")
    limitfile.write("ElectronE       lnN     1.0251  -       -       1.0191 \n")
    limitfile.write("ElectronID      lnN     1.0303  -       -       1.0168 \n")
    limitfile.write("Trigger lnN     1.0488  -       -       1.0289 \n")
    limitfile.write("PU      lnN     1.0891  -       -       1.0244 \n")
    limitfile.write("JES     lnN     1.2491  -       -       1.0154 \n")
    limitfile.write("JER     lnN     1.0706  -       -       1.0385 \n")
    limitfile.write("Uncl    lnN     1.1304  -       -       1.044 \n")
    limitfile.write("BEff    lnN     1.0071  -       -       1.0077 \n")
    limitfile.write("BMiss   lnN     1.0157  -       -       1.01 \n")
    limitfile.write("JMS     lnN     1.0112  -       -       1.01 \n")
    limitfile.write("JMR     lnN     1.0075  -       -       1.0083 \n")
    limitfile.write("Tau21   lnN     1.0497  -       -       1.0086 \n")
    limitfile.write("MCNorm  lnN     1.135   -       -       - \n")
    limitfile.write("CF      lnN     -       -       1.439   - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")
    
    return 


### ElEl_Bin1/HNElEl_1000_VBF.txt    
def WriteTemplateEESR1HM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.4468  2.703   1.1033  1.036 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.026 \n")
    limitfile.write("MuonPt  lnN     1.0     -       -       1.0011 \n")
    limitfile.write("MuonID  lnN     1.0     -       -       1.0084 \n")
    limitfile.write("ElectronE       lnN     1.0582  -       -       1.0055 \n")
    limitfile.write("ElectronID      lnN     1.0444  -       -       1.0419 \n")
    limitfile.write("Trigger lnN     1.015   -       -       1.0131 \n")
    limitfile.write("PU      lnN     1.037   -       -       1.0102 \n")
    limitfile.write("JES     lnN     1.3421  -       -       1.01 \n")
    limitfile.write("JER     lnN     1.0031  -       -       1.0183 \n")
    limitfile.write("Uncl    lnN     1.021   -       -       1.0053 \n")
    limitfile.write("BEff    lnN     1.0     -       -       1.0069 \n")
    limitfile.write("BMiss   lnN     1.0039  -       -       1.0056 \n")
    limitfile.write("JMS     lnN     1.0001  -       -       1.0039 \n")
    limitfile.write("JMR     lnN     1.0     -       -       1.0038 \n")
    limitfile.write("Tau21   lnN     1.0039  -       -       1.0045 \n")
    limitfile.write("MCNorm  lnN     1.1926  -       -       - \n")
    limitfile.write("CF      lnN     -       -       1.9823  - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")
    
    return


### ElEl_Bin1/HNElEl_1000.txt
#def WriteTemplateEESR1HM(limitfile, flavour, SR, nCF, nFake):
#
#    limitfile.write("Stat    lnN     1.4468  2.703   1.1033  1.0315 \n")
#    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
#    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
#    limitfile.write("MuonPt  lnN     1.0     -       -       1.0065 \n")
#    limitfile.write("MuonID  lnN     1.0     -       -       1.0043 \n")
#    limitfile.write("ElectronE       lnN     1.0582  -       -       1.0053 \n")
#    limitfile.write("ElectronID      lnN     1.0444  -       -       1.0439 \n")
#    limitfile.write("Trigger lnN     1.015   -       -       1.0158 \n")
#    limitfile.write("PU      lnN     1.037   -       -       1.0116 \n")
#    limitfile.write("JES     lnN     1.3421  -       -       1.0067 \n")
#    limitfile.write("JER     lnN     1.0031  -       -       1.0066 \n")
#    limitfile.write("Uncl    lnN     1.021   -       -       1.0072 \n")
#    limitfile.write("BEff    lnN     1.0     -       -       1.0055 \n")
#    limitfile.write("BMiss   lnN     1.0039  -       -       1.0043 \n")
#    limitfile.write("JMS     lnN     1.0001  -       -       1.0011 \n")
#    limitfile.write("JMR     lnN     1.0     -       -       1.0035 \n")
#    limitfile.write("Tau21   lnN     1.0039  -       -       1.0024 \n")
#    limitfile.write("MCNorm  lnN     1.1926  -       -       - \n")
#    limitfile.write("CF      lnN     -       -       1.9823  - \n")
#    if (nFake==0.):
#        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
#        limitfile.write("Fake    lnN     -       -     -       - \n")
#    else:
#        limitfile.write("Fake    lnN     -       1.3     -       - \n")
#
#    return


### ElEl_Bin2/HNElEl_100.txt
def WriteTemplateEESR2LM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.1959  1.6453  1.1075  1.7097 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
    limitfile.write("MuonPt  lnN     1.0036  -       -       1.0 \n")
    limitfile.write("MuonID  lnN     1.0071  -       -       1.0 \n")
    limitfile.write("ElectronE       lnN     1.0056  -       -       1.0 \n")
    limitfile.write("ElectronID      lnN     1.014   -       -       1.0266 \n")
    limitfile.write("Trigger lnN     1.0121  -       -       1.0144 \n")
    limitfile.write("PU      lnN     1.0334  -       -       1.0116 \n")
    limitfile.write("JES     lnN     1.0393  -       -       1.0 \n")
    limitfile.write("JER     lnN     1.0383  -       -       1.0 \n")
    limitfile.write("Uncl    lnN     1.0079  -       -       1.0 \n")
    limitfile.write("BEff    lnN     1.0126  -       -       1.0 \n")
    limitfile.write("BMiss   lnN     1.0162  -       -       1.0 \n")
    limitfile.write("JMS     lnN     1.0528  -       -       1.0 \n")
    limitfile.write("JMR     lnN     1.0222  -       -       1.0 \n")
    limitfile.write("Tau21   lnN     1.0723  -       -       1.0725 \n")
    limitfile.write("MCNorm  lnN     1.2418  -       -       - \n")
    limitfile.write("CF      lnN     -       -       1.8357  - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")
    
    return


### ElEl_Bin2/HNElEl_1000_VBF.txt
def WriteTemplateEESR2HM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.4039  2.0623  1.2626  1.0134 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.029 \n")
    limitfile.write("MuonPt  lnN     1.0028  -       -       1.0009 \n")
    limitfile.write("MuonID  lnN     1.0033  -       -       1.0013 \n")
    limitfile.write("ElectronE       lnN     1.0513  -       -       1.0037 \n")
    limitfile.write("ElectronID      lnN     1.0699  -       -       1.0379 \n")
    limitfile.write("Trigger lnN     1.0315  -       -       1.0149 \n")
    limitfile.write("PU      lnN     1.0633  -       -       1.0125 \n")
    limitfile.write("JES     lnN     1.0615  -       -       1.0029 \n")
    limitfile.write("JER     lnN     1.0201  -       -       1.003 \n")
    limitfile.write("Uncl    lnN     1.0289  -       -       1.0003 \n")
    limitfile.write("BEff    lnN     1.0124  -       -       1.0042 \n")
    limitfile.write("BMiss   lnN     1.0264  -       -       1.0027 \n")
    limitfile.write("JMS     lnN     1.0564  -       -       1.0004 \n")
    limitfile.write("JMR     lnN     1.0292  -       -       1.0005 \n")
    limitfile.write("Tau21   lnN     1.0619  -       -       1.08 \n")
    limitfile.write("MCNorm  lnN     1.3929  -       -       - \n")
    limitfile.write("CF      lnN     -       -       2.01    - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


### ElEl_Bin2/HNElEl_1000.txt
#def WriteTemplateEESR2HM(limitfile, flavour, SR, nCF, nFake):
#
#    limitfile.write("Stat    lnN     1.4039  2.0623  1.2626  1.011 \n")
#    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
#    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
#    limitfile.write("MuonPt  lnN     1.0028  -       -       1.0011 \n")
#    limitfile.write("MuonID  lnN     1.0033  -       -       1.0007 \n")
#    limitfile.write("ElectronE       lnN     1.0513  -       -       1.0023 \n")
#    limitfile.write("ElectronID      lnN     1.0699  -       -       1.0376 \n")
#    limitfile.write("Trigger lnN     1.0315  -       -       1.0132 \n")
#    limitfile.write("PU      lnN     1.0633  -       -       1.0161 \n")
#    limitfile.write("JES     lnN     1.0615  -       -       1.0029 \n")
#    limitfile.write("JER     lnN     1.0201  -       -       1.0019 \n")
#    limitfile.write("Uncl    lnN     1.0289  -       -       1.0004 \n")
#    limitfile.write("BEff    lnN     1.0124  -       -       1.0037 \n")
#    limitfile.write("BMiss   lnN     1.0264  -       -       1.0048 \n")
#    limitfile.write("JMS     lnN     1.0564  -       -       1.0015 \n")
#    limitfile.write("JMR     lnN     1.0292  -       -       1.0002 \n")
#    limitfile.write("Tau21   lnN     1.0619  -       -       1.0808 \n")
#    limitfile.write("MCNorm  lnN     1.3929  -       -       - \n")
#    limitfile.write("CF      lnN     -       -       2.01    - \n")
#    if (nFake==0.):
#        limitfile.write("ZeroFake        gmN 0   -       0.1152  -       - \n")
#        limitfile.write("Fake    lnN     -       -     -       - \n")
#    else:
#        limitfile.write("Fake    lnN     -       1.3     -       - \n")
#
#    return


### MuEl_Bin1/HNMuEl_100.txt
def WriteTemplateEMSR1LM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.1871  1.1274  -       1.0284 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
    limitfile.write("MuonPt  lnN     1.0207  -       -       1.0044 \n")
    limitfile.write("MuonID  lnN     1.0105  -       -       1.0139 \n")
    limitfile.write("ElectronE       lnN     1.035   -       -       1.0073 \n")
    limitfile.write("ElectronID      lnN     1.0072  -       -       1.0092 \n")
    limitfile.write("Trigger lnN     1.0236  -       -       1.0039 \n")
    limitfile.write("PU      lnN     1.0128  -       -       1.0315 \n")
    limitfile.write("JES     lnN     1.0316  -       -       1.0043 \n")
    limitfile.write("JER     lnN     1.0358  -       -       1.0242 \n")
    limitfile.write("Uncl    lnN     1.0691  -       -       1.0401 \n")
    limitfile.write("BEff    lnN     1.0018  -       -       1.0087 \n")
    limitfile.write("BMiss   lnN     1.0128  -       -       1.0041 \n")
    limitfile.write("JMS     lnN     1.0066  -       -       1.0051 \n")
    limitfile.write("JMR     lnN     1.0034  -       -       1.0048 \n")
    limitfile.write("Tau21   lnN     1.0037  -       -       1.0024 \n")
    limitfile.write("MCNorm  lnN     1.148   -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.2037  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


### MuMu_Bin1/HNMuEl_1000_VBF.txt
def WriteTemplateEMSR1HM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.5213  2.9027  -       1.0286 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.03 \n")
    limitfile.write("MuonPt  lnN     1.0167  -       -       1.0027 \n")
    limitfile.write("MuonID  lnN     1.0314  -       -       1.0182 \n")
    limitfile.write("ElectronE       lnN     1.0107  -       -       1.0029 \n")
    limitfile.write("ElectronID      lnN     1.0355  -       -       1.0166 \n")
    limitfile.write("Trigger lnN     1.0079  -       -       1.0057 \n")
    limitfile.write("PU      lnN     1.0327  -       -       1.0154 \n")
    limitfile.write("JES     lnN     1.4994  -       -       1.0153 \n")
    limitfile.write("JER     lnN     1.0349  -       -       1.0044 \n")
    limitfile.write("Uncl    lnN     1.0181  -       -       1.0147 \n")
    limitfile.write("BEff    lnN     1.0053  -       -       1.0021 \n")
    limitfile.write("BMiss   lnN     1.0069  -       -       1.0074 \n")
    limitfile.write("JMS     lnN     1.0049  -       -       1.0029 \n")
    limitfile.write("JMR     lnN     1.0069  -       -       1.0037 \n")
    limitfile.write("Tau21   lnN     1.0081  -       -       1.0008 \n")
    limitfile.write("MCNorm  lnN     1.2672  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.2037  -       - \n")
        limitfile.write("Fake    lnN     -       -       -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


### MuEl_Bin2/HNMuEl_100.txt
def WriteTemplateEMSR2LM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.1284  1.1671  -       1.3233 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.05 \n")
    limitfile.write("MuonPt  lnN     1.0417  -       -       1.0 \n")
    limitfile.write("MuonID  lnN     1.0408  -       -       1.0425 \n")
    limitfile.write("ElectronE       lnN     1.0484  -       -       1.0706 \n")
    limitfile.write("ElectronID      lnN     1.0461  -       -       1.0192 \n")
    limitfile.write("Trigger lnN     1.0396  -       -       1.0036 \n")
    limitfile.write("PU      lnN     1.0543  -       -       1.0406 \n")
    limitfile.write("JES     lnN     1.0484  -       -       1.0836 \n")
    limitfile.write("JER     lnN     1.0397  -       -       1.0 \n")
    limitfile.write("Uncl    lnN     1.0479  -       -       1.0447 \n")
    limitfile.write("BEff    lnN     1.0475  -       -       1.0019 \n")
    limitfile.write("BMiss   lnN     1.0359  -       -       1.0 \n")
    limitfile.write("JMS     lnN     1.0447  -       -       1.007 \n")
    limitfile.write("JMR     lnN     1.0488  -       -       1.0 \n")
    limitfile.write("Tau21   lnN     1.0856  -       -       1.0731 \n")
    limitfile.write("MCNorm  lnN     1.3051  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.2037  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


### MuEl_Bin2/HNMuEl_1000_VBF.txt
def WriteTemplateEMSR2HM(limitfile, flavour, SR, nCF, nFake):

    limitfile.write("Stat    lnN     1.2438  -       -       1.0113 \n")
    limitfile.write("Lumi    lnN     1.025   -       -       1.025 \n")
    limitfile.write("PDF     lnN     -       -       -       1.029 \n")
    limitfile.write("MuonPt  lnN     1.3245  -       -       1.0046 \n")
    limitfile.write("MuonID  lnN     1.0286  -       -       1.0191 \n")
    limitfile.write("ElectronE       lnN     1.3679  -       -       1.0025 \n")
    limitfile.write("ElectronID      lnN     1.0531  -       -       1.0176 \n")
    limitfile.write("Trigger lnN     1.0251  -       -       1.0051 \n")
    limitfile.write("PU      lnN     1.0384  -       -       1.0126 \n")
    limitfile.write("JES     lnN     1.4183  -       -       1.0066 \n")
    limitfile.write("JER     lnN     1.3676  -       -       1.0074 \n")
    limitfile.write("Uncl    lnN     1.0292  -       -       1.0013 \n")
    limitfile.write("BEff    lnN     1.0184  -       -       1.0046 \n")
    limitfile.write("BMiss   lnN     1.049   -       -       1.0039 \n")
    limitfile.write("JMS     lnN     1.0265  -       -       1.0003 \n")
    limitfile.write("JMR     lnN     1.0443  -       -       1.0009 \n")
    limitfile.write("Tau21   lnN     1.1085  -       -       1.0793 \n")
    limitfile.write("MCNorm  lnN     1.5749  -       -       - \n")
    limitfile.write("CF      lnN     -       -       -       - \n")
    if (nFake==0.):
        limitfile.write("ZeroFake        gmN 0   -       0.2037  -       - \n")
        limitfile.write("Fake    lnN     -       -     -       - \n")
    else:
        limitfile.write("Fake    lnN     -       1.3     -       - \n")

    return


def WriteTemplate(limitfile, flavour, SR, mass, nCF, nFake):

    if flavour == "MuMu":
        if mass < 500:
            if(SR=="SR1"):
                WriteTemplateMMSR1LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR2") :
                WriteTemplateMMSR2LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR3"):
                WriteTemplateMMSR1LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR4"):
                WriteTemplateMMSR2LM(limitfile, flavour, SR, nCF, nFake)
        else:
            if(SR=="SR1"):
                WriteTemplateMMSR1HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR2"):
                WriteTemplateMMSR2HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR3"):
                WriteTemplateMMSR1HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR4"):
                WriteTemplateMMSR2HM(limitfile, flavour, SR, nCF, nFake)
    elif flavour == "EE":
        if mass< 500:
            if(SR=="SR1"):
                WriteTemplateEESR1LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR2"):
                WriteTemplateEESR2LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR3"):
                WriteTemplateEESR1LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR4"):
                WriteTemplateEESR2LM(limitfile, flavour, SR, nCF, nFake)
        else:
            if(SR=="SR1"):
                WriteTemplateEESR1HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR2"):
                WriteTemplateEESR2HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR3"):
                WriteTemplateEESR1HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR4"):
                WriteTemplateEESR2HM(limitfile, flavour, SR, nCF, nFake)
    else:
        if mass< 500:
            if(SR=="SR1"):
                WriteTemplateEMSR1LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR2"):
                WriteTemplateEMSR2LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR3"):
                WriteTemplateEMSR1LM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR4"):
                WriteTemplateEMSR2LM(limitfile, flavour, SR, nCF, nFake)
        else:
            if(SR=="SR1"):
                WriteTemplateEMSR1HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR2"):
                WriteTemplateEMSR2HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR3"):
                WriteTemplateEMSR1HM(limitfile, flavour, SR, nCF, nFake)
            if(SR=="SR4"):
                WriteTemplateEMSR2HM(limitfile, flavour, SR, nCF, nFake)

        return
