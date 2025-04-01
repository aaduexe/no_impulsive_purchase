import pandas as pd
import os

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

    def update_status(self, wish: str, status: str) -> None:
        """
        Updates the status of a wish in the DataFrame.
        
        Args:
            wish (str): The wish to update.
            status (str): The new status to be set.
        """
        self.data.loc[self.data['Wish'] == wish, 'Status'] = status
