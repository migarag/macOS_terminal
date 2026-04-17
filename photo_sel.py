import os
import shutil

# Step 1: Set the paths
#master_folder = 'path/to/master_folder'  # Path to the master folder
master_folder = '/Users/migaragunawansha/Pictures/24JUL24 SUGR_B Exports'  # Path to the master folder
selected_folder = os.path.join(master_folder, 'Selected')  # New folder to store selected files

# Create 'Selected' folder if it doesn't exist
if not os.path.exists(selected_folder):
    os.makedirs(selected_folder)

# Step 2: Read the 'sel_files.txt' file to get selected filenames
with open(os.path.join(master_folder, 'sel_files.txt'), 'r') as f:
    selected_files = f.read().split(',')

# Strip whitespace and ensure filenames are clean
selected_files = [filename.strip() for filename in selected_files]

# Step 3: Search for matching files in the master folder and subfolders
for root, dirs, files in os.walk(master_folder):
    for file in files:
        if file in selected_files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(selected_folder, file)
            
            # Copy the file to the 'Selected' folder
            shutil.copy(source_path, destination_path)
            print(f'Copied {file} to {selected_folder}')

print("File search and copy completed.")
