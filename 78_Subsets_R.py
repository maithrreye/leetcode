"""
Recursive solution 

time complexity O(2^N)
space complexity O(2^N)

"""


import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        temp1=[]
        self.helper(nums, temp1, 0)
        return self.res
    
    
    def helper(self,nums, temp1,pivot):
        
        #Base 
        #print("temp1",temp1)
        self.res.append(temp1)
        #print("Result",self.res)
        
        #Logic
        for i in range(pivot,len(nums)):
            #print(pivot)
            temp2=copy.deepcopy(temp1)
            temp2.append(nums[i])
            #print(temp2)
            self.helper(nums,temp2,i+1)
            
            
        
