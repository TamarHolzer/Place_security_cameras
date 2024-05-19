import matplotlib.pyplot as plt
import drafts.show_polygon as polygon
from drafts import show_polygon

# מציאת הקו הישר בהפרשים של חצי
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

    # show_line(result)
    return result


def show_line(r):
    # הצגת הקו
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


def find_room_frame(allCordinated):
    walls = []
    j = 0

    for i in allCordinated:
        if (j < (len(allCordinated) - 1)):
            walls.append(find_line(allCordinated[j], allCordinated[j + 1]))
        else:
            walls.append(find_line(allCordinated[j], allCordinated[0]))
        j += 1
    #polygon.print_polygon(allCordinated)
    return walls

# cordinates = [(0, 0), (0, 20), (20, 30), (20, 0)]
# find_space(cordinates)

def find_room_targets():#allCordinated
    targets = []
    allCordinated = [[(0, 0), (0, 1), (0, 2)], [(5, 0), (8, 0), (9, 0)]]
    point = 0
    sublist = 1
    while(allCordinated[allCordinated][sublist] != None):
        while (allCordinated[0][sublist] != None):
            a = find_room_frame(allCordinated[0][point], allCordinated[sublist][point])
            targets.append(a)
            point += 1

        sublist += 1




    # for point in allCordinated[0]:
    #     for sublist in allCordinated[1:]:
    #         # for other_point in sublist:
    #         #     if(other_point!=point):
    #         #         if(other_point != None):
    #         #             a = [find_room_frame([point, other_point])]
    #         #             targets.append(a)
    #         #         else:
    #         #             break
    #         #     else:
    #         #         continue
    #
    return targets

