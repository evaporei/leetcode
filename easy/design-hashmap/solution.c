
#define MAX_ENTRIES 1000

struct Node {
    int key, val;
    struct Node *next;
};

struct Node *dummy_node() {
    struct Node *dummy = malloc(sizeof(struct Node));
    dummy->key = -1;
    dummy->val = -1;
    dummy->next = NULL;
    return dummy;
}

typedef struct {
    struct Node *buckets[MAX_ENTRIES];
} MyHashMap;

MyHashMap* myHashMapCreate() {
    MyHashMap *obj = malloc(sizeof(MyHashMap));
    for (int i = 0; i < MAX_ENTRIES; i++) {
        obj->buckets[i] = dummy_node();
    }
    return obj;
}

int hash(int key) {
    return key % MAX_ENTRIES;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    struct Node *curr = obj->buckets[hash(key)];
    while (curr) {
        if (curr->key == key) {
            curr->val = value;
            return;
        }
        curr = curr->next;
    }
    struct Node *new_node = malloc(sizeof(struct Node));
    new_node->key = key;
    new_node->val = value;
    new_node->next = obj->buckets[hash(key)];
    obj->buckets[hash(key)] = new_node;
}

int myHashMapGet(MyHashMap* obj, int key) {
    struct Node *curr = obj->buckets[hash(key)];
    while (curr->next) {
        if (curr->key == key)
            return curr->val;
        curr = curr->next;
    }
    return curr->val;
}

void myHashMapRemove(MyHashMap* obj, int key) {
    struct Node *prev = obj->buckets[hash(key)];
    struct Node *curr = prev->next;

    if (prev->key == key) {
        obj->buckets[hash(key)] = curr;
        free(prev);
        return;
    }

    while (curr) {
        if (curr->key == key) {
            prev->next = curr->next;
            free(curr);
            return;
        }
        prev = curr;
        curr = curr->next;
    }
}

void myHashMapFree(MyHashMap* obj) {
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
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 
 * int param_2 = myHashMapGet(obj, key);
 
 * myHashMapRemove(obj, key);
 
 * myHashMapFree(obj);
*/
