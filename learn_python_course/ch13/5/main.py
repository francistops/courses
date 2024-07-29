def area_sum(rectangles):
    area = []
    for rectangle in rectangles:
        area.append(rectangle['height'] * rectangle['width'])
    return sum(area)
