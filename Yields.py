# python program to round percentages to nearest integers and remove spaces
# written to be applied to tex files, with percentages in the format:
#             "13.7 \%" -> "14\%"


import re # for regex

# files
fnamesi = "Tex/Abstract.tex Tex/Results_and_discussion_cleavable.tex Tex/Acknowledgements.tex Tex/Results_and_discussion_HOcy5.tex Tex/CompoundList.tex Tex/Results_and_discussion_HOcy6.tex Tex/Conclusions_1.tex Tex/Conclusions_2.tex Tex/Results_and_discussion_intro_1.tex Tex/Experimental_1st_year.tex Tex/Results_and_discussion_intro_2.tex Tex/Experimental_AHL_analogue_conjugates.tex Tex/Results_and_discussion_nMeOA.tex Tex/Experimental_general.tex Tex/Results_and_discussion_PA_AIs.tex Tex/Experimental_triazoles.tex Tex/Results_and_discussion_SHLs.tex Tex/Future_work_1_chem.tex Tex/Future_work_1_bio.tex Tex/Future_work_2.tex Tex/Results_and_discussion_triazoles.tex Tex/Introduction.tex Tex/Summary.tex Tex/NMRs.tex Tex/Nomenclature.tex Tex/Results_and_discussion_antibiotics.tex Tex/Thesis_working_chapter.tex Tex/Results_and_discussion_bio_1.tex Tex/TitlePage.tex Tex/Results_and_discussion_bio_2.tex Tex/Experimental_bio.tex"


for fnamei in fnamesi.split():

    print ("File: ", fnamei)

    # opening input file
    fi = open(fnamei, 'r')
    
    # reading
    text = fi.read() 

    # regexing
    # IR
    regex = r"\\noindent{\\textbf{IR} \(neat\) \$\\nu_{max}\$ \/ cm\$\^{-1}\$ =([\S\s]*?)\\\\\[1\\baselineskip\]"
    matches = re.finditer(regex, text)
    for matchNum, match in enumerate(matches, start=1):
        
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

        irtext = r"""
            \noindent{\textbf{IR} (neat) $\nu_{max}$ / cm$^{-1}$ = 
                3337.0 (N-H),
                2927.7 (C-H),
                2857.1 (C-H),
                1723.7 (carbamate C=O),
                1634.5 ($\alpha$,$\beta$ unsaturated C=O),
                1610.7 (C=C),
                1580.9 (N-H bend)}
            \\[1\baselineskip]
        """
        
        irtext = match.group(groupNum)

        irtext = re.sub('([0-9]+[0-9])(\.[0-4])', '\g<1>', irtext)
        for match in re.finditer('([0-9]+[0-9])(\.[5-9])', irtext):
            irtext = irtext.replace(match.group(0),str(int(match.group(1))+1),1)
        #print (irtext)
    
    # Yields
    #text = re.sub('([^\.][0-9]+) \\\%', '\g<1>\%', text)
    #text = re.sub('([0-9]+)\.([0-4])([0-9]*) \\\%', '\g<1>\%', text)
    #for match in re.finditer('([0-9]+)\.([5-9])([0-9]*) \\\%', text):
    #        text = text.replace(match.group(0),str(int(match.group(1))+1)+'\%',1)
            
    # ml to mL
    #text = re.sub(' ml', ' mL', text) 
    
    # # closing input file      
    # fi.close() 
    
    # # output file name
    # fnameo =  fnamei
    
    # print ("output to", fnameo)

    # # writing to output file
    # fo = open(fnameo, 'w')
    # fo.write(text)
    # fo.close()