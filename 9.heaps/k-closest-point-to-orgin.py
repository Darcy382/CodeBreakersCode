import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        max_heap = []
        for i in range(K):
            heapq.heappush(max_heap, (-1 * self.distance(points[i]), points[i]))

        for point in points[K:]:
            distance = self.distance(point)
            if distance < max_heap[0][0] * -1:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-1 * distance, point))
        points = []
        for distance, point in max_heap:
            points.append(point)
        return points

    def distance(self, point):
        x, y = point[0], point[1]
        return ((x ** 2 + y ** 2) ** 0.5)