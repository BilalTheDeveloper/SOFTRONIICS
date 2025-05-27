nums = [-10, -10, 5, 2]  

nums.sort()

option1 = nums[-1] * nums[-2] * nums[-3]  
option2 = nums[0] * nums[1] * nums[-1]    

print(max(option1, option2))
