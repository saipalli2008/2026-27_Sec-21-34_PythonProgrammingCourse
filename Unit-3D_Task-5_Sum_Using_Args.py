def sum_values(*args):  
    total = 0
    for value in args:
        total = total + value
    return total

print(sum_values(1, 2, 3))
print(sum_values(10, 20,30,40))