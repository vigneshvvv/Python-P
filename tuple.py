fruits = ("apple", "mango")

# fruits[1] = "orange"

temp_list = list(fruits)
temp_list[1] = "orange"

fruits = tuple(temp_list)
print(fruits)

fruits = fruits + ("cherry",)

print(fruits)

del fruits
