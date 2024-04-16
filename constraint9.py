# Inequality constraint function
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

    # Calculate the right-hand side of the inequality constraint
    rhs = NC * y[k]

    # Compare the sum of products with the right-hand side
    # Return the difference, which should be non-positive for feasible points
    return sum_products - rhs


# Define the constraint
constraint = {'type': 'ineq', 'fun': inequality_constraint}

# Pass the constraint to scipy.optimize.minimize
constraints = [constraint]