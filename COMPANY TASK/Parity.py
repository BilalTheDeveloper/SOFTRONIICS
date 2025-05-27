arr = [3, 1, 2, 4]  

left, right = 0, len(arr) - 1

while left < right:
    if arr[left] % 2 == 0:  
        left += 1
    elif arr[right] % 2 != 0:  
        right -= 1
    else:
        arr[left], arr[right] = arr[right], arr[left]  
        left += 1
        right -= 1

print(arr)
