def rating(lvl):
    return 30 + lvl * 5 + 5*2 + 10 + (lvl - 10) * 2

def rating_overall(lvl_fort, lvl_tyr):

    fort = rating(lvl_fort)
    tyr = rating(lvl_tyr)

    if fort >= tyr:
        return 1.5 * fort + 0.5 * tyr
    else:
        return 1.5 * tyr + 0.5 * fort

rating_overall(17, 16)
rating_overall(17, 18) + 2.5 * 1.5

rating(19)
rating(18)



rating_overall(19, 17)
rating_overall(18, 17)


rating_overall(19, 21)
rating_overall(19, 21)


rating_overall(17, 17)
