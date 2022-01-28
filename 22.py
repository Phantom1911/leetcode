class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # valid string : you must open a parantheses before closing it
        arr = []
        generate(n, n, "", arr)
        return arr


def generate(remopen, remclose, currstr, arr):
    if remopen == 0 and remclose == 0:
        arr.append(currstr)
        return
    if remopen > 0:
        generate(remopen - 1, remclose, currstr + '(', arr)
    if remclose > remopen:
        generate(remopen, remclose - 1, currstr + ')', arr)