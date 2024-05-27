import solve_with_pulp
from my_coverage_algorithm import find_room2
import numpy
def BIP_main():#x,v,y,nc, nhd, nvd, ne, na,nt
    #כל אלו אמורים ליהיות גנרים לא פה!
    a = [(0, 0), (9, 0), (9, 9), (0, 9)]
    # number of camera positions- מספר עמדות המצלמה
    pointInWalls = find_room2.find_room_frame(a)
    children_len = [len(child) for child in pointInWalls]
    NC = sum(children_len)
    # number of horizontal orientations- מספר כיוונים אופקיים.
    NhD = 2
    # number of vertical orientations- מספר כיוונים אנכיים
    NvD = 2
    # number of heights- מספר גבהים
    NE = 1
    # number of camera types- מספר סוגי מצלמות
    NA = 1
    # number of target positions- מספר עמדות יעד
    dirOfTheTargetPoints = find_room2.find_room_targets(pointInWalls)
    numOfTheTargetPoints = 0
    listOfTargetPositions = []
    #המרת הנקודות לרשימה
    for key, tuple_list in dirOfTheTargetPoints.items():
        #print(f"Key: {key}")
        for tuple_item in tuple_list:
            numOfTheTargetPoints += 1
            listOfTargetPositions.append(tuple_item)
            #print(f"  Tuple: {tuple_item}")
    print(listOfTargetPositions)
    NT = numOfTheTargetPoints

    # given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
    CVR = 0.9

    sol = solve_with_pulp.solve_with_pulp(NC=NC, NhD=NhD, NvD=NvD, NE=NE, NA=NA, NT=NT, CVR=CVR)


BIP_main()