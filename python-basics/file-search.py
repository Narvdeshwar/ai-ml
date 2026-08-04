file_path="python-basics/file-search.txt"

with open(file_path,"r") as f:
    data=f.readline()
    while data:
        if ("python" in data):
            print("Searched key found in file.")
            break
        data=f.readline()
    else:
        print("No keyword found in the file.")
