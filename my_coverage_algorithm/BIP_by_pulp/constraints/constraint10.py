
# Inequality constraint function
import pulp
def inequality_constraint3(prob, y, NA, NT, CVR):
    # Add the constraint
    prob += pulp.lpSum(y[k] for k in range(NA)) >= NT * CVR, "Minimum_coverage_rate_constraint"


