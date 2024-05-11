import math


def calculate_fov(x0, y0, height, phi, psi, theta1, theta2, max_distance):
    # Step 0: Calculate tau
    tau = height / math.cos(math.radians(theta2 + psi))
    if theta2 + psi < 90 or tau > max_distance:
        # Stop calculation if conditions are not met
        return None

    # Step 1: Calculate vertices assuming P0 = (0, 0) and phi = 0
    h = height
    tan_psi = math.tan(math.radians(psi))
    tan_theta1_over_2 = math.tan(math.radians(theta1 / 2))
    tan_theta2_over_2 = math.tan(math.radians((theta2 + psi) / 2))

    x1 = h * tan_psi
    y1 = h
    x2 = h / math.cos(math.radians(psi)) * (math.cos(math.radians(theta1 / 2)) + tan_theta1_over_2)
    y2 = h
    x3 = h * tan_psi
    y3 = -h
    x4 = h / math.cos(math.radians(psi)) * (math.cos(math.radians(theta1 / 2)) - tan_theta1_over_2)
    y4 = -h

    # Step 2: Rotate vertices by phi
    cos_phi = math.cos(math.radians(phi))
    sin_phi = math.sin(math.radians(phi))
    vertices_rotated = [
        (x1 * cos_phi - y1 * sin_phi, x1 * sin_phi + y1 * cos_phi),
        (x2 * cos_phi - y2 * sin_phi, x2 * sin_phi + y2 * cos_phi),
        (x3 * cos_phi - y3 * sin_phi, x3 * sin_phi + y3 * cos_phi),
        (x4 * cos_phi - y4 * sin_phi, x4 * sin_phi + y4 * cos_phi)
    ]

    # Step 3: Translate vertices to actual installation coordinates (x0, y0)
    vertices_actual = [(vertex[0] + x0, vertex[1] + y0) for vertex in vertices_rotated]

    return vertices_actual


# Example usage:
x0 = 0
y0 = 0
height = 7
phi = 0
psi = 45
theta1 = 80
theta2 = 80
max_distance = 60

fov_vertices = calculate_fov(x0, y0, height, phi, psi, theta1, theta2, max_distance)
if fov_vertices:
    print("FOV Vertices:")
    for vertex in fov_vertices:
        print(vertex)
else:
    print("FOV cannot be computed with the given parameters.")
