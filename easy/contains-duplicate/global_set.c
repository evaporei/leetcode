#include <limits.h>

#define INVALID_VALUE INT_MIN

typedef struct Node {
    int value;
    struct Node *next;
} Node;

#define NODE_COUNT 1000

typedef struct Set {
    Node *buckets[NODE_COUNT];
} Set;

void set_init(Set *set) {
    // do one big alloc instead of per iteration
    Node *mem = malloc(sizeof(Node) * NODE_COUNT);
    // setup dummy nodes
    for (int i = 0; i < NODE_COUNT; i++) {
        set->buckets[i] = &mem[i];
        set->buckets[i]->value = INVALID_VALUE;
        set->buckets[i]->next = NULL;
    }
}

bool set_add(Set *set, int n) {
    int idx = abs(n) % NODE_COUNT; // very good hashing
    Node *curr = set->buckets[idx];
    while (curr->next) {
        if (curr->value == n)
            return true;
        curr = curr->next;
    }
    if (curr->value == n)
        return true;
    curr->next = malloc(sizeof(Node));
    curr->value = n;
    curr->next = NULL;
    return false;
}

// to avoid stack overflow lol
Set set;

bool containsDuplicate(int* nums, int numsSize) {
    set_init(&set);
    for (int i = 0; i < numsSize; i++) {
        if (set_add(&set, nums[i])) {
            return true;
        }
    }
    return false;
}
