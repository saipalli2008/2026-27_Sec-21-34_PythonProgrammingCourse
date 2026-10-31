number = int(input("Enter a number: "))
for multiplier in range(1,11):  # multiplier; use range(...) for 1 to 10
    product= number*multiplier  # multiply number by the current multiplier
    print(f"{number} x {multiplier} = {product}")  # show number, multiplier, and product