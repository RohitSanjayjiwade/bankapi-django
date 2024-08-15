from django.core.management.base import BaseCommand
from bank.models import Branch  # Ensure the correct model import
import pandas as pd

class Command(BaseCommand):
    help = 'Populates Branch model from a CSV file'

    def handle(self, *args, **kwargs):
        print("Starting the data processing...")

        # Specify the path to your CSV file
        csv_file_path = '/home/vaibhav/Desktop/bank_branches.csv'

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
        ifscCode = row.get('ifsc', '')
        branchName = row.get('branch', '')
        address = row.get('address', '')
        cityName = row.get('city', '')
        districtName = row.get('district', '')
        stateName = row.get('state', '')
        bankId = row.get('bank_id', '')

        try:
            # Create a new Branch instance
            Branch.objects.create(
                ifsc=ifscCode,
                branch=branchName,
                address=address,
                city=cityName,
                district=districtName,
                state=stateName,
                bank_id_id=bankId
            )
        except Exception as e:
            print(f"Error processing row: {row}")
            print(f"Error details: {e}")
