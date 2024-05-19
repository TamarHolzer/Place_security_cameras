# Inequality constraint function
import numpy
import pulp


def inequality_constraint2(prob, x, y, v, NC, NT, NhD, NvD, NE, NA):
    # Iterate over each target k
    for k in range(NT):
        # Sum up the products of v and x for all combinations of i, j, d, e, and t
        sum_product = pulp.lpSum(v[i, j, d, e, t, k] * x[(i, j, d, e, t)]
                                 for i in range(NC)
                                 for j in range(NhD)
                                 for d in range(NvD)
                                 for e in range(NE)
                                 for t in range(NA)) <= NC * y[k], f"Upper_bound_constraint_for_target_{k}"

    # Add a constraint to ensure that the sum of products is less than or equal to NC * y[k]
    #prob += sum_product

#
#     for k in range(NT):
#         prob += (pulp.lpSum(v[i, j, d, e, t, k] * x[(i, j, d, e, t)]
#                             for i in range(NC)
#                             for j in range(NhD)
#                             for d in range(NvD)
#                             for e in range(NE)
#                             for t in range(NA)) <= NC * y[k], f"Upper_bound_constraint_for_target_{k}")
#
#
