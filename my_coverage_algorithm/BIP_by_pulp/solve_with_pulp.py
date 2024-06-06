import pulp
import constraints.constraintP8 as con8
import constraints.constraintP9 as con9
import constraints.constraintP10 as con10
import optimize_object_pulp
from my_coverage_algorithm import initilize_v_with_fov

# import cameras.retrieving_the_cameras_data as dataFuncs
# from my_coverage_algorithm.BIP_by_pulp import find_room2
# from cameras import Camera

def solve_with_pulp(NC, NhD, NvD, NE, NA, NT, CVR):
    # Define the problem
    prob = pulp.LpProblem("Camera_Optimization", pulp.LpMinimize)


    # # Parameters
    # NC = 8
    # NhD = 2
    # NvD = 2
    # NE = 1
    # NA = 1
    # NT = 20
    # CVR = 0.9

    # Assume V is a predefined 6-dimensional array that represents visibility
    v = initilize_v_with_fov.initilize_v_with_fov()

    # Decision variables
    x = pulp.LpVariable.dicts("x", ((i, j, d, e, t) for i in range(NC) for j in range(NhD)
                                    for d in range(NvD) for e in range(NE) for t in range(NA)), cat='Binary')
    y = pulp.LpVariable.dicts("y", range(NT), cat='Binary')

    # Define the objective function
    optimize_object_pulp.objective_function(prob, x, NC, NhD, NvD, NE, NA)

    # Add constraints
    con8.inequality_constraint1(prob, x, y, v, NC, NhD, NvD, NE, NA, NT)
    con9.inequality_constraint2(prob, x, y, v, NC, NT, NhD, NvD, NE, NA)
    con10.inequality_constraint3(prob, y, NA, NT, CVR)

    # Solve the problem
    prob.solve()

    # Print the results
    print("Status:", pulp.LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    print("Optimal number of cameras:", pulp.value(prob.objective))
