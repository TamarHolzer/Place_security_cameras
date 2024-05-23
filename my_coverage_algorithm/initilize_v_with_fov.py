import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path


def compute_fov(epsilon, theta1, theta2, psi, phi, T, x0, y0):
    # Step 0: Compute tau and check conditions
    tau = epsilon / np.cos(np.radians(theta2 + psi))
    if (theta2 + psi) >= 90 or tau > T:
        raise ValueError("FOV cannot be computed with the given parameters.")

    # Step 1: Compute the initial coordinates of the FOV vertices
    h = epsilon
    tan_theta1_half = np.tan(np.radians(theta1 / 2))
    tan_psi = np.tan(np.radians(psi))
    cos_psi = np.cos(np.radians(psi))
    cos_theta2_psi = np.cos(np.radians(theta2 + psi))
    tan_theta2_psi = np.tan(np.radians(theta2 + psi))

    # Vertex at the lower left (near the camera)
    p1_x = h * tan_psi
    #p1_x = h * tan_psi - (h / cos_psi) * tan_theta1_half
    p1_y = (h / cos_psi) * tan_theta1_half

    # Vertex at the lower right (near the camera)
    #p2_x = h * tan_psi + (h / cos_psi) * tan_theta1_half
    p2_x = h * tan_psi
    p2_y = (h / cos_psi) * -(tan_theta1_half)

    # Vertex at the upper right (far from the camera)
    # p3_x = h * tan_theta2_psi + (h / cos_theta2_psi) * tan_theta1_half
    p3_y = (h / cos_theta2_psi) * tan_theta1_half
    p3_x = h * tan_theta2_psi

    # Vertex at the upper left (far from the camera)
    # p4_ = h * tan_theta2_psi - (h / cos_theta2_psi) * tan_theta1_half
    p4_y = - (h / cos_theta2_psi) * tan_theta1_half
    p4_x = h * tan_theta2_psi

    # Step 2: Rotate the coordinates by angle phi
    def rotate(x, y, angle):
        rad = np.radians(angle)
        x_new = x * np.cos(rad) - y * np.sin(rad)
        y_new = x * np.sin(rad) + y * np.cos(rad)
        return x_new, y_new

    p1_x, p1_y = rotate(p1_x, p1_y, phi)
    p2_x, p2_y = rotate(p2_x, p2_y, phi)
    p3_x, p3_y = rotate(p3_x, p3_y, phi)
    p4_x, p4_y = rotate(p4_x, p4_y, phi)

    # Step 3: Translate to the actual installation coordinates
    p1_x += x0
    p1_y += y0

    p2_x += x0
    p2_y += y0

    p3_x += x0
    p3_y += y0

    p4_x += x0
    p4_y += y0

    # Return the coordinates of the FOV vertices
    return (p1_x, p1_y), (p2_x, p2_y), (p3_x, p3_y), (p4_x, p4_y)

#
# def is_point_in_polygon(point, polygon):
#     path = Path(polygon)
#     return path.contains_point(point)
#
#
# def generate_boolean_matrix(target_matrix, fov_vertices):
#     rows, cols = target_matrix.shape
#     bool_matrix = np.zeros((rows, cols), dtype=bool)
#
#     for i in range(rows):
#         for j in range(cols):
#             point = (j, i)  # (x, y)
#             if is_point_in_polygon(point, fov_vertices):
#                 bool_matrix[i, j] = True
#
#     return bool_matrix


# Example usage with valid parameters
epsilon = 7  # height (m)
theta1 = 60  # horizontal angle of view (degrees) גודל הזווית של מצלמה!!!!
theta2 = 30  # vertical angle of view (degrees) - Adjusted to ensure the angle sum is < 90
psi = 20  # vertical angle of the camera (degrees)
phi = 0  # horizontal angle of the camera (degrees) הכיוון של המצלמה!!!!
T = 60  # maximum recognition distance (m)
x0 = 0  # camera installation x-coordinate (m)
y0 = 0  # camera installation y-coordinate (m)

fov_vertices = compute_fov(epsilon, theta1, theta2, psi, phi, T, x0, y0)
print(f"FOV vertices: {fov_vertices}")

# Define a target matrix (for example, a 10x10 grid)
target_matrix = np.zeros((10, 10))

# Generate the boolean matrix representing whether the target is covered
#bool_matrix = generate_boolean_matrix(target_matrix, fov_vertices)
print("Boolean matrix representing whether the target is covered:")
#print(bool_matrix)

# Plotting the FOV trapezoid and the target matrix for visualization
vertices = np.array(fov_vertices)
vertices = np.append(vertices, [vertices[0]], axis=0)  # Close the trapezoid by repeating the first point

plt.figure()
plt.plot(vertices[:, 0], vertices[:, 1], marker='o')
plt.fill(vertices[:, 0], vertices[:, 1], alpha=0.3)
plt.title('Field of View (FOV) Trapezoid')
plt.xlabel('X-coordinate (m)')
plt.ylabel('Y-coordinate (m)')
plt.grid(True)

# Plot the target matrix points
# for i in range(target_matrix.shape[0]):
#     for j in range(target_matrix.shape[1]):
#         if bool_matrix[i, j]:
#             plt.plot(j, i, 'ro')  # Red dot if the point is covered
#         else:
#             plt.plot(j, i, 'bo')  # Blue dot if the point is not covered

plt.axis('equal')
plt.show()
