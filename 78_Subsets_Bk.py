"""
Recursive solution 

time complexity O(2^N)
space complexity O(N)

Recurse and Backtrack

"""


import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        templist=[]
        self.helper(nums, templist, 0)
        return self.res
    
    
    def helper(self,nums, templist,pivot):
        
        #Base 
        
        temp1=copy.deepcopy(templist)
        #print("temp1",temp1)
        self.res.append(temp1)
        print("Result",self.res)
        
        #Logic
        for i in range(pivot,len(nums)):
            print(pivot)
            #print("templist",templist)
            #ACTION
            templist.append(nums[i])
            print(templist)
            #RECURSE
            self.helper(nums,templist,i+1)
            #BACKTRACK
            templist.pop()
            
            
            
        
