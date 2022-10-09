"""
TC=O(N 2^N)
SC=O(N)


"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        self.res=[]
        templist=[]
        self.helper(nums, templist, 0)
        return self.res
    
    def helper(self,nums, templist,pivot):
        #Base 
        temp1=copy.deepcopy(templist)
        
        self.res.append(templist.copy())
        print("Result",self.res)
        
        #Logic
        for i in range(pivot,len(nums)):
            #print(pivot)
            #print("templist",templist)
            if i!=pivot and nums[i]==nums[i-1]:
                continue
            templist.append(nums[i])
            #print(templist)
     
            self.helper(nums,templist,i+1)
         
            templist.pop()
