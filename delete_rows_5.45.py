import os
import pandas as pd
from datetime import datetime

def find_excel_files(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xlsx") and "Tüm Yönler.xlsx" in file:
                file_path = os.path.join(root, file)
                paths.append(file_path)
    return paths

def delete_rows_below_time(file_path, time_threshold="05:45"):
    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Ensure 'Saat' column is treated as string and strip spaces
        df['Saat'] = df['Saat'].astype(str).str.strip()

        # Convert to datetime, coerce errors to NaT, and extract time
        df['Saat'] = pd.to_datetime(df['Saat'], format='%H:%M', errors='coerce').dt.time

        # Define the time threshold
        threshold_time = datetime.strptime(time_threshold, '%H:%M').time()

        # Filter rows where 'Saat' is greater than or equal to the threshold
        df_filtered = df[df['Saat'] >= threshold_time]

        # Save the filtered DataFrame back to the Excel file
        df_filtered.to_excel(file_path, index=False)
        print(f"Rows with 'Saat' less than {time_threshold} have been deleted from {file_path}.")
    except Exception as e:
        print(f"Error: {e}")
        print(f"The file {file_path} could not be processed.")

def process_directory(directory, time_threshold="05:45"):
    # Find all relevant Excel files in the directory
    excel_paths = find_excel_files(directory)

    # Process each Excel file
    for file_path in excel_paths:
        delete_rows_below_time(file_path, time_threshold)

# Example usage
directory = r"C:\\Users\\Lenovo\\Downloads\\Konya Kavşak Sayım Verileri\\Konya Kavşak Sayım Verileri\\Ata Petrol"
process_directory(directory, "05:45")
