import os,sys

def  MakeHistFile(histlist, binlist,xminlist, xmaxlist,jobname):

    if not os.path.exists(str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/"+jobname ):
        os.system("mkdir " + str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/"+jobname)

    if not os.path.exists(str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/"+jobname +"/dat/"):
        os.system("mkdir " + str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/"+jobname +"/dat/")
    file_cuts=open(str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/"+jobname +"/dat/histfile.txt","w")
    for i in range(0,len(histlist)):
        file_cuts.write(histlist[i] + " " + binlist[i] + " " + xminlist[i] + " " +xmaxlist[i]+"\n")
    file_cuts.write("END")
    file_cuts.close()

    return


if os.getenv("USER") == "jalmond":
    os.system("cat ~/.ssh/config > check_connection.txt")
    
    ch_connect = open("check_connection.txt",'r')
    
    cpath="/tmp/"
    for line in ch_connect:
        if "ControlPath" in line:
            if "~/ssh" in line:
                cpath="~/"
            elif "/tmp/" in line:
                cpath="/tmp/"
            else:
                print "Modify the cms21 connection since  ControlPath in ~/.ssh/cofig is set to something other than tmp or home dir"
            
    ch_connect.close()
    os.system("rm check_connection.txt")

    
    os.system("ls " + cpath + " > check_snu_connection.txt")
    snu_connect = open("check_snu_connection.txt",'r')
    connected_lxplus=False

    for line in snu_connect:
        if "ssh-"+os.getenv("USER")+"@lxplus" in line:
            connected_lxplus=True
            
    os.system("rm check_snu_connection.txt")    
    if connected_lxplus == False:    
        print "No connection to lxplus please make connection in screen and run script again"
        quit()



from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--i", dest="i", default="123",help="tag")
parser.add_option("-x", "--x", dest="x", default="TEST",help="tag")

(options, args) = parser.parse_args()
configinputfile = options.i
jobdir = options.x

if not os.path.exists(configinputfile):
    print configinputfile + " is missing"
    sys.exit()

inputfile=""
histlist=[]
binlist=[]
xminlist=[]
xmaxlist=[]
cutlist=[]
skim=""
periodtag=""
datetag=""
analyzer=""
stream=""
isblind="false"
plottag="Default"
outputlist=[]
sigfile=""
_id=""
histfile=""
year =""
input_configfile = open(configinputfile,"r")

for line in input_configfile:
    if "*********************" in line:
        continue
    if "cut " in line and "# " in line:
        sline = line.split()
        cut = sline[2]
        cutlist.append(cut)
    elif "blinded" in line and "# " in line:
        sline = line.split()
        if sline[2] == "true":
            isblind="true"
    elif "year" in line:
        sline = line.split()
        year=sline[2]
    
    elif "hists:" in line:
        sline = line.split()
        histfile=sline[2]

    elif "ID" in line:
        sline = line.split()
        _id=sline[2]
        
    elif "samples" in line and "# " in line:
        sline = line.split()
        inputfile = str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/PlotConfig/"+sline[2]
    elif "skim" in line and "# " in line:
        sline = line.split()
        skim  = sline[2]
        print "skim = " + skim
    elif "periodtag" in line:
        sline = line.split()
        periodtag  =sline[2]
    elif "datetag" in line:
        sline = line.split()
        datetag  =sline[2]
    elif "DrawSig" in line:
        sline = line.split()
        sigfile  =sline[2]
    elif "analyzer" in line:
        sline = line.split()
        analyzer  =sline[2]
    elif "plottag" in line:
        sline = line.split()
        plottag  =sline[2]
    elif "stream" in line:
        sline = line.split()
        stream  =sline[2]
    elif "caption" in line:
        sline = line.replace("# caption","")
        sline = sline.replace("...",'.";')
        cap= open("caption.txt","w")
        cap.write(sline)
        cap.close()

    elif "#################" in line:
        if len(cutlist) == 0:
            continue
        inputdir=str(os.getenv("INFILE_MERGED_PATH"))  

        readhists=open(str(os.getenv("HNDILEPTONWORKSPACE_DIR")) + "/src/SignalRegionPlotter/CatPlotter/PlotConfig/"+histfile,"r")
        for rline in readhists:
            if "END" in rline:
                break
            if "##" in rline:
                sline = rline.split()
                histlist.append(sline[1])
                binlist.append(sline[2])
                xminlist.append(sline[3])
                xmaxlist.append(sline[4])
        readhists.close()

        MakeHistFile(histlist, binlist,xminlist, xmaxlist,jobdir)


        outputlist.append("https://jalmond.web.cern.ch/jalmond/SNU/histograms/"+plottag+"/indexCMS.html")

        os.system('python  ' + (os.getenv("HNDILEPTONWORKSPACE_DIR")) + '/src/SignalRegionPlotter/CatPlotter/setupplotter.py -i ' + inputfile + ' -d ' + inputdir + ' -x ' + jobdir + ' -s ' + stream + ' -a ' + analyzer + ' -S ' + skim + ' -C ' + cutlist[0] + ' -M ' + configinputfile + ' -c ' + plottag + ' -b ' + isblind + ' -t ' + sigfile + ' -y ' + year + ' -j ' + _id)
        histlist=[]
        binlist=[]
        xminlist=[]
        xmaxlist=[]
        cutlist=[]

print "Plots are found in:"
for x in outputlist:
    print x
