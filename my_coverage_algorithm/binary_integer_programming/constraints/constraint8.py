# Inequality constraint function
import numpy
def inequality_constraint1(x, y, v, NC, NT, NhD, NvD, NE, NA, CVR):
    # Iterate over all targets k
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
                            a = v[i][j][d][e][t][k]
                            print(x[i][j][d][e][t])
                            #b = x[i][j][d][e][t]
                            #c = a * b
                            #sum_products += c

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



