num=int(input("Enter a 3-digit number: "))
orig_num=num
total=0
while num>0:
    digit = num%10
    total =total +digit ** 3
    num = num //10
if total == orig_num:
    print(f"{orig_num} is an Armstrong number")
else:
    print(f"{orig_num} is  not an Armstrong number")