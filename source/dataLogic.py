import pandas as pd
import os
import source.bareBone as bb
from datetime import date
from datetime import datetime

class DataHandler:
    def __init__(self):
        """
        Initializes the DataHandler class.
        Loads existing data if available; otherwise, creates an empty DataFrame.
        """
        self.file_path = "data/wishes.csv"
        
        if os.path.exists(self.file_path):
            self.data = pd.read_csv(self.file_path)
        else:
            self.data = pd.DataFrame(columns=['Date', 'Wish', 'Status'])

    def add_entry(self, entry: dict) -> None:
        """
        Adds a new entry to the DataFrame.
        
        Args:
            entry (dict): Dictionary containing 'Date', 'Wish', and 'Status'.
        """
        new_row = pd.DataFrame([entry])  # Convert dict to DataFrame
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def save_to_csv(self) -> None:
        """
        Saves the current DataFrame to a CSV file.
        Creates the directory if it does not exist.
        """
        if not os.path.exists('data'):
            os.makedirs('data')
        
        self.data.to_csv(self.file_path, index=False)
    
    def review_item(self, desiredItem_key: str) -> str:
        dateRec = self.data.loc[self.data['Wish'] == desiredItem_key, 'Date'].values[0]
        days = (date.today() - datetime.strptime(str(dateRec), "%Y-%m-%d").date()).days
        if days > 29:
            questionScore = bb.AskSession()
            status_value = bb.Conclusion(questionScore)
            self.update_status(desiredItem_key, status_value)
            self.save_to_csv()
        else:
            if days == 1:
                show = f"It's been {days} day only. Please wait for at-least 30 days."
                print("It's been",days,"day only. Please wait for at-least 30 days.")
            else:
                show = f"It's been {days} days only. Please wait for at-least 30 days."
                print(f"It's been {days} days only. Please wait for at-least 30 days.")
            return show

    def update_status(self, wish: str, status: str) -> None:
        """
        Updates the status of a wish in the DataFrame.
        
        Args:
            wish (str): The wish to update.
            status (str): The new status to be set.
        """
        self.data.loc[self.data['Wish'] == wish, 'Status'] = status