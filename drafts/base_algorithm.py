import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def calculate_cctv_positions(room_polygon, camera_coverage_angle):
    # Calculate centroid of the room polygon
    centroid_x = sum(x for x, y in room_polygon) / len(room_polygon)
    centroid_y = sum(y for x, y in room_polygon) / len(room_polygon)

    # Calculate distances from centroid to each corner
    distances = [(math.sqrt((x - centroid_x) ** 2 + (y - centroid_y) ** 2), (x, y)) for x, y in room_polygon]
    distances.sort(reverse=True)  # Sort by distance in descending order

    # Calculate the angle between cameras
    num_cameras = int(360 / camera_coverage_angle)
    angle_between_cameras = 360 / num_cameras

    # Calculate camera positions
    camera_positions = []
    for i in range(num_cameras):
        angle = math.radians(i * angle_between_cameras)
        x = distances[i % len(distances)][1][0]  # Select corners in a cyclic manner
        y = distances[i % len(distances)][1][1]
        camera_positions.append((x, y))

    return camera_positions

# Example usage
room_polygon = [(0, 0), (10, 0), (12, 6), (8, 10), (2, 8)]  # Example polygon representing room corners
camera_coverage_angle = 60  # degrees



# Define coordinates of the polygon
polygon_coordinates = [(0, 0), (10, 0), (12, 6), (8, 10), (2, 8)]


#מדפיס את המצולע
# Create a polygon patch
polygon = Polygon(polygon_coordinates, closed=True, fill=None)

# Plotting
fig, ax = plt.subplots()
ax.add_patch(polygon)
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 11)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon with Given Coordinates')
plt.grid(True)
plt.show()




positions = calculate_cctv_positions(room_polygon, camera_coverage_angle)
print("CCTV Positions:")
for i, pos in enumerate(positions, 1):
    print(f"CCTV {i}: ({pos[0]:.2f}, {pos[1]:.2f})")

#מדפיס גם מיקום מצלמות


# Define coordinates of the polygon
polygon_coordinates = [(0, 0), (10, 0), (12, 6), (8, 10), (2, 8)]

# Define location scores for CCTV cameras
cctv_locations = {
    'CCTV 1': (0.00, 0.00),
    'CCTV 2': (10.00, 0.00),
    'CCTV 3': (12.00, 6.00),
    'CCTV 4': (2.00, 8.00),
    'CCTV 5': (8.00, 10.00),
    'CCTV 6': (0.00, 0.00)
}

# Create a polygon patch
polygon = Polygon(polygon_coordinates, closed=True, fill=None)
# Plotting
fig, ax = plt.subplots()
ax.add_patch(polygon)

# Plot CCTV locations
for cctv, location in cctv_locations.items():
    ax.plot(location[0], location[1], 'ro')
    ax.text(location[0], location[1], cctv)
# Set plot limits and labels
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 11)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon with CCTV Locations')
plt.grid(True)
plt.show()
