from dataLogic import DataHandler
from datetime import date

item = input("What item are you looking to buy?\n")
new_row = {
    'date' : date.today(),
    'item' : item,
    'status' : 'waiting'
}

dataFrame = DataHandler()
dataFrame.dataUpdate(new_row)
dataFrame.saveData()