def diskStacking(disks):
    disksDict = {}
    n = len(disks)
    for i in range(len(disks)):
        disksDict[i] = {"maxHeight": disks[i][2], "topDisk": i, "existingConfig": [i]}
    for i in range(1, len(disks)):
        t1 = -1
        t2 = -1
        if canPlaceInExistingHighest(disks[i], disks[disksDict[i - 1]["topDisk"]]):
            t1 = disksDict[i - 1]["maxHeight"] + disks[i][2]
        if canPlaceInExistingHighest(disks[disksDict[i - 1]["topDisk"]], disks[i]):
            t2 = disksDict[i - 1]["maxHeight"] + disks[i][2]
        # print("t1", t1)
        if t1 > disks[i][2]:
            disksDict[i]["maxHeight"] = t1
            disksDict[i]["topDisk"] = i
            disksDict[i]["existingConfig"] = []
            for j in disksDict[i-1]["existingConfig"]:
                disksDict[i]["existingConfig"].append(j)
            disksDict[i]["existingConfig"].append(i)
        elif t2 > disks[i][2]:
            disksDict[i]["maxHeight"] = t2
            disksDict[i]["existingConfig"] = []
            disksDict[i]["existingConfig"].append(i)
            for j in disksDict[i - 1]["existingConfig"]:
                disksDict[i]["existingConfig"].append(j)
            disksDict[i]["topDisk"] = disksDict[i]["existingConfig"][-1]

    ans = []
    # print(disksDict)
    for i in disksDict[n - 1]["existingConfig"]:
        ans.append(disks[i])
    ans = ans[::-1]
    return ans


def canPlaceInExistingHighest(newDisk, topDisk):
    if newDisk[0] < topDisk[0] and newDisk[1] < topDisk[1] and newDisk[2] < topDisk[2]:
        return True
    return False


if __name__=="__main__":
    print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 3, 4]]))


