client = {"name": "Jose Manuel", "age": 20}
print(type(client))
print(client)
print(client["name"])

everything = {"name": "Jose Manuel", "age": 20, "address": {"city": "San Francisco", "state": "CA"}}
print(everything["address"])
print(everything["address"]["city"])

dictionary = {"firstKey": ["a", "b", "c"], "secondKey": ["d", "e", "f"]}
print(dictionary["secondKey"][1].upper())

dictionary["thirdKey"] = "g"
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
