class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        if (head->next == nullptr) {
            return head;
        }
        if ((head->next)->val == head->val) {
            head = head->next;
            head = deleteDuplicates(head);
        }
        else {
            head->next = deleteDuplicates(head->next);
        }
        return head;
    }
};
