import json

# File path and file modes
file_path = "python-basics/test.json"
read_mode = "r"
write_mode = "w"

# -----------------------------
# Read JSON file
# json.load() converts JSON data into a Python dictionary
# -----------------------------
print("Initial file content:")

with open(file_path, read_mode) as f:
    file_obj = json.load(f)
    print(file_obj)

# -----------------------------
# New data to save into the JSON file
# -----------------------------
dump_obj = {
    "first_name": "ashrith",
    "read_mode": "write",
    "is_valid": True
}

# -----------------------------
# Write data to JSON file
# json.dump() writes a Python dictionary into a JSON file
# indent=4 makes the JSON easy to read
# -----------------------------
print("Writing new data...")

with open(file_path, write_mode) as f:
    json.dump(dump_obj, f, indent=4)

# -----------------------------
# Read the updated JSON file
# -----------------------------
print("Updated file content:")

with open(file_path, read_mode) as f:
    file_obj = json.load(f)
    print(file_obj)
