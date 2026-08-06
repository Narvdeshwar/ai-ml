import json
file_path="python-basics/test.json"
read_mode="r"
# for reading the json file we use the json.load() after reading the file
with open(file_path,read_mode) as f:
    file_obj=json.load(f)
    print(file_obj)
