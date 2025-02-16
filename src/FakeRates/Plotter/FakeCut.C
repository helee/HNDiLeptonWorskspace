#include "base_functions.h"
#include "Macros.h"
#include "mylib.h"
#include "canvas_margin.h"

void FakeCut(TString sample = "ZGTo2LG",TString channel="muon", TString var="dxy",TString type="-1.000000", TString year="2016"){
  

  TString skim="SkimTree_SSNonIso";
  // check which pc is running script to setup local paths
  TString s_hostname = GetHostname();

  TString analysername="HNtypeI_JA";

  vector<TString> code_names= {"HNtypeI_JA"};
  vector<TString> channel_names= {"muon","electron"};

  if(std::find(code_names.begin(), code_names.end(), analysername) != code_names.end()) cout << "Running with code " << analysername << endl;
  else {cout << "Error in input of analyzer: " << analysername << endl; for (auto i: code_names)   std::cout << i << ' '; return; }

  if(std::find(channel_names.begin(), channel_names.end(), channel) != channel_names.end()) cout <<	"Running with channel " <<  channel <<	endl;
  else {cout << "Error in input of _chan: " << channel << endl;  for (auto i: channel_names)   std::cout << i << ' '; return; }

  
  // local path names
  TString ENV_FILE_PATH= (getenv("INFILE_PATH"));
  TString ENV_MERGEDFILE_PATH = getenv("INFILE_MERGED_PATH");
  TString ENV_PLOT_PATH = getenv("PLOT_PATH");
  TString FLATVERSION = getenv("FLATVERSION");

  
  MakeDir(ENV_PLOT_PATH + FLATVERSION);
  TString input_path = ENV_FILE_PATH + FLATVERSION+"/"+analysername+"/";
  TString output = ENV_PLOT_PATH + FLATVERSION + "/"+analysername+"/";

  MakeDir(output);
  output+="/FakeCuts/";
  MakeDir(output);

  output+=channel+"/";
  MakeDir(output);
  output+=year+"/";
  MakeDir(output);

  cout << "FakerateType1::LOG Output dir = " << output << endl;
  
  if(s_hostname == "JohnMB2018s-MacBook-Pro.local"){
    input_path = "/Users/john/HNDiLeptonWorskspace/OutputTool/MergedFiles/";
  }

  // Set Plotting style
  setTDRStyle();
  gStyle->SetPalette(1);
    
  
  vector<TString> muIDs={"POGTightPFIsoVeryVeryTight"};
  vector<TString> elIDs={"HNTight_dxy05_05_dz01_ip4_4"};

  cout << "List of IDs : " << endl;
  for (auto i: muIDs) cout << i << endl;
  for (auto i: elIDs) cout << i << endl;

  
  vector<TString> SR = {""};


  TString data_path ="/Users/john/HNDiLeptonWorskspace/Files/HNtypeI_JA/"+year+"/HNtypeI_JA_SkimTree_SSNonIso_"+sample+".root";
  
  
  TFile * file_data = new TFile((data_path).Data());
  if(CheckFile(file_data) > 0) return;
  
  vector<TString> IDs;
  // get efficiencies for each ID ran based on channel
  if ( channel.Contains("el") ) IDs = elIDs;
  else IDs =   muIDs;
  
  // hist leg
  
  // graph leg
  
  // canvas for hists
  TString canvasname= channel;
  TCanvas* c1 = new TCanvas(canvasname,canvasname, 800,800);

  TString histname=channel+"_"+var+"_type_"+type+IDs[0];
  TH1D* data_hist = GetHist(file_data,histname);

  data_hist->GetYaxis()->SetRangeUser(0.1, data_hist->GetMaximum());
  double eff = data_hist->Integral(data_hist->FindBin(-0.05), data_hist->FindBin(0.05))/ data_hist->Integral();
  string s_eff = std::to_string(eff);
  data_hist->SetLineColor(kRed);
  data_hist->SetLineWidth(3.);
  TLegend *legend = MakeLegend(0.65, 0.65, 0.9, 0.92);
  //if(type.Contains("-1"))legend->AddEntry(data_hist,var + " Lep Type -1","l");
  
  c1->SetLogy();
  c1->cd();
  data_hist->Draw("hist");

  TLine *devz = new TLine(-0.05,0.1,-0.05,data_hist->GetMaximum());
  devz->SetLineWidth(2);
  devz->SetLineStyle(1);
  devz->Draw("SAME");
  TLine *devz2 = new TLine(0.05,0.1,0.05,data_hist->GetMaximum());
  devz2->SetLineWidth(2);
  devz2->SetLineStyle(1);
  devz2->Draw("SAME");


  legend->Draw();
  
  setTDRStyle();
 

  TString _type="Lep Type 1";
  if(type.Contains("-1")) _type="Lep Type -1";
  else if(type.Contains("-2")) _type="Lep Type -2";
  else if(type.Contains("-3")) _type="Lep Type -3";
  else if(type.Contains("-4")) _type="Lep Type -4";
  else if(type.Contains("-5")) _type="Lep Type -5";
  else if(type.Contains("-6")) _type="Lep Type -6";
  else if(type.Contains("-7")) _type="Lep Type -7";
  else if(type.Contains("-8")) _type="Lep Type -8";
  else if(type.Contains("-9")) _type="Lep Type -9";
  else if(type.Contains("-10")) _type="Lep Type -10";
  else if(type.Contains("0.,")) _type="Lep Type 0";
  else if(type.Contains("1.")) _type="Lep Type 1";
  else if(type.Contains("2.")) _type="Lep Type 2";
  else if(type.Contains("3.")) _type="Lep Type 3";
  else if(type.Contains("4.")) _type="Lep Type 4";
  else if(type.Contains("5.")) _type="Lep Type 5";
  else if(type.Contains("6.")) _type="Lep Type 6";

  DrawLatexWithLabel(year,sample,0.25,0.88);
  DrawLatexWithLabel(year,_type,0.25,0.78);
  DrawLatexWithLabel(year,"Cut Eff. ="+TString(s_eff),0.25,0.83);
  
  TString save_sg= output + "/fake_var_"+channel + "_"+var+"_"+year+".pdf";
  
  c1->SaveAs(save_sg);
  OutMessage("GetSignalEfficiency",save_sg);
  
  file_data->Close();
    
  delete file_data;
  
  return;
}
