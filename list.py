nums = [10,20,30,40,50]

# x = nums[0]*2

print(nums[0])
print(nums[4])
# print(nums[5])
print(len(nums))

nums[1] = 15
print(nums)

nums[1:3] = [50,60]
print(nums)

nums.append(60)
print(nums)

nums.extend([70,80,90])
print(nums)

nums.insert(1,20)
print(nums)

nums.remove(50)
print(nums)

nums.pop()
print(nums)

# nums.clear()
# print(nums)

# for x in nums:
#     print(x*2)

present = False

for x in nums:
    if(x == 100):
        present = True

if present:
    print("number present")
else:
    print("There is no such number")  