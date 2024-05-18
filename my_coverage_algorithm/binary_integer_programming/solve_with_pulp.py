import pulp
import numpy

# Problem definition
prob = pulp.LpProblem("Camera_Optimization", pulp.LpMinimize)

# Parameters
NC = 3
NhD = 2
NvD = 2
NE = 1
NA = 1
NT = 48
CVR = 0.9
y = [1 for k in range(NT)]
x = numpy.ones((NC, NhD, NvD, NE, NA))
v = numpy.ones((NC, NhD, NvD, NE, NA, NT))

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, d, e, t) for i in range(NC) for j in range(NhD)
                                for d in range(NvD) for e in range(NE) for t in range(NA)), cat='Binary')
y = pulp.LpVariable.dicts("y", range(NT), cat='Binary')

# Objective function
prob += pulp.lpSum(x[i, j, d, e, t] for i in range(NC) for j in range(NhD)
                   for d in range(NvD) for e in range(NE) for t in range(NA))

# Constraints
for k in range(NT):
    prob += pulp.lpSum(v[i][j][d][e][t][k] * x[i, j, d, e, t] for i in range(NC) for j in range(NhD)
                       for d in range(NvD) for e in range(NE) for t in range(NA)) >= y[k]
    prob += pulp.lpSum(v[i][j][d][e][t][k] * x[i, j, d, e, t] for i in range(NC) for j in range(NhD)
                       for d in range(NvD) for e in range(NE) for t in range(NA)) <= NC * y[k]

prob += pulp.lpSum(y[k] for k in range(NT)) >= NT * CVR

# Solve the problem
prob.solve()

# Print results
print("Status:", pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
