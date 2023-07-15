class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = max(nums)
        i = nums.index(n)
        left = nums[:i]
        right = nums[i + 1:]
        r = TreeNode(n)
        left = self.constructMaximumBinaryTree(left)
        right = self.constructMaximumBinaryTree(right)
        r.left = left
        r.right = right
        return r
