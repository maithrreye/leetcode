"""
 Using for-loop based recursion with backtracking
//TC: O(2^(m*n)) - m is the number of candidates and n is the target
//SC: O(2^(m*n)) (everytime make a new arraylist)

Templist is a reference in backtracking so you take deepcopy


"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res=[]
        templist=[]
        if candidates is None or len(candidates)==0:
            return self.res
        self.backtrack(candidates,target,templist,0,0)
        return self.res
    
    def backtrack(self,candidates,target,templist,sum1,pivot):
       # print(sum1,pivot,templist)
        if (sum1>target):
            return 
        if(sum1==target):
            temp1=copy.deepcopy(templist)
            self.res.append(temp1)
            return
        #logic
        for i in range(pivot,len(candidates)):
            #action
            templist.append(candidates[i])
            #recurse
            self.backtrack(candidates,target,templist,sum1+candidates[i],i)
            #backtrack
            #print("backtrack")
            templist.pop()
        
        
    
  
