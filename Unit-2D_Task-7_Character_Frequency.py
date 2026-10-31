s = input("Enter a string: ")

frequency = {}  # empty dictionary {}

for ch in s:  # each character in s
    if ch in frequency:  # character already in frequency?
        frequency[ch] = frequency[ch] + 1  # increase by 1
    else:
        frequency[ch] = 1  # first time: store 1

for char, count in frequency.items():  # items in frequency
    print(char, ":", count)
    