import solve_with_pulp
import cameras.retrieving_the_cameras_data as dataFuncs
from my_coverage_algorithm.BIP_by_pulp import find_room2
from my_coverage_algorithm import Initialize_the_quantity_variable as init

def BIP_main(list_of_tuples_with_the_xy_cordinates = [(0, 0), (9, 0), (9, 9), (0, 9)], heightOfRoomChosenByUser = 2.50):#x,v,y,nc, nhd, nvd, ne, na,nt

    #שליפת נתוני המצלמות
    dataCameras, numOfCameras = dataFuncs.get_all_cameras()
    pointInWalls = find_room2.find_room_frame(list_of_tuples_with_the_xy_cordinates)  # מיקומים אפשריים למצלמות

    # number of target positions- מספר עמדות יעד
    NT = init.sum_the_target_position(pointInWalls)

    # number of camera positions- מספר עמדות המצלמה
    NC = init.sum_the_cameras_positions(pointInWalls)


    # number of vertical orientations- מספר כיוונים אנכיים0
    numOfVerticalOriens = []
    if dataCameras != None:
        for i in range(len(dataCameras)):
            theVer = dataCameras[i]
            numOfVerticalOriens.append(theVer.vertical_angle)
    if (numOfVerticalOriens != []):
        numOfVerticalOriens.sort(reverse=True)
        NvD = numOfVerticalOriens.pop()
    # print(NvD)

    # number of heights- מספר גבהים
    heightOfRoomChosenByUser *= 100
    if (heightOfRoomChosenByUser > 280):
        NE = 1
    else:
        NE = 280 - heightOfRoomChosenByUser

    # number of camera types- מספר סוגי מצלמות
    NA = numOfCameras

    # number of horizontal orientations- מספר כיוונים אופקיים.

    NhD = int(sum_of_horizontal_orientations(list_of_tuples_with_the_xy_cordinates, את הזווית האופקית המינימלית))


    # given minimal coverage rate- בהינתן שיעור כיסוי מינימלי
    CVR = 0.9


    sol = solve_with_pulp.solve_with_pulp(NC=NC, NhD=NhD, NvD=NvD, NE=NE, NA=NA, NT=NT, CVR=CVR)


BIP_main()