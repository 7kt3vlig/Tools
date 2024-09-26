import os
import csv

def count_tea_breaks_in_folder(folder_path):
    total_count = 0
    
    # Loop through all the CSV files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            
            # Open and read the CSV file
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                
                # Count occurrences of "Aux - Tea Break"
                file_count = sum(row.count("Aux - Tea Break") for row in reader)
                total_count += file_count
                
                print(f"{filename}: {file_count} occurrences")
    
    print(f"\nTotal count of 'Aux - Tea Break' in all files: {total_count}")

# Path to the folder containing your CSV files
folder_path = r'C:\Users\Jag\Desktop\Cristina2023'
  # Replace with the actual path to your folder

# Call the function
count_tea_breaks_in_folder(folder_path)