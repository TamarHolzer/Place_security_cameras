import numpy
import FOV

def Initialize_the_variable_v(NC, NhD, NvD, NE, NA, NT):
    # NC - מספר עמדות המצלמה
    # NhD - מספר כיוונים אופקיים.
    # NvD  - מספר כיוונים אנכיים
    # NE  - מספר גבהים
    # NA - מספר סוגי מצלמות
    # NT- מספר עמדות יעד
    # CVR - בהינתן שיעור כיסוי מינימלי
    # initial v with zeros
    v = numpy.zeros((NC, NhD, NvD, NE, NA, NT))

    #
    for k in range(NT):  # עובר על כל הנקודות כיסוי
        for t in range(NA):  # ובודק לכל מצלמה
            for i in range(NC):  # לכל הנקודות להתקנה
                for h in range(NE):  # לכל הגבהים של ההתקנה
                    for j in range(NhD):  # לכל הזוויות האופקיות
                        for d in range(NvD):  # ולכל הזוויות האנכיות
                            #is_visible()
                            print()

#def is_visible():
