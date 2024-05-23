from matplotlib.patches import Polygon
import matplotlib.pyplot as plt


def print_polygon(polygon_coordinates):
    polygon = Polygon(polygon_coordinates, closed=True, fill=None)

    # Plotting
    fig, ax = plt.subplots()
    ax.add_patch(polygon)

    ax.set_xlim(-1, 30)
    ax.set_ylim(-1, 50)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Polygon with Given Coordinates')
    plt.grid(True)
    plt.show()

    # positions = calculate_cctv_positions(room_polygon, camera_coverage_angle)
    # print("CCTV Positions:")
    # for i, pos in enumerate(positions, 1):
    #     print(f"CCTV {i}: ({pos[0]:.2f}, {pos[1]:.2f})")
