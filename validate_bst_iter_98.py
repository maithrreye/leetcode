# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
-> Inorder traversal - Left,Root,Right 
-> compare left with root, root with right and then right with left in the inorder way 
->Stack iterative solution 
-> TC O(N) and SC O(H) ->O(N) stack space


Example =[9,5,13,3,7,11,15,2,4,6,8,10,12,14,16,null,null]
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev=None
        stack_=[]
        while(root or stack_): #root not null or stack not isempty
            while(root):
                stack_.append(root)
                root=root.left
            root=stack_.pop()
            #print(root.val)
            #if prev:
                #print(prev.val,root.val)
            if(prev and prev.val>=root.val):
                return False
            prev=root
            root=root.right
        return True
            
            
        
        
