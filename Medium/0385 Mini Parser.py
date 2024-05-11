# https://leetcode.com/problems/mini-parser/description/


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # eval("[1,2,3]") => [1,2,3] it'll convert string of list to list
        return self.find(eval(s))
    
    def find(self,s):
		# if our elment s is type of int we'll return new NestedInteger of that value
        if type(s) == type(1):
            return NestedInteger(s)
			
		# create a new object that will contain our elements of type NestedInteger
        n = NestedInteger()
        
        for x in s:
			# traverse  the list s and recursively find all nestedIntegers and add them in container n
			# recursion will handle multiple nested lists
            n.add(self.find(x))
        return n
        
