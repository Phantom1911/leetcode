class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # start from the end of the unsorted array and use siftDown on each element
        n = len(array)
        for i in range(n - 1, -1, -1):
            self.siftDown(i, array)
        return array

    def siftDown(self, idx, array):
        leftChildIdx = (2 * idx) + 1
        rightChildIdx = (2 * idx) + 2
        n = len(array)
        if 0 <= leftChildIdx < n:
            # check if left chilf is invalid
            if array[leftChildIdx] > array[idx]:
                array[leftChildIdx], array[idx] = array[idx], array[leftChildIdx]
                self.siftDown(leftChildIdx, array)
            # if left child is valid, check if right child is invalid
            elif 0 <= rightChildIdx < n and array[rightChildIdx] > array[idx]:
                array[rightChildIdx], array[idx] = array[idx], array[rightChildIdx]
                self.siftDown(rightChildIdx, array)

if __name__=="__main__":
    minHeap = MinHeap([8,4,1,0,9,17,14])
    print(minHeap.heap)