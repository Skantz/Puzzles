struct ListNode_ {
  int v;
  struct ListNode_ *x;
};

struct ListNode_* removeElements(struct ListNode_* head, int v) {
    while (head && head->v == v) {
        head = head->x;
    }
    struct ListNode_* save = head;
    while (head && head->x) {
        while (head->x && head->x->v == v)
            head->x = head->x->x;
        head = head->x;
    }
    return save;
}
