def laptopRentals(times):
    # Write your code here.
    # one laptop is enough in case there are no overlaps between the usage times
    # num of laptops needed = max number of overlaps for any time
    usageMap = {}
    for slot in times:
        slotStart, slotEnd = slot[0], slot[1]
        for i in range(slotStart, slotEnd):
            usageMap[i] = 1 if i not in usageMap else usageMap[i] + 1

    ans = 0
    for key in usageMap:
        if ans < usageMap[key]:
            ans = usageMap[key]

    return ans
