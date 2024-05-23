import math

import numpy
def FOV():
    # משתנים
    x = 0                               #מיקום על ציר הX
    y = 0                               #מיקום על ציר הY
    horizontal_orientations = 60        #-גודל הזוית מאוזן 𝜃1
    vertical_orientations = 60           #-גודל הזוית מאונך 𝜃2
    height = 7                               #𝜀-גובה ההתקנה
    horizontal_angle_of_view = 45           #𝜑-כיוון הצילום ביחס לציר הX-זוית אופקית
    vertical_angle_of_view = 20            #𝜓 כיוון הצילום ביחס לציר הZ-זוויות אנכיות
    available_sight_range = 60              #
    recognition_distance = 60               #T

    #step0
    #𝜏 = 𝜀/{cos(𝜃2 + 𝜓)}.
    #זיהוי מרחק מקסימלי
    #המרתי את הרדינאטורים למעלות -לא לשכוח בחישובי הטריגו
    i = numpy.cos(numpy.radians(vertical_orientations+vertical_angle_of_view))
    littleT = height/i
    #print(littleT)

    #If 𝜃2 + 𝜓 < 90 or 𝜏>T
    if (vertical_orientations + vertical_angle_of_view) >= 90 or littleT > recognition_distance:
        return None

    #step1

    a = height*numpy.tan(numpy.radians(vertical_angle_of_view))
    b = (height/(numpy.cos(numpy.radians(vertical_angle_of_view))*(+(numpy.tan(horizontal_orientations/2)))))
    c = (height/(numpy.cos(numpy.radians(vertical_angle_of_view))*(-(numpy.tan(horizontal_orientations/2)))))
    d = height*numpy.tan(numpy.radians(vertical_orientations+vertical_angle_of_view))
    e = (height/(numpy.cos(numpy.radians((vertical_angle_of_view+vertical_orientations))*(+(numpy.tan(horizontal_orientations/2))))))
    f = (height/(numpy.cos(numpy.radians((vertical_angle_of_view+vertical_orientations))*(-(numpy.tan(horizontal_orientations/2))))))

    list_step1 = [[a],
                  [b],
                  [a],
                  [c],
                  [d],
                  [e],
                  [d],
                  [f]]
    vector_step1 = numpy.array(list_step1)
    #print(vector_step1)

    #step2
    a = numpy.cos(numpy.radians((numpy.radians(horizontal_angle_of_view))))
    b = numpy.sin(numpy.radians(horizontal_angle_of_view))
    rotation_mat = numpy.array([[a, -b], [b, a]])
   # print(vector_step1[0])

    vector_step11 = numpy.array([[a, b],
                                 [a, c],
                                 [d, e],
                                 [d, f]])
    #print(vector_step11)
    vector_step2 = numpy.dot(rotation_mat, vector_step11.T).T
    #print(vector_step2)

    # vector_i = numpy.array([[vector_step1[0]],
    #                         [vector_step1[1]]])
    # vector_step2 = numpy.multiply(v2, vector_i)
    # print(vector_step2)
    # v0 = numpy.array([[0, 0],
    #                   [0, 0]])

    # vector_step2 = numpy.array([v2], [v0],)
    # vector_step2 = []
    #print(v2)
    # vector_step2 = numpy.zeros([2, 2, 2, 2], dtype=float)
    # #print("check")
    # #print(vector_step2)
    # i = 0
    # for x in range(0, 4, 2):
    #     vector_i = numpy.array([[vector_step1[x]],
    #                             [vector_step1[x+1]]])
    #     #print("me too")
    #     #print(vector_i)
    #     #print(v2)
    #     vector_step2[i] = numpy.multiply(v2, vector_i)
    #     i = i+1
    #print(vector_step2)

    #step3
    vi = numpy.array([[x, y],
                      [x, y],
                      [x, y],
                      [x, y]])
    # print(len(vector_step2))
    vector_step3 = numpy.add(vector_step2, vi)
    #print(vector_step3)


    return vector_step3

b = FOV()
print(b)