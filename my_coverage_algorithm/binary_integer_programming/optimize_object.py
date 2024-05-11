def objective_function(x, y, v, NT, NC, NhD, NvD, NE, NA, CVR):
    # Initialize the total sum
    total_sum = 0

    # Perform the summation using nested loops
    for i in range(1, NC+1):
        for j in range(1, NhD+1):
            for d in range(1, NvD+1):
                for e in range(1, NE+1):
                    for t in range(1, NA+1):
                        # Add the decision variable to the total sum
                        #total_sum += 1
                        total_sum += x[i][j][d][e][t]

    return total_sum

# # Example values for parameters
# NC = 5
# NhD = 3
# NvD = 2
# NE = 4
# NA = 3

# Calculate the objective function
#result = objective_function(NC, NhD, NvD, NE, NA)
#rint("Objective function value:", result)
