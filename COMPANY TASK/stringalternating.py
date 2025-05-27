binary_string = "010101"  

pattern1 = "".join('0' if i % 2 == 0 else '1' for i in range(len(binary_string)))
pattern2 = "".join('1' if i % 2 == 0 else '0' for i in range(len(binary_string)))

flips_to_pattern1 = sum(1 for i in range(len(binary_string)) if binary_string[i] != pattern1[i])
flips_to_pattern2 = sum(1 for i in range(len(binary_string)) if binary_string[i] != pattern2[i])

max_flips = max(flips_to_pattern1, flips_to_pattern2)

print(max_flips)

