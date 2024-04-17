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

# Inequality constraint function
def inequality_constraint(x, v, y, NT, NC, NhD, NvD, NE, NA):
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
                            sum_products += v[i,j,d,e,t,k] * x[i,j,d,e,t]

        # Compare the sum of products with the right-hand side
        # Return the difference, which should be non-negative for feasible points
        if sum_products < y[k]:
            return sum_products - y[k]

    # If no violation is found, return 0
    return 0

# Define the constraint
constraint = {'type': 'ineq', 'fun': inequality_constraint}

# Pass the constraint to scipy.optimize.minimize
constraints = [constraint]

