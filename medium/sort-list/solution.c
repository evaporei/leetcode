/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* getMid(struct ListNode *node) {
    struct ListNode *slow = node;
    struct ListNode *fast = node->next;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}

struct ListNode *merge(struct ListNode *left, struct ListNode *right) {
    struct ListNode dummy;
    struct ListNode *tail = &dummy;

    while (left && right) {
        if (left->val <= right->val) {
            tail->next = left;
            left = left->next;
        } else {
            tail->next = right;
            right = right->next;
        }
        tail = tail->next;
    }

    if (left)
        tail->next = left;
    if (right)
        tail->next = right;

    return dummy.next;
}

struct ListNode* sortList(struct ListNode* head) {
    if (!head || !head->next)
        return head;
    
    struct ListNode *left = head;
    struct ListNode *mid = getMid(head);
    struct ListNode *right = mid->next;
    mid->next = NULL;

    left = sortList(left);
    right = sortList(right);

    return merge(left, right);
}
