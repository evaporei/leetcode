#define MAX_ENTRIES 1000

struct Node {
    int key;
    struct Node *next;
};

struct Node *dummy_node() {
    struct Node *dummy = malloc(sizeof(struct Node));
    dummy->key = -1;
    dummy->next = NULL;
    return dummy;
}

typedef struct {
    struct Node *buckets[MAX_ENTRIES];
} MyHashSet;

MyHashSet* myHashSetCreate() {
    MyHashSet *obj = malloc(sizeof(MyHashSet));
    for (int i = 0; i < MAX_ENTRIES; i++) {
        obj->buckets[i] = dummy_node();
    }
    return obj;
}

int hash(int key) {
    return key % MAX_ENTRIES;
}

void myHashSetAdd(MyHashSet* obj, int key) {
    struct Node *curr = obj->buckets[hash(key)];
    while (curr) {
        if (curr->key == key) {
            return;
        }
        curr = curr->next;
    }
    struct Node *new_node = malloc(sizeof(struct Node));
    new_node->key = key;
    new_node->next = obj->buckets[hash(key)];
    obj->buckets[hash(key)] = new_node;
}

void myHashSetRemove(MyHashSet* obj, int key) {
    struct Node *prev = NULL;
    struct Node *curr = obj->buckets[hash(key)];

    while (curr) {
        if (curr->key == key) {
            if (prev) {
                prev->next = curr->next;
            } else {
                obj->buckets[hash(key)] = curr->next;
            }
            free(curr);
            return;
        }
        prev = curr;
        curr = curr->next;
    }
}

bool myHashSetContains(MyHashSet* obj, int key) {
    struct Node *curr = obj->buckets[hash(key)];
    while (curr) {
        if (curr->key == key)
            return true;
        curr = curr->next;
    }
    return false;
}

void myHashSetFree(MyHashSet* obj) {
    for (int i = 0; i < MAX_ENTRIES; i++) {
        struct Node *curr = obj->buckets[i];
        while (curr) {
            struct Node *next = curr->next;
            free(curr);
            curr = next;
        }
    }
    free(obj);
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 
 * myHashSetRemove(obj, key);
 
 * bool param_3 = myHashSetContains(obj, key);
 
 * myHashSetFree(obj);
*/

