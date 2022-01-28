def waterArea(heights):
    # Write your code here.
    maxes = [0 for i in range(len(heights))]
    lmax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = lmax
        lmax = max(lmax, height)
    rmax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(maxes[i], rmax)
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rmax = max(rmax, height)
    return sum(maxes)


pass



def waterArea2(heights):
    # for each index we'll need how much water can be stored
	# for each index get the max height to the left (including current height) and max height to the right
	n = len(heights)
	if n == 0:
		return 0
	leftmax = [0 for i in range(n)]
	rightmax = [0 for i in range(n)]
	leftmax[0]  = heights[0]
	rightmax[n-1] = heights[n-1]
	for i in range(1,n):
		leftmax[i] = max(leftmax[i-1], heights[i])
	for i in range(n-2,-1,-1):
		rightmax[i] = max(rightmax[i+1], heights[i])
	ans = 0
	for i in range(n):
		currwater = (min(leftmax[i],rightmax[i]) - heights[i])
		ans = ans + currwater if currwater > 0 else ans
	return ans
