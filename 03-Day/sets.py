sets = {1, 2, 3, 4, 5, 6, 7, 9, 1, 1, 2, 9, (9, 2)}
print(sets)
print(len(sets))
print(type(sets))
print(9 in sets)

addition = {"a", "b", "c"}
together = sets.union(addition)
print(together)

sets.add("Jose Manuel")
print(sets)

addition.remove("c")
print(addition)

addition.discard("b")
print(addition)

lottery = {0, 1, 2, 3}
deleted = lottery.pop()
print(deleted)
print(lottery)

lottery.clear()
print(lottery)

giveaways = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
delete = giveaways.pop()
print(delete)
print(giveaways)

# newSet = set([1, 2, 3, 4, 5])
# print(newSet)
