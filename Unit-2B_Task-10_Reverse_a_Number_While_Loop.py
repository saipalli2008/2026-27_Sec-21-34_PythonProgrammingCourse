num=int(input("Enter a num: "))
orig_num = num
reversed_num = 0

while num>0:  # continue while number still has digits
    last_digit=num %10  # get the last digit with % 10
    reversed_num = reversed_num *10+last_digit
    num=num//10

print(f"Reverse of {orig_num} is {reversed_num}")