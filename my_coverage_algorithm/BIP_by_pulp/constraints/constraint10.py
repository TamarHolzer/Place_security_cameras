
# Inequality constraint function
import pulp
def inequality_constraint3(prob, y, NA, NT, CVR):
            prob += pulp.lpSum(y[k] for k in range(NT)) >= NT * CVR
#        for k in range(NA):

