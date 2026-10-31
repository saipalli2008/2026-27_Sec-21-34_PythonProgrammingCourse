set_data = {10, 20, 30}  # e.g. {10, 20, 30}
print("Set:", set_data)

print("20 in set?", 20 in set_data)  # 20 in set_data
print("40 not in set?", 40 not in set_data)  # 40 not in set_data

set_data.add(40)  # add 40
print("After add:", set_data)

set_data.remove(10)  # remove 10
print("After remove:", set_data)

set_data.discard(99)  # discard 99 (safe even if missing)
print("After discard:", set_data)