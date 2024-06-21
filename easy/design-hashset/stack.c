#define MAX_KEYS 1000001

typedef struct {
    bool entries[MAX_KEYS];
} MyHashSet;

MyHashSet* myHashSetCreate() {
    MyHashSet *obj = malloc(sizeof(MyHashSet));
    for (int i = 0; i < MAX_KEYS; i++) {
        obj->entries[i] = false;
    }
    return obj;
}

void myHashSetAdd(MyHashSet* obj, int key) {
    obj->entries[key] = true;
}

void myHashSetRemove(MyHashSet* obj, int key) {
    obj->entries[key] = false;
}

bool myHashSetContains(MyHashSet* obj, int key) {
    return obj->entries[key];
}

void myHashSetFree(MyHashSet* obj) {
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
