x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x <= y:  # outer: compare x with y (smaller side)
    if x <= z:  # inner under if: compare x with z
        smallest = x  
    else:
        smallest = z  
else:
    if y <= z:  # inner under else: compare y with z
        smallest = y  
    else:
        smallest = z

print(f"Smallest = {smallest} (among {x}, {y}, {z})")