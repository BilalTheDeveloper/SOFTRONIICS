arr = [1, 5, 7, -1, 5]  
k = 6

count = 0
freq = {}

for num in arr:
    complement = k - num
    if complement in freq:
        count += freq[complement]
    
    freq[num] = freq.get(num, 0) + 1

print(count)
