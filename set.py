s = {1,2,3}
s.add(2)

print(s)

s.remove(2)
print(s)

# s.remove(4)

s.discard(4)

x = s.pop()
print(x)

print(len(s))

print(3 in s)

if(3 in s):
    print("Number present")
else:
    print("Number doesn't exist")    