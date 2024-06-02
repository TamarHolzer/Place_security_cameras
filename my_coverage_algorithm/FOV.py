import numpy as np

# FOV
def compute_fov(epsilon, theta1, theta2, psi, phi, T, x0, y0):
    # Step 0: Compute tau and check conditions
    tau = epsilon / np.cos(np.radians(theta2 + psi))
    if (theta2 + psi) >= 90 or tau > T:
        raise ValueError("FOV cannot be computed with the given parameters.")

    # Step 1: Compute the initial coordinates of the FOV vertices
    # שלב 1: חשב את הקואורדינטות הראשוניות של קודקודי ה-FOV
    h = epsilon
    tan_theta1_half = np.tan(np.radians(theta1 / 2))
    tan_psi = np.tan(np.radians(psi))
    cos_psi = np.cos(np.radians(psi))
    cos_theta2_psi = np.cos(np.radians(theta2 + psi))
    tan_theta2_psi = np.tan(np.radians(theta2 + psi))

    # Vertex at the lower left (near the camera)
    # קודקוד בפינה השמאלית התחתונה (ליד המצלמה)
    p1_x = h * tan_psi
    p1_y = (h / cos_psi) * tan_theta1_half

    # Vertex at the lower right (near the camera)
    # קודקוד בפינה הימנית התחתונה (ליד המצלמה)
    p2_x = h * tan_psi
    p2_y = (h / cos_psi) * -tan_theta1_half

    # Vertex at the upper right (far from the camera)
    # קודקוד בצד ימין למעלה (רחוק מהמצלמה)
    p3_x = h * tan_theta2_psi
    p3_y = (h / cos_theta2_psi) * tan_theta1_half

    # Vertex at the upper left (far from the camera)
    # קודקוד בפינה השמאלית העליונה (רחוק מהמצלמה)
    p4_x = h * tan_theta2_psi
    p4_y = (h / cos_theta2_psi) * (-tan_theta1_half)

    # Step 2: Rotate the coordinates by angle phi
    # שלב 2: סובב את הקואורדינטות לפי זווית phi
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
    # שלב 3: תרגם לקואורדינטות ההתקנה בפועל
    p1_x += x0
    p1_y += y0

    p2_x += x0
    p2_y += y0

    p3_x += x0
    p3_y += y0

    p4_x += x0
    p4_y += y0

    # Return the coordinates of the FOV vertices
    # החזר את הקואורדינטות של קודקודי ה-FOV
    return (p1_x, p1_y), (p2_x, p2_y), (p4_x, p4_y), (p3_x, p3_y)




