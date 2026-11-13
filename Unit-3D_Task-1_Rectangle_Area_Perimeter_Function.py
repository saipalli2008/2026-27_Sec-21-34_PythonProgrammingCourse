def rectangle_area_perimeter(length, breadth):  # length, breadth
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

length = 5  # e.g. 5
breadth = 3  # e.g. 3
area, perimeter = rectangle_area_perimeter(length, breadth)
print("Area:", area)
print("Perimeter:", perimeter)