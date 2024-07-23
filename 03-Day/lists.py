lista = ["a", "b", "c"]
print(type(lista))
print(lista)

newList = ["Hello", 99, 9.0]
print(newList)

print(len(lista))
print(lista[0:2])

lists = ["d", "e", "f"]
together = lista + lists
print(together)

# together[0] = "alpha"
print(together)

together.append("g")
print(together)

together.pop()
print(together)

deleted = together.pop(0)
print(together)
print(deleted)

unordered = ["z", "g", "e", "m", "n", "f", "b", "a", "a"]
unordered.sort()
print(unordered)

# data = unordered.reverse()
# print(type(data))
# reverse = unordered[::-1]

unordered.reverse()
print(unordered)
