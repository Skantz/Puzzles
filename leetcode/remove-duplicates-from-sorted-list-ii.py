class Solution:
    def deleteDuplicates(self, head):
        seen = set()
        dups = set()
        save = head
        while head:
            if head.val in seen:
                dups.add(head.val)
            else:
                seen.add(head.val)
            head = head.next
        return self.modified_list(dups, save)

    def modified_list(self, nums, head):
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
