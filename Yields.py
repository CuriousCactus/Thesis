# python program to round percentages to nearest integers and remove spaces
# written to be applied to tex files, with percentages in the format:
#             "13.7 \%" -> "14\%"


import re # for regex

# files
fnamesi = "Tex/Abstract.tex Tex/Results_and_discussion_cleavable.tex Tex/Acknowledgements.tex Tex/Results_and_discussion_HOcy5.tex Tex/CompoundList.tex Tex/Results_and_discussion_HOcy6.tex Tex/Conclusions.tex Tex/Results_and_discussion_intro_1.tex Tex/Experimental_1st_year.tex Tex/Results_and_discussion_intro_2.tex Tex/Experimental_AHL_analogue_conjugates.tex Tex/Results_and_discussion_nMeOA.tex Tex/Experimental_general.tex Tex/Results_and_discussion_PA_AIs.tex Tex/Experimental_triazoles.tex Tex/Results_and_discussion_SHLs.tex Tex/Future_work.tex Tex/Results_and_discussion_triazoles.tex Tex/Introduction.tex Tex/Summary.tex Tex/NMRs.tex Tex/Test.tex Tex/Nomenclature.tex Tex/Thesis.tex Tex/Results_and_discussion_antibiotics.tex Tex/Thesis_working_chapter.tex Tex/Results_and_discussion_bio_1.tex Tex/TitlePage.tex Tex/Results_and_discussion_bio_2.tex"

for fnamei in fnamesi.split():

    print ("rounding percentages in", fnamei)

    # opening input file
    fi = open(fnamei, 'r')
    
    # reading
    text = fi.read() 

    # regexing
    text = re.sub('([^\.][0-9]+) \\\%', '\g<1>\%', text)
    text = re.sub('([0-9]+)\.([0-4])([0-9]*) \\\%', '\g<1>\%', text)
    for match in re.finditer('([0-9]+)\.([5-9])([0-9]*) \\\%', text):
          text = text.replace(match.group(0),str(int(match.group(1))+1)+'\%',1)
    
    # closing input file      
    fi.close() 
    
    # output file name
    fnameo =  fnamei
    
    print ("output to", fnameo)

    # writing to output file
    fo = open(fnameo, 'w')
    fo.write(text)
    fo.close()