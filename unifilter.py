import sys
import re

def deltags(buf):
#Deletes all HTML tags and gives back content inside
    return re.sub(r"</?[\w\" =]+>", "", buf)

#Read the File
fp = open(sys.argv[1]).read()

#List of lines in the file
lines = fp.split("\n")

#Iterate each line and do the checks
ind = 0
unidict = {}
unilist = []
resfile = open("./result.txt", "w")
while ind < len(lines):
    curr_line = lines[ind]
    if curr_line.startswith("<h2>"):
        #Parse and put this data somewhere
        lineCont = deltags(curr_line)
        unirankstr = deltags(lines[ind + 2])
        if unirankstr.startswith("#"):
            unirank = unirankstr.split(" ")[0].split("#")[1]
            unidict[unirank] = lineCont
            resfile.write(lineCont + ": " + str(unirank) + "\n")
        ind = ind + 3
    else:
        ind = ind + 1
