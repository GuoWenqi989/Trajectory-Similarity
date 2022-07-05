import Point


class STPoint(Point.Point):
    """
    STPoint creates a data type for spatio-temporal point, i.e. STPoint().

    """

    def __init__(self, lat, lng, time, data=None):
        super(STPoint, self).__init__(lat, lng)
        self.time = time
        self.data = data  # contains edge's attributes

    def __str__(self):
        """
        For easily reading the output
        """
        return str(self.__dict__)

# Sample
# a = STPoint(130, 30, '2021-01-01 10:10:10')
# print(a)
# b = STPoint(130, 31, '2021-01-01 10:10:10', {'k1':'v1', 'k2':'v2'})
# print(b)
# print(Point.distance(a,b))
