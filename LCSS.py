import STPoint
import Point
DISTANCE = 100

class LCSS():
    def __init__(self, a, b, distance_threshold=None):
        self.a = a
        self.b = b
        self.len_a = len(a)
        self.len_b = len(b)
        self.distance_threshold = distance_threshold if distance_threshold is not None else DISTANCE # meter
    
    def getLCSSScore(self):
        matrix = [[0 for i in range(self.len_a+1)] for j in range(self.len_b+1)]
        for i in range(self.len_a):
            for j in range(self.len_b):
                if Point.distance(self.a[i], self.b[j]) < self.distance_threshold:
                    matrix[i+1][j+1] = matrix[i][j] + 1
                else:
                    matrix[i+1][j+1] = matrix[i+1][j] if matrix[i+1][j] > matrix[i][j+1] else matrix[i][j+1]
        min_len = self.len_a if self.len_a < self.len_b else self.len_b
        if min_len > 0:
            return matrix[self.len_a][self.len_b] / min_len
        return 0


# Sample
# a = STPoint.STPoint(130, 30, '2021-01-01 10:10:10')
# a1 = STPoint.STPoint(130.0001, 30.0001, '2021-01-01 10:10:10')
# b = STPoint.STPoint(130, 31, '2021-01-01 10:10:10')
# c = STPoint.STPoint(130, 32, '2021-01-01 10:10:10')
# d = STPoint.STPoint(130, 33, '2021-01-01 10:10:10')

# list_1 = [a, b, c]
# list_2 = [a, b, d]
# l = LCSS(list_1, list_2)
# print(l.getLCSSScore())

# list_1 = [a1, b, c]
# list_2 = [a, b, d]
# l = LCSS(list_1, list_2)
# print(l.getLCSSScore())

# list_1 = [a1, b, c]
# list_2 = [a, b, d]
# l = LCSS(list_1, list_2, 1)
# print(l.getLCSSScore())
