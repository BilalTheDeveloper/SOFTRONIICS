arr = [1, 2, 1, 3, 4, 2, 3]  
k = 4  

freq = {}
distinct_counts = []

for i in range(k):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

distinct_counts.append(len(freq))

for i in range(k, len(arr)):
    if freq[arr[i - k]] == 1:
        del freq[arr[i - k]]
    else:
        freq[arr[i - k]] -= 1

    freq[arr[i]] = freq.get(arr[i], 0) + 1

    distinct_counts.append(len(freq))

print(distinct_counts)
