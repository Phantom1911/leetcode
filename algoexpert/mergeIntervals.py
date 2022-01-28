def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key = lambda x: x[0])
	i = 0
	while i < (len(intervals)):
		if i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
			intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
			intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
			del intervals[i+1]
		else:
			i+= 1
	return intervals