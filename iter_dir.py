import os
import pandas as pd

def find_excel_files(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "Tüm yönler.xlsx":
                file_path = os.path.join(root, file)
                paths.append(file_path)
    return paths

def process_excel_files(paths, location_number):
    timestep = 0
    result_df = pd.DataFrame(columns=["timestep", "location", "flow", "occupy", "speed"])
    for file_path in paths:
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                timestep += 1
                flow = row["Toplam Araç Sayısı"]
                result_df = result_df.append({"timestep": timestep, "location": location_number, "flow": flow, "occupy": 1, "speed": 1}, ignore_index=True)
            print("Excel dosyası bulundu ve okundu:", file_path)
        except Exception as e:
            print(f"Hata: {e}")
            print(f"{file_path} dosyası okunamadı veya işlenemedi.")
    return result_df

def save_to_csv(df, csv_file):
    try:
        df.to_csv(csv_file, index=False)
        print(f"Veriler '{csv_file}' dosyasına kaydedildi.")
    except Exception as e:
        print(f"Hata: {e}")
        print("Veriler CSV dosyasına kaydedilemedi.")

def main(directories_and_files):
    for location_number, (starting_directory, csv_file) in enumerate(directories_and_files, start=1):
        print(f"Processing directory: {starting_directory}")
        
        # Find Excel files
        excel_paths = find_excel_files(starting_directory)
        
        # Process Excel files
        result_df = process_excel_files(excel_paths, location_number)
        
        # Save to CSV
        save_to_csv(result_df, csv_file)

if __name__ == "__main__":
    directories_and_files = [
         (r"C:\\Users\\Lenovo\Downloads\\Konya Kavşak Sayım Verileri\\Konya Kavşak Sayım Verileri\\Ata Petrol", "ata_petrol.csv"),
        (r"C:\\Users\\Lenovo\Downloads\\Konya Kavşak Sayım Verileri\\Konya Kavşak Sayım Verileri\\Hakimiyet Kavşağı", "hakimiyet.csv"),
        (r"C:\\Users\\Lenovo\Downloads\\Konya Kavşak Sayım Verileri\\Konya Kavşak Sayım Verileri\\İstasyonKavşağı", "istasyon_kavşağı.csv")
    ]
    
    main(directories_and_files)
