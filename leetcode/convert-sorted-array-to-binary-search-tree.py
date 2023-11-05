class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        root = TreeNode(nums[n//2])
        root.left = self.sortedArrayToBST(nums[:n//2])
        root.right = self.sortedArrayToBST(nums[n//2 + 1:])
        return root
