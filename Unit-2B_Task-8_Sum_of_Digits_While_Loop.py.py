#sum of digits
num=int(input("Enter a number: "))
orig_num=num #original number
work =num #working number
total =0#digit sum
while work>0:
    digit =work %10
    total=total+digit
    work =work//10
print(f"sum of digit of {orig_num} is {total}")
