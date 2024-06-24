import math
import numpy
import matplotlib.pyplot as plt
#import drafts.show_polygon as polygon
#from drafts import show_polygon


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
    #print("Points between ({}, {}) and ({}, {}) with a difference of 0.5:".format(x1, y1, x2, y2))
    #print(result)

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
    # polygon.print_polygon(allCordinated)
    return walls


# cordinates = [(0, 0), (0, 20), (20, 30), (20, 0)]
# find_space(cordinates)

# def find_room_targets():  # allCordinated
#     targets = []
#     allCordinated = [[(0, 0), (0, 1), (0, 2)], [(5, 0), (8, 0), (9, 0)]]
#     point = 0
#     sublist = 1
#     while (allCordinated[allCordinated][sublist] != None):
#         while (allCordinated[0][sublist] != None):
#             a = find_room_frame(allCordinated[0][point], allCordinated[sublist][point])
#             targets.append(a)
#             point += 1
#
#         sublist += 1
#
#     return targets


# find_room_targets()
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



def generate_hexagonal_grid(radius):
    points = []
    for q in range(-radius, radius + 1):
        r1 = max(-radius, -q - radius)
    r2 = min(radius, -q + radius)
    for r in range(r1, r2 + 1):
        points.append((q, r))
    return points


def hex_to_cartesian(q, r):
    x = q * 3 / 2
    y = math.sqrt(3) * (r + q / 2)
    return (x, y)


def plot_hexagonal_grid(radius):
    points = generate_hexagonal_grid(radius)
    cartesian_points = [hex_to_cartesian(q, r) for (q, r) in points]
    x_coords, y_coords = zip(*cartesian_points)

    plt.scatter(x_coords, y_coords, c='blue')
    plt.title(f'Hexagonal Grid Points with Radius {radius}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


    # Example usage
    radius = 3  # Radius of the hexagonal grid
    plot_hexagonal_grid(radius)

#print(generate_hexagonal_grid(50))

def find_room_targets(walls):
    if not walls or len(walls) < 2:
        raise ValueError("There should be at least two walls to calculate intermediate points.")

    interval = 7

    first_wall = walls[0]
    other_walls = walls[1:]

    intermediate_points = {}

    for point1 in first_wall:
        x1, y1 = point1
        intermediate_points[point1] = []

        for wall in other_walls:
            for point2 in wall:
                x2, y2 = point2
                vector = numpy.array([x2 - x1, y2 - y1])
                distance = numpy.linalg.norm(vector)
                num_intervals = int(distance // interval)

                for i in range(1, num_intervals):
                    fraction = i * interval / distance
                    intermediate_point = (x1 + fraction * vector[0], y1 + fraction * vector[1])
                    intermediate_points[point1].append(intermediate_point)

    return intermediate_points



allCordinated = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(5, 0), (8, 0), (9, 0),(10, 0)], [(8,8)]]
print(find_room_targets(allCordinated))