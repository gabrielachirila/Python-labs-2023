# 2
# Write a script using the os module that renames all files in a specified directory to have a sequential number
# prefix. For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or
# files that can't be renamed.

import os
import sys

if len(sys.argv) != 2:
    print("Correct format: python ex4.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

try:
    if not os.path.exists(directory_path):
        raise Exception(f"Directory not found: {directory_path}")

    files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

    counter = 1

    for filename in files:
        root, ext = os.path.splitext(filename)
        new_filename = f"{root}{counter}{ext}"
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"{filename} renamed -> {new_filename}")

        except Exception as e:
            print(f"Error renaming file {filename}: {e}")

        counter += 1


except FileNotFoundError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error: {e}")
