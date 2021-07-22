#!/bin/bash
if [[ $HOSTNAME == "tamsa1" ]];
then

    #### use cvmfs for root ####
    export CMS_PATH=/cvmfs/cms.cern.ch
    source $CMS_PATH/cmsset_default.sh
    export SCRAM_ARCH=slc7_amd64_gcc700
    export cmsswrel='cmssw-patch/CMSSW_10_4_0_patch1'
    cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/$cmsswrel/src
    echo "@@@@ SCRAM_ARCH = "$SCRAM_ARCH
    echo "@@@@ cmsswrel = "$cmsswrel
    echo "@@@@ scram..."
    eval `scramv1 runtime -sh`
    cd -
    source /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/$cmsswrel/external/$SCRAM_ARCH/bin/thisroot.sh
    
    export VERSION="Initial"
    export FLATVERSION="Run2Legacy_v4"
    export HNDILEPTONWORKSPACE_DIR=`pwd`
    export PLOT_PATH=$PWD/Plots/
    export OUTFILE_PATH=$HNDILEPTONWORKSPACE_DIR/rootfiles/
    export DATACARD_SHAPE_PATH=$HNDILEPTONWORKSPACE_DIR/Limits/DataCardsShape/
    export INFILE_MERGED_PATH=/data6/Users/helee/working_HN_Plotter/Run2Legacy_v4_mll10/ 
    export INFILE_PATH=/data6/Users/helee/SKFlatOutput/Run2Legacy_v4/
    
    export SCRIPT_DIR=$HNDILEPTONWORKSPACE_DIR/script/
    export ROOT_INCLUDE_PATH=$ROOT_INCLUDE_PATH:$HNDILEPTONWORKSPACE_DIR/include/:$HNDILEPTONWORKSPACE_DIR/src/:$HNDILEPTONWORKSPACE_DIR/SignalEfficiency:$HNDILEPTONWORKSPACE_DIR/SignalRegionPlotter:$HNDILEPTONWORKSPACE_DIR/MakeCards:$HNDILEPTONWORKSPACE_DIR/OutputTool
    #export LIMIT_PATH="/data6/Users/jalmond/Limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton/batch/"
    export LIMIT_PATH="/data6/Users/helee/Limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/data/HNtypeI/batch/"

fi
if [[ $HOST == "JohnMB2018s-MacBook-Pro.local" ]];then

    export VERSION="Initial"
    export FLATVERSION="Run2Legacy_v4"
    export HNDILEPTONWORKSPACE_DIR=`pwd`
    export PLOT_PATH=/Users/john/HNPlots/ 
    export OUTFILE_PATH=$HNDILEPTONWORKSPACE_DIR/rootfiles/
    export INFILE_MERGED_PATH=$HOME/HNDiLeptonWorskspace/OutputTool/MergedFiles/
    export INFILE_PATH=$HNDILEPTONWORKSPACE_DIR/Files/
    export SCRIPT_DIR=$HNDILEPTONWORKSPACE_DIR/script/
    export ROOT_INCLUDE_PATH=$ROOT_INCLUDE_PATH:$HNDILEPTONWORKSPACE_DIR/include/:$HNDILEPTONWORKSPACE_DIR/src/:$HNDILEPTONWORKSPACE_DIR/SignalEfficiency:$HNDILEPTONWORKSPACE_DIR/SignalRegionPlotter:$HNDILEPTONWORKSPACE_DIR/MakeCards:$HNDILEPTONWORKSPACE_DIR/OutputTool
    export LIMIT_PATH=$HNDILEPTONWORKSPACE_DIR/LimitCode/CMS-StatisticalTools/:$HNDILEPTONWORKSPACE_DIR/Limits/MakeShapeInput

fi    
alias run="bash "$SCRIPT_DIR"/run.sh"
alias skout='cd '$PLOT_PATH

