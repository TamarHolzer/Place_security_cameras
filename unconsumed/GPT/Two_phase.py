
# def BIP():
#     #האם יש מצלמה במיקום הזה
#     xijdet = 0
#     #האם השטח מכוסה
#     yk = 0
#     #האם השטח מכוסה ע"י המצלמה הזאת
#     vijdet = 0
#     print(xijdet)


def two_phase_algorithm(NC, NhD, NvD, NE, NA, NT, CVR):
    # Phase 1
    # Define the decision variables
    # x_i_j_d_e_t represents whether there exists a camera at position i with
    # horizontal orientation j, vertical orientation d, height e, and angle of view t
    # Initialize decision variables x_i_j_d_e_t to zero
    x_i_j_d_e_t = {(i, j, d, e, t): 0
                   for i in range(1, NC + 1)
                   for j in range(1, NhD + 1)
                   for d in range(1, NvD + 1)
                   for e in range(1, NE + 1)
                   for t in range(1, NA + 1)}
    #print('AAA' + x_i_j_d_e_t.values().__str__())


    # Define y_k representing whether the target at position k is covered by a camera
    # Initialize y_k to zero
    y_k = {k: 0 for k in range(1, NT + 1)}
    #print(y_k.values().__str__())

    # Define V_i_j_d_e_t_k representing whether the target at position k is visible from camera position i
    # with horizontal orientation j, vertical orientation d, height e, and angle of view t
    # Initialize V_i_j_d_e_t_k to zero
    V_i_j_d_e_t_k = {(i, j, d, e, t, k): 0
                     for i in range(1, NC + 1)
                     for j in range(1, NhD + 1)
                     for d in range(1, NvD + 1)
                     for e in range(1, NE + 1)
                     for t in range(1, NA + 1)
                     for k in range(1, NT + 1)}

    # Objective function for phase 1
    objective_phase_1 = sum(x_i_j_d_e_t.values())

    # Phase 1 constraints
    constraints_phase_1 = []
    for k in range(1, NT + 1):
        constraints_phase_1.append(sum(V_i_j_d_e_t_k[(i, j, d, e, t, k)] * x_i_j_d_e_t[(i, j, d, e, t)] \
                                       for i in range(1, NC + 1) for j in range(1, NhD + 1) \
                                       for d in range(1, NvD + 1) for e in range(1, NE + 1) \
                                       for t in range(1, NA + 1)) >= y_k[k])
        constraints_phase_1.append(sum(V_i_j_d_e_t_k[(i, j, d, e, t, k)] * x_i_j_d_e_t[(i, j, d, e, t)] \
                                       for i in range(1, NC + 1) for j in range(1, NhD + 1) \
                                       for d in range(1, NvD + 1) for e in range(1, NE + 1) \
                                       for t in range(1, NA + 1)) <= NC * y_k[k])
    constraints_phase_1.append(sum(y_k.values()) >= NT * CVR)
    print(constraints_phase_1)
    # Phase 2
    # Solve the FIX problem using the hill climbing method
    # Initial value for phase 2 is obtained from phase 1

    # Implement hill climbing method here

    return objective_phase_1, constraints_phase_1


# Example usage
# number of camera positions- מספר עמדות המצלמה
NC = 3
# number of horizontal orientations- מספר כיוונים אופקיים.
NhD = 2
# number of vertical orientations
NvD = 2
# number of heights- מספר כיוונים אנכיים
NE = 1
# number of camera types- מספר סוגי מצלמות
NA = 1
# number of target positions- מספר עמדות יעד
NT = 2
# given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
CVR = 0.5

objective, constraints = two_phase_algorithm(NC, NhD, NvD, NE, NA, NT, CVR)
print("Objective Function for Phase 1:", objective)
print("Constraints for Phase 1:", constraints)

# BIP()