class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points) - 1):
            points1 = points[i]
            points2 = points[i+1]
            
            count += max(abs(points1[0] - points2[0]), abs(points1[1] - points2[1]))
        
        return count
        