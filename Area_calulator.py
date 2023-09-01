import math

def paint_calc(height, width, cover):
    area = math.ceil((height * width) / cover)
    print(f"You need {area} cans")


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc (height = test_h, width = test_w, cover = coverage)
