import os

folder_path = input("Enter the path of the folder: ")
new_name = input("Enter the new name for the files: ")

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Iterate through the list of files
for i, file in enumerate(files):
    # Get the file path
    file_path = os.path.join(folder_path, file)
    # Check if the file is a file and not a directory
    if os.path.isfile(file_path):
        # Get the file extension
        extension = os.path.splitext(file)[1]
        # Create the new file name
        new_file_name = f"{new_name}_{i}{extension}"
        # Get the new file path
        new_file_path = os.path.join(folder_path, new_file_name)
        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed {file} to {new_file_name}")