#Imports
from types import new_class
import requests as r
import urllib.request as url
import urllib.parse
import json

#Main

def inventory(steamid, usejson = False) :
    #Get inventory
    
    if usejson :
        with open('inventory.json', 'r') as f :
            inv = json.load(f)

    else :
        inv = r.get("https://steamcommunity.com/profiles/" + steamid + "/inventory/json/730/2").json()

        #Creates a Json file
        with open('inventory.json', 'w') as f :
            json.dump(inv, f)

    return(inv)

def itemprice(inv) :

    total = {}

    for item in inv["rgDescriptions"] :
        #Check if marketable
        if inv["rgDescriptions"][item]["marketable"] == True :
            name = urllib.parse.quote(inv["rgDescriptions"][item]["market_hash_name"])
            data = url.urlopen("https://steamcommunity.com/market/priceoverview/?appid=" + inv["rgDescriptions"][item]["appid"] + "&currency=3&market_hash_name=" + name)
            info = json.loads(data.read())

            try :
                price = info["lowest_price"]
            except KeyError :
                price = info["median_price"]

            total[inv["rgDescriptions"][item]["market_hash_name"]] = price
    
    return(total)

def total(prices) :

    total = 0

    for item in prices :

        newnumber = ""
        
        for number in prices[item] :
            number = number.replace(",", ".")
            if number.isdigit() == True or number == "." :
                newnumber += number 
                
        total += float(newnumber)
    
    return(total)

prices = itemprice(inventory('76561198292721634', True)) #76561198239631966
print(prices)
totalprices = total(prices)
print(totalprices)



