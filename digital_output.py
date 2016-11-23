nums = int(input("input some number: "))
count = divmod(nums, 10)
output = []
while count[0] != 0:
    output.append(count[1])
    nums = count[0]
    count = divmod(nums, 10)
output.append(count[1])
print(*output[::-1], sep='\n')
