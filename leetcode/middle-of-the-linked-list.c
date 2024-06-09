struct ListNode_ {
  int v;
  struct ListNode_ *x;
};

struct ListNode_* middleNode(struct ListNode_* head) {
  int n = 0;
  struct ListNode_* save = head;
  while (head) {
    head = head->x;
    n++;
  }
  int m = 0;
  while (m < (n/2)) {
    save = save->x;
    m++;
  }
  return save;
}
