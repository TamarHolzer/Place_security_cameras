
# Inequality constraint function
import numpy
def inequality_constraint3(x1, y, NT, CVR):

    # Calculate the sum of target values
    sum_targets = sum(y)

    # Calculate the right-hand side of the inequality constraint
    rhs = NT * CVR

    # Compare the sum of target values with the right-hand side
    # Return the difference, which should be non-negative for feasible points
    return sum_targets - rhs


#def constraint10(y, NT, CVR):
    #args = {'y': y, 'NT': NT, 'CVR': CVR}

    # Define the constraint
    #constraint = {'type': 'ineq', 'fun': inequality_constraint}#, 'args': args

    # Pass the constraint to scipy.optimize.minimize
    #constraints = [constraint]
    #return constraints