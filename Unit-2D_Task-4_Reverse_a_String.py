s = "Python"
print(s[0:3])    # Pyt   → from index 0 up to (not including) 3
print(s[1:5])    # ytho  → from index 1 up to (not including) 5
print(s[:3])     # Pyt   → start omitted → begin at 0
print(s[2:])     # thon  → stop omitted → go to the end
print(s[::2])    # Pto   → every 2nd character forward
print(s[::-1])   # nohtyP → step -1 means walk backwards