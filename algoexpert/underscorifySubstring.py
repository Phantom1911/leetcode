def underscorifySubstring(string, substring):
    '''
	this question seems to be a combination of string matching
	we can do string matching to get all the locations of the substring
	then we can merge all the intervals of occurence to know where to place _
	'''
    m, n = len(string), len(substring)
    intervals = []
    for i in range(m - n + 1):
        if string[i:i + n] == substring:
            intervals.append([i, i + n])
    print(intervals)
    mergeIntervals(intervals)
    print(intervals)
    inserted_underscores = 0
    for interval in intervals:
        string = insert_underscore(string, interval[0] + inserted_underscores)
        inserted_underscores += 1
        string = insert_underscore(string, interval[1] + inserted_underscores)
        inserted_underscores += 1
    return string


def mergeIntervals(intervals):
    i = 0
    while i < len(intervals):
        if i + 1 < len(intervals) and intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = intervals[i + 1][1]
            del intervals[i + 1]
        else:
            i += 1
    return intervals


def insert_underscore(string, index):
    return string[:index] + '_' + string[index:]
