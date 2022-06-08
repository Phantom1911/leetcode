"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if len(intervals) == 0:
            return 0
        heap = []
        # print(intervals)
        # print(type(intervals[0]))
        intervals = sorted(intervals, key= lambda x:x.start)
        # print(intervals[0].start)
        maxRooms = 1
        heapq.heappush(heap, intervals[0].end)
        for i in range(1,len(intervals)):
            currInterval = intervals[i]
            if heap[0] > currInterval.start:
                heapq.heappush(heap, currInterval.end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, currInterval.end)
            maxRooms = max(maxRooms, len(heap))
        return maxRooms