arr = [1, 3, 6, 10]  

unique_diffs = set()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        diff = abs(arr[i] - arr[j])
        unique_diffs.add(diff)

print(len(unique_diffs))
