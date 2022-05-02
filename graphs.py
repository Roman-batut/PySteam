"""IMPORTS"""

#Graphs
import matplotlib.pyplot as plt

#Files
import time
from datetime import datetime

"""FUNCTIONS"""

#Table
def table(dic) :
    #Variables
    data = [] ; columns = ["Item", "Price"]
    celColors = [] ; colColors = []
    keys = list(dic.keys()) ; values = list(dic.values())
    date = str(datetime.now()) ; file = date[:date.find(" ")]

    #List Comprehension
    [data.append([keys[i], values[i]]) for i in range(len(keys))]
    #[celColors.append([["#1e1e1e", "w", "w", "w", "w"],["#1e1e1e", "w", "w", "w", "w"]]) for j in range(len(data))]
    #[colColors.append(["#333333"]) for k in range(len(columns))]

    #Table
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis("tight") ; ax.axis("off")
    ax.table(cellText = data, colLabels = columns, loc = "center")
    fig.tight_layout()
    
    #Save
    plt.savefig("history/" + file + "_table.png", transparent = True)

#Piechart
def piechart(dic, total) :
    #Variables
    data =[]
    keys = list(dic.keys()) ; values = list(dic.values())
    date = str(datetime.now()) ; file = date[:date.find(" ")]

    #List Comprehension
    [(data.append(float((values[i][:int(values[i].find("€"))])[:(values[i][:int(values[i].find("€"))]).find(",")] + "." + (values[i][:int(values[i].find("€"))])[(values[i][:int(values[i].find("€"))]).find(",")+1:]))) for i in range(len(keys))]

    #Piechart
    fig, ax = plt.subplots()
    ax.pie(data, labels = keys, autopct = "%1.1f%%")
    ax.set_title("Total : " + str(total))
    #fig.tight_layout()
    
    #Save
    plt.savefig("history/" + file + "_piechart.png", transparent = True)


