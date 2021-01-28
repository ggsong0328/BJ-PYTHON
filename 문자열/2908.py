import string

nums = input().split()
f_nums = nums[0]
s_nums = nums[1]

tmp = f_nums[0]
f_nums = f_nums[-1] + f_nums[1:]
f_nums = f_nums[0:2] + tmp

tmp = s_nums[0]
s_nums = s_nums[-1] + s_nums[1:]
s_nums = s_nums[0:2] + tmp

if int(f_nums) > int(s_nums):
    result = f_nums
else:
    result = s_nums

print(result)
