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