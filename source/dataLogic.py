import pandas as pd

class DataHandler:
    def __init__(self): # As of now, the app needs to load data everytime so--
        try: # If data already exists, then the data will be loaded.
            self.data = pd.read_csv("data.csv")
        except: # otherwise, the dataframe will be created. !It does not export the data.
            self.data = pd.DataFrame(columns=['date', 'item', 'status', 'score'])

    def dataUpdate(self, dict):
        dict = pd.DataFrame([dict]) #conver the python dict to dataframe first
        self.data = pd.concat([self.data, dict], ignore_index= True) #concat new row to the actual dataframe
    
    def saveData(self): # data exporting function, when the user decided to save, or have completed the question and new score is acquired:
        self.data.to_csv("data.csv", index= False)
        # it does not need to return anything, only parameter needed is to give it the dataframe.