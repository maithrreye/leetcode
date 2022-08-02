# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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

"""
Time Complexity  constructor: O(N+L) rest of methods are O(1) here N is integer in the input and L is total no of list in the input 
Space complexity : O(N+L) where N is integer in the input and L is list in the input 

"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack=[]
        if nestedList:
            self.stack.append(iter( nestedList))
            print("stack",self.stack)
            self.ptr=None
  
    def next(self) -> int:
        val=self.ptr
        self.ptr= None
        return val
        
    
    def hasNext(self) -> bool:
        while(len(self.stack)>0 and self.ptr==None):
            iterator=self.stack[-1] #check top and you are not popping out 
            print("iterator in hasNext",iterator)
            currentNI=next(iterator,None)
            print(currentNI)
            
            if currentNI == None:
                self.stack.pop()
                continue #continue to next iteration
            
            nestedInt=currentNI
            if nestedInt.isInteger():
                self.ptr= nestedInt.getInteger()
                return True 
            else:
                self.stack.append(iter(nestedInt.getList()))
            print("stack",self.stack)
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
