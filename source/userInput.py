from datetime import date

def newItem() -> dict:
    item = input("What item are you looking to buy?\n")
    new_row = {
        'Date' : date.today(),
        'Wish' : item,
        'Status' : 'waiting'
    }
    return new_row
