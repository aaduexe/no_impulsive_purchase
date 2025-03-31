import pandas as pd
import os

class DataHandler:
    def __init__(self): # As of now, the app needs to load data everytime so--
        try: # If data already exists, then the data will be loaded.
            self.data = pd.read_csv("data/wishes.csv")
        except: # otherwise, the dataframe will be created. !It does not export the data.
            self.data = pd.DataFrame(columns=['Date', 'Wish', 'Status'])

    def dataUpdate(self, dict: dict) -> None:
        dict = pd.DataFrame([dict]) #convert the python dict to dataframe first
        self.data = pd.concat([self.data, dict], ignore_index= True) #concat new row to the actual dataframe
    
    def saveData(self) -> None: # data exporting function, when the user decided to save, or have completed the question and new score is acquired:
        try: # Check if direcory exists
            os.makedirs('data')
        except:
            ...
        
        self.data.to_csv("data/wishes.csv", index= False)
        # it does not need to return anything, only parameter needed is to give it the dataframe.

    def statusUpdate(self, key: str, value: str) -> None:
        self.data.loc[self.data['Wish'] == key, ['Status']] = value

