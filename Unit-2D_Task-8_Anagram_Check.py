s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):  # sorted(s1) equals sorted(s2)
    print("Anagrams")  # "Anagrams"
else:
    print("Not anagrams")  # "Not anagrams"