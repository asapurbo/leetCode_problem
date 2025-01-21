nums = [2,1,1]

major_count = 0
major_element = None

#length of the array
n = len(nums)

all_data = {}

for i in range(n):
      if all_data.get(nums[i]):
            all_data[nums[i]]+=1
      else:
            all_data[nums[i]] = 1

max_value = 0
major = 0
for key, value in all_data.items():
      if max_value < value:
            major = key
            max_value = value

if n // 2 <= max_value:
      print(major)
