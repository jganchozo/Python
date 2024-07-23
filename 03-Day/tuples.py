client = "Jose", "Manuel"
print(type(client))
print(client)

numbers = (1, 2, 3, 4)
print(numbers)

varies = (1, "Jose Manuel", 9.0, (10, 20))
print(varies)

print(client[-1])

# client[0] = 9

print(varies[3])
print(varies[3][0])

customer = list(varies)
print(type(customer))
print(customer)

customer = tuple(varies)
print(type(customer))
print(customer)

values = (1, 2, 3)
x, y, z = values
print(x)
print(y)
print(z)

values = (1, 2, 3, 1, 2, 1)
print(len(values))
print(values.count(1))
print(values.index(2))
