import os

folder_path = 'C:/Personal/Baby shower/New folder'
output_file_path = 'C:/Personal/Baby shower/New folder/file.txt'

# Get all file names in the folder
file_names = os.listdir(folder_path)

# Write file names to a text file
with open(output_file_path, 'w') as output_file:
    for file_name in file_names:
        output_file.write(file_name + '\n')

print(f"File names have been written to {output_file_path}")
