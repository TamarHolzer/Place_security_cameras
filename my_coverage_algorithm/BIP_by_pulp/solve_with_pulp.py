import pulp
import numpy
import constraints.constraint8 as con8
import constraints.constraint9 as con9
import constraints.constraint10 as con10
import optimize_object

# Problem definition
prob = pulp.LpProblem("Camera_Optimization", pulp.LpMinimize)

# Parameters
NC = 3  # Number of camera positions
NhD = 2  # Number of horizontal orientations
NvD = 1  # Number of vertical orientations
NE = 1  # Number of heights
NA = 1  # Number of camera types
NT = 4  # Number of target positions
CVR = 0.9  # Minimum coverage rate


v = numpy.ones((NC, NhD, NvD, NE, NA, NT))



# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, d, e, t) for i in range(NC)
                                for j in range(NhD)
                                for d in range(NvD)
                                for e in range(NE)
                                for t in range(NA)), cat='Binary')
y = pulp.LpVariable.dicts("y", range(NT), cat='Binary')

#object function
optimize_object.objective_function(prob, x, NC, NhD, NvD, NE, NA)

# Add constraints
con8.inequality_constraint1(prob, x, y, v, NC, NhD, NvD, NE, NA, NT)
con9.inequality_constraint2(prob, x, y, v, NC, NT, NhD, NvD, NE, NA)
con10.inequality_constraint3(prob, y, NA, NT, CVR)


# # Add a constraint to ensure at least one camera is selected
# prob += pulp.lpSum(x[(i, j, d, e, t)] for i in range(NC)
#                    for j in range(NhD)
#                    for d in range(NvD)
#                    for e in range(NE)
#                    for t in range(NA)) >= 1, "At_least_one_camera"


# Solve the problem
prob.solve()

# Print the results
print("Status:", pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

print(v)

# Print the optimal objective function value
print("Optimal number of cameras:", pulp.value(prob.objective))