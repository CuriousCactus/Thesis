# python program to round percentages to nearest integers
import re # for regex

# files
fnamesi = "Results_and_discussion_antibiotics.tex"

for fnamei in fnamesi.split():

    print ("rounding percentages in", fnamei)

    # opening input file
    fi = open(fnamei, 'r')
   
    # reading
    text = fi.read()

    # regexing
    text = re.sub('([0-9]+)\.([0-4])([0-9]*)\%', '\g<1>%', text)
    for match in re.finditer('([0-9]+)\.([5-9])([0-9]*)\%', text):
          text = text.replace(match.group(0),str(int(match.group(1))+1)+'%',1)
   
    # closing input file     
    fi.close()
   
    # output file name
    fnameo = "rounded_" + fnamei
   
    print ("output to", fnameo)

    # writing to output file
    fo = open(fnameo, 'w')
    fo.write(text)
    fo.close()