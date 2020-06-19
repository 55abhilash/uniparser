import requests
from bs4 import BeautifulSoup 
from urllib import request

query = input("Enter Uni: ")
query = query.replace(" ","+")
query = "https://search.prtl.co/2018-07-23/?q=en-283%7Ckw-" + query + "%7Clv-master%7Cmh-face2face%7Ctc-EUR" 

#r = request.urlopen(query)

r = requests.get(query)
fee = r.json()[0]["tuition_fee"]
feeval= fee["value"]
feefreq = fee["unit"]
feecurr = fee["currency"]

print(str(feeval) + " " + feecurr + " / " + feefreq)
