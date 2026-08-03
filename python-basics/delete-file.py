import os

file_path = "python-basics/sample2.txt"

try:
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully!")
    else:
        print("File does not exist.")
except PermissionError:
    print("Permission denied: Cannot delete file.")
except Exception as e:
    print(f"An error occurred: {e}")
