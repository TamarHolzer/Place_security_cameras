#import pulp
#
#
# def BIP_mine():
#     # Example usage
#     # number of camera positions- מספר עמדות המצלמה
#     NC = 10
#     # number of horizontal orientations- מספר כיוונים אופקיים.
#     NhD = 4
#     # number of vertical orientations
#     NvD = 2
#     # number of heights- מספר כיוונים אנכיים
#     NE = 3
#     # number of camera types- מספר סוגי מצלמות
#     NA = 2
#     # number of target positions- מספר עמדות יעד
#     NT = 20
#     # given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
#     CVR = 0.8
#
#     x_i_j_d_e_t = ['i','j','d','e','t','k']
#
#
#     objective_function = 0
#
#
#     #האם קיימת מצלמה במיקום הזה עם מאפיינים כאלו
#     y_k = 0 #אם המיקום הזה מכוסה על ידי מצלמה
#     v_ijdetk = 0 #האם המיקום הזה מכוסה על ידי המצלמה הזאת
#
#
import pulp

# Define the problem
prob = pulp.LpProblem("Camera_Placement", pulp.LpMinimize)

# Define decision variables
NC = 10  # Number of camera positions
NhD = 4  # Number of horizontal orientations
NvD = 3  # Number of vertical orientations
NE = 2   # Number of heights
NA = 1   # Number of camera types
NT = 20  # Number of target positions
CVR = 0.8  # Given minimal coverage rate

x = pulp.LpVariable.dicts("x",
                           ((i, j, d, e, t) for i in range(1, NC + 1)
                                            for j in range(1, NhD + 1)
                                            for d in range(1, NvD + 1)
                                            for e in range(1, NE + 1)
                                            for t in range(1, NA + 1)),
                            cat='Binary')

y = pulp.LpVariable.dicts("y", range(1, NT + 1), cat='Binary')

# Define the objective function
prob += pulp.lpSum(x[(i, j, d, e, t)] for i in range(1, NC + 1)
                                      for j in range(1, NhD + 1)
                                      for d in range(1, NvD + 1)
                                      for e in range(1, NE + 1)
                                      for t in range(1, NA + 1))

# Define constraints
for k in range(1, NT + 1):
    prob += pulp.lpSum(V[i - 1][j - 1][d - 1][e - 1][t - 1] * x[(i, j, d, e, t)]
                       for i in range(1, NC + 1)
                       for j in range(1, NhD + 1)
                       for d in range(1, NvD + 1)
                       for e in range(1, NE + 1)
                       for t in range(1, NA + 1)) >= y[k]

    prob += pulp.lpSum(V[i - 1][j - 1][d - 1][e - 1][t - 1] * x[(i, j, d, e, t)]
                       for i in range(1, NC + 1)
                       for j in range(1, NhD + 1)
                       for d in range(1, NvD + 1)
                       for e in range(1, NE + 1)
                       for t in range(1, NA + 1)) <= NC * y[k]

prob += pulp.lpSum(y[k] for k in range(1, NT + 1)) >= NT * CVR

# Solve the problem
prob.solve()

# Output results
print("Status:", pulp.LpStatus[prob.status])

for var in prob.variables():
    print(var.name, "=", var.varValue)

print("Minimum number of cameras:", pulp.value(prob.objective))

