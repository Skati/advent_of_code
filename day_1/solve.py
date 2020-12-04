input_file = 'input.txt'
input = []
with open(input_file) as f:
    for line in f:
        input.append(int(line.replace('\n', '')))

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i]*nums[j]
print(twoSum(input,2020))
