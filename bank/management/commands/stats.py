from django.core.management.base import BaseCommand
from bank.models import Bank  # Ensure the correct model import
import pandas as pd

class Command(BaseCommand):
    help = 'Populates Branch model from a CSV file'

    def handle(self, *args, **kwargs):
        print("Starting the data processing...")

        # Specify the path to your CSV file
        csv_file_path = '/home/vaibhav/Desktop/indian_banks.csv'

        # Read the CSV file into a DataFrame
        try:
            df = pd.read_csv(csv_file_path)
            print(f"CSV file loaded successfully with {len(df)} rows.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        # Process each row in the DataFrame
        for _, row in df.iterrows():
            self.process_row(row)

        print("Processing completed.")

    def process_row(self, row):
        # Extract data from the row
        name = row.get('name', '')
        id = row.get('id', '')

        try:
            # Create a new Branch instance
            Bank.objects.create(
                name=name,
                id=id
            )
        except Exception as e:
            print(f"Error processing row: {row}")
            print(f"Error details: {e}")
