total_input_number=int(input("Enter how many number:"))
total_sum=0
for input_index in range(total_input_number):
    entered_number=float(input("Enter a number:"))
    total_sum = total_sum + entered_number
average = total_sum/total_input_number
print(f"total_sum={total_sum}")
print(f"Avarage={average}")