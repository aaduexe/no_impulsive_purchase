from datetime import date

def newItem() -> dict:
    """
    Prompts the user to input an item they wish to buy.
    Returns a dictionary containing the item's details with the current date.
    """
    item = input("What item are you looking to buy?\n")
    new_row = {
        'Date' : date.today(),
        'Wish' : item,
        'Status' : 'waiting'
    }
    return new_row