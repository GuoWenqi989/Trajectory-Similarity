import STPoint
import Point
DISTANCE = 100

class LCSS():
    def __init__(self, a, b, distance_threshold=None):
        self.a = a
        self.b = b
        self.len_a = lens(a)
        self.len_b = lens(b)
        self.distance_threshold = distance_threshold if distance_threshold == None else DISTANCE # meter
    
    def getLCSS():
        matrix = [[0 for i in range(len_a+1)] for j in range(len_b+1)]
        for i in range(len_a):
            for j in range(len_b):
                if Point.distance(a[i], b[j]) < self.distance_threshold:
                    matrix[i+1][j+1] = matrix[i][j] + 1
                else:
                    matrix[i+1][j+1] = matrix[i+1][j] if matrix[i+1][j] > matrix[i][j+1]
        min_len = len_a if len_a < len_b else len_b
        if min_len > 0:
            return matrix[len_a][len_b] / min_len
        return 0

