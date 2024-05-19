import pandas as pd
import os

def combine_csv_files(csv_files, combined_csv_file):
    combined_df = pd.DataFrame(columns=["timestep", "location", "flow", "occupy", "speed"])

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            print(f"Hata: {e}")
            print(f"{csv_file} dosyası okunamadı veya işlenemedi.")

    # Sort the combined dataframe by timestep
    combined_df = combined_df.sort_values(by=["timestep", "location"]).reset_index(drop=True)

    # Save the combined dataframe to a new CSV file
    try:
        combined_df.to_csv(combined_csv_file, index=False)
        print(f"Veriler '{combined_csv_file}' dosyasına kaydedildi.")
    except Exception as e:
        print(f"Hata: {e}")
        print("Veriler CSV dosyasına kaydedilemedi.")

if __name__ == "__main__":
    # List of CSV files to combine
    csv_files = [
        "ata_petrol.csv",
        "hakimiyet.csv",
        "istasyon_kavşağı.csv"
    ]
    
    # Output CSV file
    combined_csv_file = "Konya_Kavşak.csv"
    
    # Combine the CSV files
    combine_csv_files(csv_files, combined_csv_file)
