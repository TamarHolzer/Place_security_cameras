import pulp
import constraints.constraintP8 as con8
import constraints.constraintP9 as con9
import constraints.constraintP10 as con10
import optimize_object_pulp
from my_coverage_algorithm import initilize_v_with_fov
from my_coverage_algorithm.BIP_by_pulp import find_room2
from flask import Flask, request, jsonify
from flask_cors import CORS
# import cameras.retrieving_the_cameras_data as dataFuncs
# from my_coverage_algorithm.BIP_by_pulp import find_room2
# from cameras import Camera

app = Flask(__name__)
CORS(app)

def solve_with_pulp(NC, NhD, NvD, NE, NA, NT, CVR, listOfTargetPositions):
    # Define the problem
    print("open prob")
    prob = pulp.LpProblem("Camera_Optimization", pulp.LpMinimize)

    dictionaryOfTheCountersParam = {
        "NC": NC,
        "NhD": NhD,
        "NvD": NvD,
        "NE": NE,
        "NA": NA,
        "NT": NT,
        "CVR": CVR
    }

    print("params")
    # Assume V is a predefined 6-dimensional array that represents visibility
    v = initilize_v_with_fov.initilize_v_with_fov(dictionaryOfTheCountersParam, listOfTargetPositions)

    # Decision variables
    x = pulp.LpVariable.dicts("x", ((i, j, d, e, t) for i in range(NC) for j in range(NhD)
                                    for d in range(NvD) for e in range(NE) for t in range(NA)), cat='Binary')
    y = pulp.LpVariable.dicts("y", range(NT), cat='Binary')

    # Define the objective function
    optimize_object_pulp.objective_function(prob, x, NC, NhD, NvD, NE, NA)
    print("constraints")
    # Add constraints
    con8.inequality_constraint1(prob, x, y, v, NC, NhD, NvD, NE, NA, NT)
    print("con1")
    con9.inequality_constraint2(prob, x, y, v, NC, NT, NhD, NvD, NE, NA)
    print("con2")
    con10.inequality_constraint3(prob, y, NA, NT, CVR)
    print("solving")
    # Solve the problem
    prob.solve()

    # Print the results
    print("Status:", pulp.LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    print("Optimal number of cameras:", pulp.value(prob.objective))
