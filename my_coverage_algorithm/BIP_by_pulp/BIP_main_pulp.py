#import solve_with_pulp
import cameras.retrieving_the_cameras_data as dataFuncs
from my_coverage_algorithm.BIP_by_pulp import find_room2
from cameras import Camera


# import numpy
def BIP_main(list_of_tuples_with_the_xy_cordinates = [(0, 0), (9, 0), (9, 9), (0, 9)]):#x,v,y,nc, nhd, nvd, ne, na,nt
    #שליפת נתוני המצלמות
    dataCameras, numOfCameras = dataFuncs.get_all_cameras()

    # number of camera positions- מספר עמדות המצלמה
    pointInWalls = find_room2.find_room_frame(list_of_tuples_with_the_xy_cordinates)#מיקומים אפשריים למצלמות
    children_len = [len(child) for child in pointInWalls] #סכימת הנקודות
    NC = sum(children_len)
    # number of horizontal orientations- מספר כיוונים אופקיים.
    NhD = 2
    # number of vertical orientations- מספר כיוונים אנכיים0
    numOfVerticalOriens = []
    if dataCameras != None:
        for i in range(len(dataCameras)):
            theVer = dataCameras[i]
            numOfVerticalOriens.append(theVer.vertical_angle)
    else:
        print("Make sure that PYCHARM is open as an administrator")
    NvD = max(numOfVerticalOriens)
    #print(NvD)
    # number of heights- מספר גבהים
    NE = 1
    # number of camera types- מספר סוגי מצלמות
    NA = numOfCameras
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
    #print(listOfTargetPositions)
    NT = numOfTheTargetPoints

    # given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
    CVR = 0.9

    sol = solve_with_pulp.solve_with_pulp(NC=NC, NhD=NhD, NvD=NvD, NE=NE, NA=NA, NT=NT, CVR=CVR)


BIP_main()