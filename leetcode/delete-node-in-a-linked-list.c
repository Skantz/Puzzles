struct ListNode_ {
  int v;
  struct ListNode_ *nxt;
};

void deleteNode(struct ListNode_* n) {
    *n = *n->nxt;
}
