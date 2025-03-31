from datetime import date

def newItem():
    item = input("What item are you looking to buy?\n")
    new_row = {
        'date' : date.today(),
        'wish' : item,
        'status' : 'waiting'
    }
    return new_row
