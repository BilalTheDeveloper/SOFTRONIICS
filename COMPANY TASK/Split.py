arr = [1, 2, 3, 4, 5, 5]  
num_subarrays = 2 

total_sum = sum(arr)

if total_sum % num_subarrays != 0:
    print(False)
else:
    target = total_sum // num_subarrays
    arr.sort(reverse=True)  

    subarrays = [0] * num_subarrays

    def can_partition(i):
        if i == len(arr): 
            return len(set(subarrays)) == 1 
        for j in range(num_subarrays):
            if subarrays[j] + arr[i] <= target:
                subarrays[j] += arr[i]
                if can_partition(i + 1):
                    return True
                subarrays[j] -= arr[i]
            if subarrays[j] == 0:  
                break
        return False

    result = can_partition(0)
    print(result)
