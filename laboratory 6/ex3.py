# 3.
# Create a Python script that calculates the total size of all files in a directory provided as a command line
# argument. The script should: Use the sys module to read the directory path from the command line. Utilize the os
# module to iterate through all the files in the given directory and its subdirectories. Sum up the sizes of all
# files and display the total size in bytes. Implement exception handling for cases like the directory not existing,
# permission errors, or other file access issues.

import os
import sys

if len(sys.argv) != 2:
    print("Correct format: python ex3.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

try:
    if not os.path.exists(directory_path):
        raise Exception(f"Directory not found: {directory_path}")

    total_size = 0

    for root, directories, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                total_size += os.path.getsize(file_path)

            except Exception as e:
                print(f"Error accessing file {file_path}: {e}")

    print(f"The total size of all files in {directory_path} is: {total_size} bytes")

except FileNotFoundError as e:
    print(f"Error: {e}")

except PermissionError as e:
    print(f"Permission error: {e}")

except Exception as e:
    print(f"Error: {e}")

