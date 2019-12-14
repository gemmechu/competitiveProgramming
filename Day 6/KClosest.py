import math


class Solution:

    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        if K == 0:
            return [[]]
        distance = {}
        result = []
        for i in range(0, len(points)):
            distance[i] = math.pow(points[i][0], 2) + math.pow(points[i][1], 2)

        newDistance = sorted(distance.items(), key=lambda kv: (kv[1], kv[0]))

        for j in range(0, K):
            index = newDistance[j][0]
            result.append(points[index])
        return result