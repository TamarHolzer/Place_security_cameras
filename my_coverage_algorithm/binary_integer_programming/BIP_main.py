import constraints.constraint8 as con8
import constraints.constraint9 as con9
import constraints.constraint10 as con10
import optimize_object as obj
from scipy.optimize import minimize
from my_coverage_algorithm import find_room
import numpy
def BIP_main():#x,v,y,nc, nhd, nvd, ne, na,nt
    #כל אלו אמורים ליהיות גנרים לא פה!
    a = [(0, 0), (9, 9), (6, 3)]
    # number of camera positions- מספר עמדות המצלמה
    c = find_room.find_room_frame(a)
    children_len = [len(child) for child in c]
    NC = sum(children_len)
    # number of horizontal orientations- מספר כיוונים אופקיים.
    NhD = 2
    # number of vertical orientations
    NvD = 2
    # number of heights- מספר כיוונים אנכיים
    NE = 1
    # number of camera types- מספר סוגי מצלמות
    NA = 1
    # number of target positions- מספר עמדות יעד
    b = 48 #find_room.find_room_targets(a)
    NT = b#len(b)
    # given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
    CVR = 0.9


    #v = [[[[[[1 for k in range(NT)] for t in range(NA)] for e in range(NE)] for d in range(NvD)] for j in range(NhD)]
    #for i in range(NC)]
    # Initialize x as a multi-dimensional list with dimensions (NC, NhD, NvD, NE, NA)
    #x = [[[[[1 for t in range(NA)] for e in range(NE)] for d in range(NvD)] for j in range(NhD)] for i in range(NC)]
    y = [1 for k in range(NT)]
    x = numpy.ones((NC, NhD, NvD, NE, NA))
    v = numpy.ones((NC, NhD, NvD, NE, NA, NT))

    #x = [1, 1, 1, 1, 1]
    #y = [1, 1, 1, 1, 1]
    #v = [1, 1, 1, 1, 1]
    #כל אלו אמורים ליהיות גנרים לא פה!

    #con8.inequality_constraint1(x, y, v, NC, NT, NhD, NvD, NE, NA, CVR)

    obj_args = (x, NC, NhD, NvD, NE, NA)  # Arguments for the objective function
    constraint1_args = (x, y, v, NC, NT, NhD, NvD, NE, NA)  # Arguments for constraint 1
    constraint2_args = (x, y, v, NC, NT, NhD, NvD, NE, NA)  # Arguments for constraint 2
    constraint3_args = (y, NT, CVR)  # Arguments for constraint 3

    #קבלתי את המאפינים
    #אילוצים
    constraints = [{'type': 'ineq', 'fun': con8.inequality_constraint1, 'args': constraint1_args},
                   {'type': 'ineq', 'fun': con9.inequality_constraint2, 'args': constraint2_args},
                   {'type': 'ineq', 'fun': con10.inequality_constraint3, 'args': constraint3_args}]

    #פונקצית המטרה
    #objectFunction = obj.objective_function(NC, NhD, NvD, NE, NA)
    #print(objectFunction)

    #גבולות
    bounds = [(0, 1)] * (NC * NhD * NvD * NE * NA * NT)

    #ניחוש התחלתי
    x0 = [1] * (NC * NhD * NvD * NE * NA * NT)
#    , args=(NC, NT, NhD, NvD, NE, NA, CVR)
    result = minimize(fun=obj.objective_function, x0=x0, args=obj_args, method='SLSQP',
                      bounds=bounds, constraints=constraints)
    print(result)

    print("ללל")
#, args=(x, y, v, NC, NT, NhD, NvD, NE, NA, CVR)
BIP_main()