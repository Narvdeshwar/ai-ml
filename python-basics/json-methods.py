import json

# JSON data in string format
json_data = '{"name":"Ashrith","age":25,"is_valid":true}'

# -----------------------------------------
# json.loads()
# Converts a JSON string into a Python object
# Return type: dict, list, etc.
# -----------------------------------------
py_obj = json.loads(json_data)

print("Python Object:", py_obj)
print("Type after loads():", type(py_obj))   # <class 'dict'>


# -----------------------------------------
# json.dumps()
# Converts a Python object into a JSON string
# Return type: str
# -----------------------------------------
json_string = json.dumps(py_obj)

print("\nJSON String:", json_string)
print("Type after dumps():", type(json_string))   # <class 'str'>


# -----------------------------------------
# Pretty JSON using indent
# -----------------------------------------
pretty_json = json.dumps(py_obj, indent=4)

print("\nPretty JSON:")
print(pretty_json)
