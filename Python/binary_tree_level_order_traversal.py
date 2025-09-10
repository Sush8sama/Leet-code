

"""
[September 10th 2025]
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

"""
from typing import Optional, List 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # To find out how many children each level has we check the amount of parent of the previous level.
        ans = []

        if root == None:
            return ans
        
        def traverseTree(ans, parents):
            if len(parents) == 0:
                return ans
            else:

                newParents = []
                newValues = []

                for node in parents:
                    if node is not None:
                        if node.left != None:
                            newParents.append(node.left)
                        if node.right != None:
                            newParents.append(node.right)
                        newValues.append(node.val)
                ans.append(newValues)
                
                return traverseTree(ans, newParents)
                    
        return traverseTree(ans, [root])