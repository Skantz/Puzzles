class Solution:
    def modifiedList(self, nums, head):
        nums = set(nums)
        if not head:
            return None
        while head and head.val in nums:
            head = head.next
        if not head:
            return None
        save = head
        prev = head
        head = head.next
        while head:
            while head and head.val in nums:
                head = head.next
            if not head:
                prev.next = None
                break
            prev.next = head
            prev = head
            head = head.next
        return save
