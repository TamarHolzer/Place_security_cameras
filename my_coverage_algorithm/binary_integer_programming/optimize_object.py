import numpy


def objective_function(x1, x, NC, NhD, NvD, NE, NA):
    # Initialize the total sum
    # x_reshaped = numpy.reshape(x, (NC, NhD, NvD, NE, NA))
    total_sum = 0

    # Perform the summation using nested loops
    for i in range(0, NC):
        for j in range(0, NhD):
            for d in range(0, NvD):
                for e in range(0, NE):
                    for t in range(0, NA):
                        # Add the decision variable to the total sum
                        # total_sum += 1
                        total_sum += x[i][j][d][e][t]
    print(total_sum)
    return total_sum

# # Example values for parameters
# NC = 5
# NhD = 3
# NvD = 2
# NE = 4
# NA = 3

# Calculate the objective function
# result = objective_function(NC, NhD, NvD, NE, NA)
# rint("Objective function value:", result)
