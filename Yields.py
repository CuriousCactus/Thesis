# python program to round percentages to nearest integers and remove spaces
# written to be applied to tex files, with percentages in the format:
#             "13.7 \%" -> "14\%"


import re # for regex

# files
fnamesi = """
Tex/Abstract.tex
Tex/Acknowledgements.tex
Tex/CompoundList.tex
Tex/Conclusions_1.tex
Tex/Conclusions_2.tex
Tex/Experimental_1st_year.tex
Tex/Experimental_AHL_analogue_conjugates.tex
Tex/Experimental_bio.tex
Tex/Experimental_general.tex
Tex/Experimental_triazoles.tex
Tex/Future_work_1_bio.tex
Tex/Future_work_1_chem.tex
Tex/Future_work_2.tex
Tex/Introduction.tex
Tex/NMRs.tex
Tex/Nomenclature.tex
Tex/Results_and_discussion_antibiotics.tex
Tex/Results_and_discussion_bio_1.tex
Tex/Results_and_discussion_bio_2.tex
Tex/Results_and_discussion_cleavable.tex
Tex/Results_and_discussion_HOcy5.tex
Tex/Results_and_discussion_HOcy6.tex
Tex/Results_and_discussion_intro_1.tex
Tex/Results_and_discussion_intro_2.tex
Tex/Results_and_discussion_nMeOA.tex
Tex/Results_and_discussion_PA_AIs.tex
Tex/Results_and_discussion_SHLs.tex
Tex/Results_and_discussion_triazoles.tex
Tex/Summary.tex
Tex/Thesis_working_chapter.tex
Tex/TitlePage.tex
"""

for fnamei in fnamesi.split():

    print ("File: ", fnamei)

    # opening input file
    fi = open(fnamei, 'r')
    
    # reading
    text = fi.read() 

    # regexing
    # NB match.group(0) means all of the match groups, NOT the first one!
    
    # mp
    for match in re.finditer(r'(\\textbf{mp} \\textit{T} \/ \$\^{\\circ}\$C = )([0-9]+)(\.[5-9])', text):
        text = text.replace(match.group(0),match.group(1)+str(int(match.group(2))+1),1)
        print (match.group(0),match.group(1)+str(int(match.group(2))+1))
    for match in re.finditer(r'(\\textbf{mp} \\textit{T} \/ \$\^{\\circ}\$C = )([0-9]+)(\.[0-4])', text):
        text = text.replace(match.group(0),match.group(1)+str(int(match.group(2))),1)
        print (match.group(0),match.group(1)+str(int(match.group(2))))
    #print (text)
        
    # # IR
    # irregex = r"\\noindent{\\textbf{IR} \(neat\) \$\\nu_{max}\$ \/ cm\$\^{-1}\$ =([\S\s]*?)\\\\\[1\\baselineskip\]"
    # matches = re.finditer(irregex, text)
    # for matchNum, match in enumerate(matches, start=1):
        
        # #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        # for groupNum in range(0, len(match.groups())):
            # groupNum = groupNum + 1
            
            # print ("{group}".format(group = match.group(groupNum)))
        
        # irtext = match.group(groupNum)

        # for match in re.finditer('([0-9]+[0-9])(\.[5-9])', irtext):
            # text = text.replace(match.group(0),str(int(match.group(1))+1),1)
        # for match in re.finditer('([0-9]+[0-9])(\.[0-4])', irtext):
            # text = text.replace(match.group(0),str(int(match.group(1))),1)
        # print (text)
    
    # # Yields
    # text = re.sub('([^\.][0-9]+) \\\%', '\g<1>\%', text)
    # text = re.sub('([0-9]+)\.([0-4])([0-9]*) \\\%', '\g<1>\%', text)
    # for match in re.finditer('([0-9]+)\.([5-9])([0-9]*) \\\%', text):
        # text = text.replace(match.group(0),str(int(match.group(1))+1)+'\%',1)
            
    # # ml to mL
    # text = re.sub(' ml', ' mL', text) 
    
    # closing input file      
    fi.close() 
    
    # output file name
    fnameo = fnamei
    
    print ("Output to:", fnameo)

    # writing to output file
    fo = open(fnameo, 'w')
    fo.write(text)
    fo.close()