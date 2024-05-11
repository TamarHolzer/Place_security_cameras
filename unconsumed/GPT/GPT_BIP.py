import math


class Camera:
    def __init__(self, x0, y0, height, phi, psi, theta1, theta2, max_distance):
        self.x0 = x0
        self.y0 = y0
        self.height = height
        self.phi = phi
        self.psi = psi
        self.theta1 = theta1
        self.theta2 = theta2
        self.max_distance = max_distance

    def calculate_fov(self):
        # Step 0: Calculate tau
        tau = self.height / math.cos(math.radians(self.theta2 + self.psi))
        if self.theta2 + self.psi < 90 or tau > self.max_distance:
            # Stop calculation if conditions are not met
            return None

        # Step 1: Calculate vertices assuming P0 = (0, 0) and phi = 0
        h = self.height
        tan_psi = math.tan(math.radians(self.psi))
        tan_theta1_over_2 = math.tan(math.radians(self.theta1 / 2))
        tan_theta2_over_2 = math.tan(math.radians((self.theta2 + self.psi) / 2))

        x1 = h * tan_psi
        y1 = h
        x2 = h / math.cos(math.radians(self.psi)) * (math.cos(math.radians(self.theta1 / 2)) + tan_theta1_over_2)
        y2 = h
        x3 = h * tan_psi
        y3 = -h
        x4 = h / math.cos(math.radians(self.psi)) * (math.cos(math.radians(self.theta1 / 2)) - tan_theta1_over_2)
        y4 = -h

        # Step 2: Rotate vertices by phi
        cos_phi = math.cos(math.radians(self.phi))
        sin_phi = math.sin(math.radians(self.phi))
        vertices_rotated = [
            (x1 * cos_phi - y1 * sin_phi, x1 * sin_phi + y1 * cos_phi),
            (x2 * cos_phi - y2 * sin_phi, x2 * sin_phi + y2 * cos_phi),
            (x3 * cos_phi - y3 * sin_phi, x3 * sin_phi + y3 * cos_phi),
            (x4 * cos_phi - y4 * sin_phi, x4 * sin_phi + y4 * cos_phi)
        ]

        # Step 3: Translate vertices to actual installation coordinates (x0, y0)
        vertices_actual = [(vertex[0] + self.x0, vertex[1] + self.y0) for vertex in vertices_rotated]

        return vertices_actual


# Example usage:
camera = Camera(x0=0, y0=0, height=7, phi=0, psi=45, theta1=80, theta2=80, max_distance=60)
fov_vertices = camera.calculate_fov()
if fov_vertices:
    print("FOV Vertices:")
    for vertex in fov_vertices:
        print(vertex)
else:
    print("FOV cannot be computed with the given parameters.")
