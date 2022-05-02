"""IMPORTS"""

#URL
from urllib.error import HTTPError
import requests as r
import urllib.request as url
import urllib.parse

#Files
import json, csv
import time
from datetime import datetime


"""FUNCTIONS"""


#Get Inventory
def inventory(steamid, usejson = False) :
    
    if usejson != False :
        with open('history/' + usejson + '.json', 'r') as f :
            inv = json.load(f)

    else :
        inv = r.get("https://steamcommunity.com/profiles/" + steamid + "/inventory/json/730/2").json()

        #Creates a Json file
        date = str(datetime.now())
        file = date[:date.find(" ")]
        with open('history/' + file + '.json', 'w') as f :
            json.dump(inv, f)

    return(inv)


#Get Item Prices
def itemprice(inv) :

    total = {}

    for item in inv["rgDescriptions"] :
        #Check if marketable
        if inv["rgDescriptions"][item]["marketable"] == True :
            try :
                name = urllib.parse.quote(inv["rgDescriptions"][item]["market_hash_name"])
                data = url.urlopen("https://steamcommunity.com/market/priceoverview/?appid=" + inv["rgDescriptions"][item]["appid"] + "&currency=3&market_hash_name=" + name)
                info = json.loads(data.read())
            except HTTPError :
                time.sleep(.5)

            try :
                price = info["lowest_price"]
            except KeyError :
                price = info["median_price"]

            total[inv["rgDescriptions"][item]["market_hash_name"]] = price
            
    return(total)


#Calculate Total
def total(prices) :

    total = 0

    for item in prices :

        newnumber = ""
        
        for number in prices[item] :
            number = number.replace(",", ".")
            if number.isdigit() == True or number == "." :
                newnumber += number 
                
        total += float(newnumber)
    
    #Creates a CVS file
    date = str(datetime.now())
    file = date[:date.find(" ")]
    prices.update({"Total" : str(total) + "€" })
    with open('history/' + file + '.csv', 'w', encoding = "UTF8") as f :
        writer = csv.writer(f)
        writer.writerow(prices.keys())
        writer.writerow(prices.values())

    return(total, prices)