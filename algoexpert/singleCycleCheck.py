def hasSingleCycle(array):
    if hasZero(array):
        return False
    visited = dict()
    for i in range(len(array)):
        visited[i] = False
    for i in range(len(array)):
        curr_idx = i
        final_idx = (i + array[i])
        if final_idx < 0:
            temp = abs(final_idx) % len(array)
            temp = -temp
            final_idx = temp + len(array)
        else:
            final_idx = final_idx % len(array)
        for j in range(len(array)):
            visited[j] = False
        visited[curr_idx] = True
        while (final_idx != curr_idx and visited[final_idx] is False):
            visited[final_idx] = True
            final_idx += array[final_idx]
            if final_idx < 0:
                temp = abs(final_idx) % len(array)
                temp = -temp
                final_idx = temp + len(array)
                final_idx = final_idx % len(array)
            else:
                final_idx = final_idx % len(array)
        if final_idx == curr_idx and allVisitedOnce(visited):
            return True
    return False

def allVisitedOnce(visited):
    for key in visited:
        if visited[key] == False:
            return False
    return True

def hasZero(array):
    for i in range(len(array)):
        if array[i] == 0:
            return True
    return False

if __name__ == "__main__":
    print(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 909, -26]))
