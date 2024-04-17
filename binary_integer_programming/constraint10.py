
# Inequality constraint function
def inequality_constraint(x, y, NT, CVR):
    # Calculate the sum of target values
    sum_targets = sum(y)

    # Calculate the right-hand side of the inequality constraint
    rhs = NT * CVR

    # Compare the sum of target values with the right-hand side
    # Return the difference, which should be non-negative for feasible points
    return sum_targets - rhs


# Define the constraint
constraint = {'type': 'ineq', 'fun': inequality_constraint}

# Pass the constraint to scipy.optimize.minimize
constraints = [constraint]
