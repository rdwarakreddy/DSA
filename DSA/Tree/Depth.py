class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        root.insert(0, "None")
        last_index = len(root) - 1
        depth = 0
        while last_index == 1:
            last_index = (last_index - 1) // 2
            depth += 1

        return depth + 1


# Example usage
root = [3, 9, 20, None, None, 15, 7]  # Example binary tree in array form
solution = Solution()
print(solution.maxDepth(root))  # Output: 3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
