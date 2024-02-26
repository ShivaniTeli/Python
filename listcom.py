list1 = ["apple", "banana", "1"]
list2 = []

for x in list1:
  if "a" in x:
    list2.append(x)

print(list2)
print(len(list2))
print(type(list2))