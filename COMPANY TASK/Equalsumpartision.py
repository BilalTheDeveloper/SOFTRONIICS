nums = [1, 5, 11, 5] 

total = sum(nums)

if total % 2 != 0:
    print(False)
else:
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    print(dp[target])
