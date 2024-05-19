
# #פונקציה המוצאת את כל הנקודות השלמות בין שתי נקודות המתקבלות כקלט
# def bresenham_line(x1, y1, x2, y2):
#     coordinates = []
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     sx = -1 if x1 > x2 else 1
#     sy = -1 if y1 > y2 else 1
#     err = dx - dy
#
#     while True:
#         coordinates.append((x1, y1))
#
#         if x1 == x2 and y1 == y2:
#             break
#
#         e2 = 2 * err
#         if e2 > -dy:
#             err -= dy
#             x1 += sx
#         if e2 < dx:
#             err += dx
#             y1 += sy
#
#     return coordinates
#
# # Example usage:
# x1, y1 = 9, 0
# x2, y2 = 0, 9

# line_coordinates = bresenham_line(x1, y1, x2, y2)
# print("Coordinates between ({}, {}) and ({}, {}):".format(x1, y1, x2, y2))
# print(line_coordinates)