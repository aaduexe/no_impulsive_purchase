from dataLogic import DataHandler
from userInput import newItem
import bareBone as bb
from datetime import date
from datetime import datetime

# Figure out this mess on your own. It's pretty basic

while True:
    table = DataHandler()
    initialization = input("Do you want to add new item or revisit item from the list?\nInput 'A' to Add Item | Input 'R' to Revisit item | Input 'Q' to Quit\n")
    if initialization.lower() == 'a':
        newWish = newItem()
        table.add_entry(newWish)
        table.save_to_csv()
        userInput1 = input(" Your item is added.\nInput 'R' to Re-run the prompts | Input 'Q' to Quit\n")
        if userInput1.lower() == 'r':
            pass
        elif userInput1.lower() == 'q':
            break
        else:
            print('Your item was succesfully added. No valid input, prompts restarted.')
    elif initialization.lower() == 'r':
        print(table.data)
        desiredItem_key = input("Type name of item you want to buy.\n")

        dateRec = table.data.loc[table.data['Wish'] == desiredItem_key, 'Date'].values[0]
        days = (date.today() - datetime.strptime(str(dateRec), "%Y-%m-%d").date()).days

        if days > 29:
            questionScore = bb.AskSession()
            status_value = bb.Conclusion(questionScore)
            table.update_status(desiredItem_key, status_value)
            table.save_to_csv()
            print("The status of",desiredItem_key,"is updated to",status_value,"as per the answers.")
        else:
            if days == 1:
                print("It's been",days,"day only. Please wait for at-least 30 days.")
            else:
                print("It's been",days,"days only. Please wait for at-least 30 days.")
    elif initialization.lower() == 'q':
        break
    else:
        print('No valid input recognized')