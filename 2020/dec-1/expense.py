file = open('input.txt', 'r')

nums = []
for line in file.readlines():
    nums.append(int(line.strip()))

# Part 1
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j])

# Part 2
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(len(nums)):
            if k != i and k != j and (nums[i] + nums[j] + nums[k]) == 2020:
                print(nums[i]*nums[j]*nums[k])