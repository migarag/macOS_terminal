import os
import shutil

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Count for how many files are sorted
count = 0

# Ensure the folder exists
if not os.path.exists(downloads_folder):
    print(f"Folder {downloads_folder} does not exist.")
else:
    # Iterate over each file in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Extract the file extension (if any)
        _, file_extension = os.path.splitext(filename)

        # Skip files without extensions
        if not file_extension:
            continue

        # Create a folder based on the file extension
        folder_name = file_extension[1:].upper() + " Files"
        destination_folder = os.path.join(downloads_folder, folder_name)

        # If the folder doesn't exist, create it
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the file to the corresponding folder
        shutil.move(file_path, os.path.join(destination_folder, filename))
        count = count + 1

    print(count, "Files sorted by type.")
