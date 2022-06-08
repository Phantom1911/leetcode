from typing import List


class Node:
    def __init__(self, name, email):
        self.name = name
        self.email = email


from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mailSet = set()
        adjlist = dict()
        mailToNodeMap = {}
        for acc in accounts:
            for i in range(1, len(acc)):
                currMail = acc[i]
                currNode = None
                if currMail in mailSet:
                    currNode = mailToNodeMap[currMail]
                else:
                    mailSet.add(currMail)
                    currNode = Node(acc[0], currMail)
                    mailToNodeMap[currMail] = currNode
        for acc in accounts:
            if len(acc) == 2:
                currNode = mailToNodeMap[acc[1]]
                if currNode not in adjlist:
                    adjlist[currNode] = set()
            else:
                currNode = mailToNodeMap[acc[1]]
                if currNode not in adjlist:
                    adjlist[currNode] = set()
                for i in range(2, len(acc)):
                    nextNode = mailToNodeMap[acc[i]]
                    adjlist[currNode].add(nextNode)

        conComps = []
        seen = set()
        for key in adjlist:
            if key not in seen:
                currSeen = set()
                conComps.append([])
                dfs(key, conComps, adjlist, currSeen)
                seen = seen.union(currSeen)
        ans = []
        for comp in conComps:
            currMails = []
            for i in range(len(comp)):
                currMails.append(comp[i].email)
            currMails = sorted(currMails)
            currMails = [comp[0].name] + currMails
            ans.append(currMails)

        return ans


def dfs(node, conComps, adjlist, currSeen):
    conComps[-1].append(node)
    currSeen.add(node)
    if node in adjlist:
        for nbr in adjlist[node]:
            if nbr not in currSeen:
                dfs(nbr, conComps, adjlist, currSeen)


if __name__=="__main__":
    print(Solution().accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
))