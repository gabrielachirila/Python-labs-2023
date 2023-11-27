# 4.
# Write a Python script that counts the number of files with each extension in a given directory. The script
# should: Accept a directory path as a command line argument (using sys.argv). Use the os module to list all files in
# the directory. Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# Include error handling for scenarios such as the directory not being found, no read permissions, or the directory
# being empty.

import os
import sys

if len(sys.argv) != 2:
    print("Correct format: python ex4.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

try:
    if not os.path.exists(directory_path):
        raise Exception(f"Directory not found: {directory_path}")

    if not os.listdir(directory_path):
        raise Exception(f"Directory is empty: {directory_path}")

    count_extensions = {}

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            root, extension = os.path.splitext(filename)

            if extension in count_extensions:
                count_extensions[extension] += 1
            else:
                count_extensions[extension] = 1

    print("The number of files with each extension:")
    for extension, count in count_extensions.items():
        print(f"{count} file/s with extension: {extension}")

except FileNotFoundError as e:
    print(f"Error: {e}")

except PermissionError as e:
    print(f"Permission error: {e}")

except Exception as e:
    print(f"Error: {e}")

