import re

TFile  = open("Tex\Experimental_1st_year.tex", "r")
TString = TFile.read()

NPList = re.findall(r'^(?!%).+$', TString, flags=re.MULTILINE)
NPString = "".join(NPList)
CList = re.findall(r'cmpd:[^}]+', NPString)

UList = []
[UList.append(item) for item in CList if item not in UList]
out = ", ".join(UList)
print(out)
