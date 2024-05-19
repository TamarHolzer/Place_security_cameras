# Inequality constraint function
import pulp


def inequality_constraint1(prob, x, y, v, NC, NhD, NvD, NE, NA, NT):
    for k in range(NT):
        prob += pulp.lpSum(v[i, j, d, e, t, k] * x[(i, j, d, e, t)]
                           for i in range(NC)
                           for j in range(NhD)
                           for d in range(NvD)
                           for e in range(NE)
                           for t in range(NA)) >= y[k], f"Coverage_constraint_for_target_{k}"

    # # Iterate over all targets k
    # # x_reshaped = numpy.reshape(x, (NC, NhD, NvD, NE, NA))
    #
    # # for k in range(NT):
    # #     prob += (pulp.lpSum(v[i][j][d][e][t][k] * x[(i, j, d, e, t)]
    # #                         for i in range(NC)
    # #                         for j in range(NhD)
    # #                         for d in range(NvD)
    # #                         for e in range(NE)
    # #                         for t in range(NA)) >= y[k], f"Coverage constraint for target {k}")
    # for k in range(NT):
    #     prob += (pulp.lpSum(v[i, j, d, e, t, k] * x[(i, j, d, e, t)]
    #                         for i in range(NC)
    #                         for j in range(NhD)
    #                         for d in range(NvD)
    #                         for e in range(NE)
    #                         for t in range(NA)) <= NC * y[k])
    #
    # # # Iterate over all combinations of indices i, j, d, e, and t
    # # for i in range(NC):
    # #     for j in range(NhD):
    # #         for d in range(NvD):
    # #             for e in range(NE):
    # #                 for t in range(NA):
    # #                     # Compute the product of decision variable x and other variable V
    # #                      prob += pulp.lpSum(v[i][j][d][e][t][k] * x[i][j][d][e][t]) >= y[k], f"Coverage constraint for target {k}"
