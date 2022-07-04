import math

DEGREES_TO_RADIANS = math.pi / 180
RADIANS_TO_DEGREES = 1 / DEGREES_TO_RADIANS
EARTH_MEAN_RADIUS_METER = 6371008.7714
DEG_TO_KM = DEGREES_TO_RADIANS * EARTH_MEAN_RADIUS_METER
LAT_PER_METER = 8.993203677616966e-06
LNG_PER_METER = 1.1700193970443768e-05


class Point:
    def __init__(self, lng, lat):
        self.lng = lng
        self.lat = lat

    def __str__(self):
        return '({},{})'.format(self.lat, self.lng)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        # equal. Orginally is compared with reference. Here we change to value
        return self.lat == other.lat and self.lng == other.lng

    def __ne__(self, other):
        # not equal
        return not self == other

def same_coords(a, b):
    # we can directly use == since Point has updated __eq__()
    if a == b:
        return True
    else:
        return False

def distance(a, b):
    """
    Calculate haversine distance between two GPS points in meters
    Args:
    -----
        a,b: Point class
    Returns:
    --------
        d: float. haversine distance in meter
    """
    if same_coords(a, b):
        return 0.0
    delta_lat = math.radians(b.lat - a.lat)
    delta_lng = math.radians(b.lng - a.lng)
    h = math.sin(delta_lat / 2.0) * math.sin(delta_lat / 2.0) + math.cos(math.radians(a.lat)) * math.cos(
        math.radians(b.lat)) * math.sin(delta_lng / 2.0) * math.sin(delta_lng / 2.0)
    c = 2.0 * math.atan2(math.sqrt(h), math.sqrt(1 - h))
    d = EARTH_MEAN_RADIUS_METER * c
    return d

# Sample
# a = Point(130, 30)
# b = Point(130, 30)
# c = Point(130, 31)
# d = Point(130, 29)
# e = Point(131, 30)
# f = Point(129, 30)

# print(a==b)
# print(a)
# print(distance(a,b))
# print(distance(a,c))
# print(distance(a,d))
# print(distance(a,e))
# print(distance(a,f))
