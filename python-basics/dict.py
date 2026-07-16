dict={
    "name":"ashrith",
    "age":34,
    "":12
}
print(dict)

# dictionary are mutable and unordered.
all_keys=dict.keys()
print(f"All keys of dict {all_keys}")

all_values=dict.values()
print(f"All values of dict {all_values}")

# print(dict.items())
print(f"key value pair print {dict.items()}")

print(dict.get("age"))

print(dict.update({"fnae":"ravi"}))
print(dict)
