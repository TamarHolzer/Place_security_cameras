# Inequality constraint function
import numpy
def inequality_constraint1(x1, x, y, v, NC, NT, NhD, NvD, NE, NA):
    # Iterate over all targets k
   # x_reshaped = numpy.reshape(x, (NC, NhD, NvD, NE, NA))

    for k in range(NT):
        # Initialize the sum of products
        sum_products = 0

        # Iterate over all combinations of indices i, j, d, e, and t
        for i in range(NC):
            for j in range(NhD):
                for d in range(NvD):
                    for e in range(NE):
                        for t in range(NA):
                            # Compute the product of decision variable x and other variable V
                            sum_products += v[i][j][d][e][t][k] * x[i][j][d][e][t]

        # Compare the sum of products with the right-hand side
        # Return the difference, which should be non-negative for feasible points
        if sum_products < y[k]:
            return sum_products - y[k]

    # If no violation is found, return 0
    return 0

# def constraint8(x, v, y, NT, NC, NhD, NvD, NE, NA):
#
#     #args = {'x': x, 'v': v, 'y': y, 'NC': NC, 'NT': NT, 'NhD': NhD, 'NvD': NvD, 'NE': NE, 'NA': NA}
#
#     # Define the constraint
#     constraint = {'type': 'ineq', 'fun': inequality_constraint} #, 'args': args
#
#     # Pass the constraint to scipy.optimize.minimize
#     constraints = [constraint]
#     return constraints













"""# Inequality constraint function
def inequality_constraint(x, V, y, NC, NhD, NvD, NE, NA, NT):
    # Initialize the sum of products
    sum_products = 0

    # Iterate over all combinations of indices i, j, d, e, and t
    for i in range(NC):
        for j in range(NhD):
            for d in range(NvD):
                for e in range(NE):
                    for t in range(NA):
                        # Sum over all targets k
                        for k in range(NT):
                            # Compute the product of decision variable x and other variable V
                            sum_products += V[i, j, d, e, t, k] * x[i, j, d, e, t]

    # Initialize the sum of target values
    sum_targets = 0

    # Sum over all targets k
    for k in range(NT):
        # Sum up all target values
        sum_targets += y[k]

    # Compare the sum of products with the sum of target values
    # Return the difference, which should be non-negative for feasible points
    return sum_products - sum_targets


# Define the constraint
constraint = {'type': 'ineq', 'fun': inequality_constraint}

# Pass the constraint to scipy.optimize.minimize
constraints = [constraint]"""
#
# a = [(0, 0), (9, 9), (6, 3)]
# # number of camera positions- מספר עמדות המצלמה
# c =a
# NC = 3
# # number of horizontal orientations- מספר כיוונים אופקיים.
# NhD = 2
# # number of vertical orientations
# NvD = 2
# # number of heights- מספר כיוונים אנכיים
# NE = 1
# # number of camera types- מספר סוגי מצלמות
# NA = 1
# # number of target positions- מספר עמדות יעד
# b = 48  # find_room.find_room_targets(a)
# NT = b  # len(b)
# # given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
# CVR = 0.9
#
# v = [[[[[[1 for k in range(NT)] for t in range(NA)] for e in range(NE)] for d in range(NvD)] for j in range(NhD)]
#      for i in range(NC)]
# # Initialize x as a multi-dimensional list with dimensions (NC, NhD, NvD, NE, NA)
# x = [[[[[1 for t in range(NA)] for e in range(NE)] for d in range(NvD)] for j in range(NhD)] for i in range(NC)]
# y = [1 for k in range(NT)]
#
# val = inequality_constraint1(x, y, v, NC, NT, NhD, NvD, NE, NA, CVR)
# print(val)