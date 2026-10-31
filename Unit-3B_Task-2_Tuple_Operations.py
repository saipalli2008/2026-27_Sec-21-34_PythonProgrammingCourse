tuple_data = (1, 2, 3)  # e.g. (1, 2, 3)
tuple_extra = (4, 5)  # e.g. (4, 5)

joined = tuple_data + tuple_extra  # concatenate with +
print("Joined:", joined)

print("Slice first two:", tuple_data[:2])  # tuple_data[:2]

a, b, c = tuple_data  # unpack tuple_data
print("Unpacked:", a, b, c)