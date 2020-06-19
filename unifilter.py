import sys
import re
import requests

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
            #Get Fees
            #query = query.replace(" ","+")
            queryfees = "https://search.prtl.co/2018-07-23/?q=en-283%7Ckw-" + lineCont + "%7Clv-master%7Cmh-face2face%7Ctc-EUR"

            #r = request.urlopen(query)
            try:
                r = requests.get(queryfees)
                if("tuition_fee" in r.json()[0]):
                    fee = r.json()[0]["tuition_fee"]
                    feeval= fee["value"]
                    feefreq = fee["unit"]
                    feecurr = fee["currency"]
                    feestr = str(feeval) + " " + feecurr + " per " + feefreq 
                else:
                    feestr = "Not Provided"
            except IndexError:
                feestr = "Not Provided"
        resfile.write(lineCont + ";" + str(unirank) + ";" + feestr + "\n")
        ind = ind + 3
    else:
        ind = ind + 1
