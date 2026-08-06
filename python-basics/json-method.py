import json
file_path="python-basics/test.json"
read_mode="r"
write_mode="w"
# for reading the json file we use the json.load() after reading the file
print("Intial first file read mode with inital value")
with open(file_path,read_mode) as f:
    file_obj=json.load(f)
    print(file_obj)

print("dumping the value")
dump_obj={"first_name":"ashrith","read_mode":"write","is_valid":True}
with open(file_path,write_mode) as f:
    json.dump(dump_obj,f)

# print("Value dumped now new write value")
# with open(file_path,read_mode) as f:
#     file_obj=json.load(f)
#     print(file_obj)
