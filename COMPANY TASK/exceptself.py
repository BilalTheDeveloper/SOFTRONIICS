arr = [1, 2, 3, 4] 

n = len(arr)
result = [1] * n

left_prod = 1
for i in range(n):
    result[i] = left_prod
    left_prod *= arr[i]

right_prod = 1
for i in range(n - 1, -1, -1):
    result[i] *= right_prod
    right_prod *= arr[i]

print(result)
