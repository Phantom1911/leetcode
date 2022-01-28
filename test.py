def findmaxidx(nums):
    currmaxidx , currsecmaxidx =0,0
    for i in range(len(nums)):
        if nums[i] > nums[currmaxidx]:
            currmaxidx = i

    for i in range(len(nums)):
        if nums[i] == nums[currmaxidx] and i != currmaxidx:
            currsecmaxidx = i
        elif nums[i] > nums[currsecmaxidx]:
            currsecmaxidx = i

    return currmaxidx, currsecmaxidx


if __name__=="__main__":
    print(findmaxidx([3,5,4,3,5,4]))