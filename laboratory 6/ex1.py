# 1.
# Create a Python script that does the following:
# Takes a directory path and a file extension as command line arguments (use sys.argv).
# Searches for all files with the given extension in the specified directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.

import sys
import os

if len(sys.argv) != 3:
    print("Correct format: python ex1.py <directory_path> <file_extension>")
    sys.exit(1)

directory_path = sys.argv[1]
file_extension = sys.argv[2]

try:
    if not os.path.exists(directory_path):
        raise Exception(f"Directory not found: {directory_path}")

    if not file_extension.startswith('.'):
        raise Exception("File extension should start with . (eg: \".txt\")")

    # os.listdir → returns a list of child files and folders
    for filename in os.listdir(directory_path):
        root, ext = os.path.splitext(filename)

        if ext == file_extension:
            file_path = os.path.join(directory_path, filename)

            try:
                with open(file_path, 'r') as file:
                    print(f"Contents of file {filename}:")
                    for line in file:
                        print(line.strip())
                    print("-" * 60)

            except Exception as e:
                print(f"Error reading file {filename}: {e}")

except Exception as e:
    print(f"Error: {e}")
