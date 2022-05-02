"""IMPORTS"""

#Internal
import functions as f
import graphs as g

#GUI
import tkinter as tk
import json

#76561198239631966
"""GUI"""


#Root
root = tk.Tk()
root.title("PySteam") ; root.iconbitmap("assets/icon.ico")
root.geometry("500x500")

#Functions
def confirmation() :
    steamID = entry.get()
    if len(steamID) == 17 and steamID.isdigit() == True :
        #Graphs
        try :
            inv = f.inventory(steamID)
            priceDic = f.itemprice(inv)
            prices = priceDic.copy()
            total, priceDicTotal = f.total(priceDic)
            g.table(priceDicTotal) ; g.piechart(prices, total)
            #Delete
            error.place_forget()
        
        except json.decoder.JSONDecodeError :
            #Error Text
            error.place(relwidth = 0.4, relheight = 0.05, relx = 0.25, rely = 0.35)
            #Delete
            entry.delete(0, tk.END)
        
    else : 
        #Error Text
        error.place(relwidth = 0.4, relheight = 0.05, relx = 0.25, rely = 0.35)
        #Delete
        entry.delete(0, tk.END)


#Background
background = tk.Frame(root, bg = "#1e1e1e")
background.place(relwidth = 1, relheight = 1)

#Frame
upFrame = tk.Frame(root, bg = "#252526") 
downFrame = tk.Frame(root, bg = "#333333") ; rightFrame = tk.Frame(root, bg = "#333333") ; leftFrame = tk.Frame(root, bg = "#333333")

upFrame.place(relwidth = 1, relheight = 0.15, relx = 0, rely = 0)
downFrame.place(relwidth = 1, relheight = 0.05, relx = 0, rely = 0.95)
rightFrame.place(relwidth = 0.05, relheight = 0.85, relx = 0.95, rely = 0.15)
leftFrame.place(relwidth = 0.05, relheight = 0.85, relx = 0, rely = 0.15)

#Title
title = tk.Label(root, text = "Py$team", fg = "#858585", bg = "#252526")
title.config(font = ('Helvetica bold',40))
title.place(relwidth = 0.6, relheight = 0.1, relx = 0.2, rely = 0.025)

#Instruction
instruction = tk.Label(root, text = "Enter SteamID", fg = "#858585", bg = "#1e1e1e")
instruction.config(font = ('Helvetica bold', 10))
instruction.place(relwidth = 0.2, relheight = 0.1, relx = 0.15, rely = 0.2)

#Entry
entry = tk.Entry(root, fg = "#858585", bg = "#333333")
entry.place(relwidth = 0.6, relheight = 0.05, relx = 0.15, rely = 0.3)

#Confirmation Button
button = tk.Button(root, text = "Confirm", bg = "#333333", fg = "#858585", command = confirmation)
button.place(relwidth = 0.1, relheight = 0.05, relx = 0.75, rely = 0.3)

#Errors
error = tk.Label(root, text = "Incorrect SteamID, please retry", fg = "#d74a1d", bg = "#1e1e1e")
error.config(font = ('Helvetica bold',10))


#Deletes


root.mainloop()







#MULTITHREADING
