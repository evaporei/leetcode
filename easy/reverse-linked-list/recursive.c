/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* recur(struct ListNode* curr, struct ListNode* prev) {
    if (!curr)
        return prev;
    struct ListNode *next = curr->next;
    curr->next = prev;
    return recur(next, curr);
}

struct ListNode* reverseList(struct ListNode* head) {
    return recur(head, NULL);
}
