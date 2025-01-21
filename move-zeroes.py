nums = [0,0,1]
#max length
n = len(nums)

not_zero_index = 0

for i in range(n):
      if nums[i] != 0:
          nums[not_zero_index] = nums[i]
          not_zero_index+=1

for x in range(not_zero_index, n):
      nums[x] = 0

print(nums)
