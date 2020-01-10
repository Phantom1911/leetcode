def kadanesAlgorithm(array):
    meh = array[0]
    msf = array[0]
    for i in range(1, len(array)):
        meh = max(array[i], meh + array[i])
        msf = max(msf, meh)
    return msf


if __name__=="__main__":
    print(kadanesAlgorithm([-9, -1, -8]))