arr = [3, 2, 5, 10, 7]  
if not arr:
    print(0)
elif len(arr) == 1:
    print(arr[0])
else:
    incl = arr[0]
    excl = 0

    for i in range(1, len(arr)):
        new_incl = excl + arr[i]
        excl = max(incl, excl)
        incl = new_incl

    print(max(incl, excl))
