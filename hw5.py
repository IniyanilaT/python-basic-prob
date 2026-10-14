import math
items = int(input("no of items:"))
capacity = int(input("capacity:"))
box = items / capacity
boxes = math.ceil(box)
print(boxes) 