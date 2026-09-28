class FenwickMax:
    def __init__ (self, size):
        self.tree = [0] * size
    def query(self, index):
        ret = -1
        while index > 0:
            ret = max(ret, self.tree[index])
            index -= (index & -index)
        return ret
    def update(self, index, value):
        while index < len(self.tree):
            self.tree[index] = max(self.tree[index], value)
            index +=  (index & -index)
class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        maxsum = 0
        endtree = FenwickMax(size = len(events))
        starttree = FenwickMax(size = len(events))
        for e in events:
            starttree.update(index = e[0], value=e[2] )
            endtree.update(index = e[1]  , value=e[2])
        return maxsum 
sol = Solution()
e = [[[1,3,2],[4,5,2],[2,4,3]],
[[1,3,2],[4,5,2],[1,5,5]],
[[1,5,3],[1,5,1],[6,6,5]]]
for event in e:
    print(sol.maxTwoEvents(events=event))

