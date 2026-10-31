s = input("Enter a string: ")

if s == s[::-1]:  # s equals its reverse s[::-1]
    print("Palindrome")  # "Palindrome"
else:
    print("Not a palindrome")  # "Not a palindrome"