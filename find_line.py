import matplotlib.pyplot as plt


#מציאת הקו הישר בהפרשים של חצי
def find_line(x, y):
    def points_between_coordinates(x1, y1, x2, y2):
        # Calculate the distance between the two points
        distance_x = abs(x2 - x1)
        distance_y = abs(y2 - y1)

    # Determine the number of points to interpolate along the line
        num_points = int(max(distance_x, distance_y) * 2) + 1

    # Generate the coordinates by linearly interpolating between the start and end points
        coordinates = []
        for i in range(num_points):
            t = i / (num_points - 1)
            new_x = x1 + t * (x2 - x1)
            new_y = y1 + t * (y2 - y1)
            coordinates.append((new_x, new_y))

        return coordinates


    x1, y1 = x[0], x[1]
    x2, y2 = y[0], y[1]

    result = points_between_coordinates(x1, y1, x2, y2)
    print("Points between ({}, {}) and ({}, {}) with a difference of 0.5:".format(x1, y1, x2, y2))
    print(result)

    show_line(result)
    return result



def show_line(r):
    #הצגת הקו
    # Define coordinates of the line
    line_coordinates = r

    # Extract x and y coordinates separately
    x_coordinates = [coord[0] for coord in line_coordinates]
    y_coordinates = [coord[1] for coord in line_coordinates]

    # Plot the line
    plt.plot(x_coordinates, y_coordinates)

    # Set plot limits and labels
    plt.xlim(min(x_coordinates) - 0.5, max(x_coordinates) + 0.5)
    plt.ylim(min(y_coordinates) - 0.5, max(y_coordinates) + 0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Line with Given Coordinates')
    plt.grid(True)
    plt.show()





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