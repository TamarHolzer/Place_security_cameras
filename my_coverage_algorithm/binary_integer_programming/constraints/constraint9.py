# Inequality constraint function
import numpy
def inequality_constraint2(x1, x, y, v, NC, NT, NhD, NvD, NE, NA):
    #x_reshaped = numpy.reshape(x, (NC, NhD, NvD, NE, NA))

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
                            v = v
                            x = x
                            sum_products += v[i][j][d][e][t][k] * x[i][j][d][e][t]

        # Compare the sum of products with the right-hand side
        # Return the difference, which should be non-positive for feasible points
        if sum_products > NC * y[k]:
            return sum_products - NC * y[k]

    # If no violation is found, return 0
    return 0


# def constraint9(x, v, y, NC, NT, NhD, NvD, NE, NA):
#     #args = {'x': x, 'v': v, 'y': y, 'NC': NC, 'NT': NT, 'NhD': NhD, 'NvD': NvD, 'NE': NE, 'NA': NA}
#
#     # Define the constraint
#     constraint = {'type': 'ineq', 'fun': inequality_constraint}#, 'args': args
#
#     # Pass the constraint to scipy.optimize.minimize
#     constraints = [constraint]
#     return constraints












#print(constraints)

"""# Inequality constraint function
def inequality_constraint(x):
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
                            sum_products += V[i,j,d,e,t,k] * x[i,j,d,e,t]
    
                            # Compare the sum of products with the right-hand side
                            # Return the difference, which should be non-positive for feasible points
                            if sum_products > NC * y[k]:
                                return sum_products - NC * y[k]

    # If no violation is found, return 0
    return 0

# Define the constraint
constraint = {'type': 'ineq', 'fun': inequality_constraint}

# Pass the constraint to scipy.optimize.minimize
constraints = [constraint]
"""
