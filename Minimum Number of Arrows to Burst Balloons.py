class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arrow = 1
        points.sort(key = lambda x:x[1])
        end1 = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > end1:
                arrow += 1
                end1 = points[i][1]
                print(end1)
            else:
                continue
        return arrow
