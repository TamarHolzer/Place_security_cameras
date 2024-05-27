import numpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import find_room2


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


# פונקציה לחישוב הנקודות שנמצאות בתוך הטווח של ה- FOV
def is_point_in_polygon(point, polygon):
    path = Path(polygon)
    return path.contains_point(point)


# יוצר מטריצה בוליאנית המסומנת האילו נקודות מכוסות על ידי הFOV
def generate_boolean_matrix(target_matrix, fov_vertices):
    rows, cols = target_matrix.shape
    bool_matrix = np.zeros((rows, cols), dtype=bool)

    for i in range(rows):
        for j in range(cols):
            point = (j, i)  # (x, y)
            if is_point_in_polygon(point, fov_vertices):
                bool_matrix[i, j] = True

    return bool_matrix


def show_the_matrix(fov_vertices, target_matrix, bool_matrix):
    #print("Boolean matrix representing whether the target is covered:")
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
    for i in range(target_matrix.shape[0]):
        for j in range(target_matrix.shape[1]):
            if bool_matrix[i, j]:
                plt.plot(j, i, 'ro')  # Red dot if the point is covered
            else:
                plt.plot(j, i, 'bo')  # Blue dot if the point is not covered

    plt.axis('equal')
    plt.show()


def initilize_v_with_fov(dictionary_of_the_counter_paramerters, list_of_target_psitions, numOfTargets):
    # <editor-fold desc="איתחול מ FOV-לשנות לדינאמי ולמחוק">
    epsilon = 7  # height (m)
    theta1 = 80  # horizontal angle of view (degrees) גודל הזווית של מצלמה!!!!
    theta2 = 60  # vertical angle of view (degrees) - Adjusted to ensure the angle sum is < 90
    psi = 20  # vertical angle of the camera (degrees)
    phi = 45  # horizontal angle of the camera (degrees) הכיוון של המצלמה!!!!
    T = 60  # maximum recognition distance (m)
    x0 = 0  # camera installation x-coordinate (m)
    y0 = 0  # camera installation y-coordinate (m)
    # </editor-fold>

    # מחשב את הקורדינאטות של הFOV
    fov_vertices = compute_fov(epsilon, theta1, theta2, psi, phi, T, x0, y0)  # compute_fov
   # print(f"FOV vertices: {fov_vertices}")

    # Define a target matrix (for example, a 10x10 grid)
    target_matrix = np.zeros((10, 10))

    # Generate the boolean matrix representing whether the target is covered
    # צור את המטריצה הבוליאנית המייצגת אם המטרה מכוסה
    bool_matrix = generate_boolean_matrix(target_matrix, fov_vertices)

    #show_the_matrix(fov_vertices, target_matrix, bool_matrix)


    # <editor-fold desc="שליפת כל הערכים של כמות המיקומים וכו לתוך משתנים">
    NC = dictionary_of_the_counter_paramerters['NC']
    NhD = dictionary_of_the_counter_paramerters['NhD']
    NvD = dictionary_of_the_counter_paramerters['NvD']
    NE = dictionary_of_the_counter_paramerters['NE']
    NA = dictionary_of_the_counter_paramerters['NA']
    NT = dictionary_of_the_counter_paramerters['NT']
    CVR = dictionary_of_the_counter_paramerters['CVR']
    # </editor-fold>

    #איתחול V באפסים
    v = numpy.zeros((NC, NhD, NvD, NE, NA, NT))


    list_of_target_psitions = (0.0, 0.0), (20,6), (4, 4)
    NT = list_of_target_psitions.__len__()

    # <editor-fold desc="מעבר על כל האפשרויות לכל נקודה וסימון האם הנקודה נצפית ע"י כל מצלמה">
    for i in range(NC):  # לכל הנקודות להתקנה
        for j in range(NhD):  # לכל הזוויות האופקיות
            for d in range(NvD):  # ולכל הזוויות האנכיות
                for h in range(NE):  # לכל הגבהים של ההתקנה
                    for t in range(NA):  # ובודק לכל מצלמה
                        fov_vertices = compute_fov(epsilon, theta1, theta2, psi, phi, T, x0, y0) # מחשב את הקורדינאטות של הFOV
                        for k in range(NT):  # עובר על כל הנקודות כיסוי
                            if k >= list_of_target_psitions.__len__():
                                continue
                            v[i, j, d, h, t, k] = is_point_in_polygon(list_of_target_psitions[k], fov_vertices)
    print(v)
    # </editor-fold>



#הפעלה למחוק!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
wall = ((0, 0), (3, 0), (2, 2), (2, 0))
c = find_room2.find_room_frame(wall)

targets = find_room2.find_room_targets(c)
unique_points = set()

# Iterate through each sub-list in `c`
for sublist in c:
    # Iterate through each point in the sublist
    for point in sublist:
        # Add the point to the set of unique points
        unique_points.add(point)

# The size of the set is the count of distinct points
numOfTargets = len(unique_points)

NC = 8
NhD = 2
NvD = 2
NE = 1
NA = 1
NT = numOfTargets
CVR = 0.9

the_counter_parameters = {'NC': NC, 'NhD': NhD, 'NvD': NvD, 'NE': NE, 'NA': NA, 'NT': NT, 'CVR': CVR}

initilize_v_with_fov(the_counter_parameters, targets, numOfTargets)
