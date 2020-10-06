import xml.etree.ElementTree as ET
import requests
import bs4
from bs4 import BeautifulSoup

counter = 0

def parsePrice():
    r = requests.get("https://finance.yahoo.com/quote/CL=F?p=CL=F")
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    price = soup.find("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
    global counter
    counter += 1
    return price

while True:
    print("#"+str(counter), "The current price of crude oil is: $"+ str(parsePrice()))







