# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
def flatten(object):
	res = []
	if isinstance(object, list):
		for item in object:
			res.extend(flatten(item))
	if not object.isInteger():
		res.extend(flatten(object))
	else:
		res.append(object.getInteger())
	return res

class NestedIterator:
	def __init__(self, nestedList: [NestedInteger]):
		self.res = flatten(nestedList)
		self.res.reverse()
	def next(self) -> int:
		return self.res.pop()
	def hasNext(self) -> bool:
		return bool(self.res)


# print(flatten([[1,2],[3,4],[5,6],[7,8]]))
# print(flatten([1,[2,[3,4,5],6],7]))
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())