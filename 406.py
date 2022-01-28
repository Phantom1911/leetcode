def shiftright(i, people, toshift):
    count = 0
    while count != toshift:
        people[i], people[i + 1] = people[i + 1], people[i]
        count += 1

class listcomparator(list):
    def __lt__(self, other):
        if self[0] == other[0]:
            return self[1] < other[1]
        return self[0] < other[0]


class Solution:
    def reconstructQueue(self, people) :
        # pay attention to sorted here
        # if two people have same heights, it is required for the one with greater infronts to come first
        people = sorted(people, key=listcomparator)
        n = len(people)
        for i in range(n - 1, -1, -1):
            toshift = people[i][1]
            if toshift != 0:
                shiftright(i, people, toshift)
        return people

if __name__=="__main__":
    print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))