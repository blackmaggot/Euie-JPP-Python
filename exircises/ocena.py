__author__ = 'WiktorMarchewka'
import random
def ocena(points_gained, max_points_to_earn):
    amount_of_percentages = (points_gained * 100)/max_points_to_earn
    dst = 'dst'
    dst_plus = 'dst+'
    db = 'db'
    db_plus = 'db+'
    bdb = 'bdb'
    if amount_of_percentages <= 50:
        return dst
    elif amount_of_percentages > 50 and amount_of_percentages <= 65:
        return dst_plus
    elif amount_of_percentages > 65 and amount_of_percentages <= 75:
        return db
    elif amount_of_percentages > 75 and amount_of_percentages <= 85:
        return db_plus
    elif amount_of_percentages >= 95:
        return bdb

print(ocena(random.randint(1, 50), 50))
