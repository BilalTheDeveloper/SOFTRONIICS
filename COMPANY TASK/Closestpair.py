arr = [8,1,4,10 ]

arr.sort()
diff_pairs = {}

for i in range(len(arr) - 1):
    diff = arr[i+1] - arr[i]
    if diff not in diff_pairs:
        diff_pairs[diff] = []
    diff_pairs[diff].append([arr[i], arr[i+1]])

sorted_diffs = sorted(diff_pairs.keys())

if len(sorted_diffs) >= 2:
    result = diff_pairs[sorted_diffs[1]] 
else:
    result = []

print(result)
