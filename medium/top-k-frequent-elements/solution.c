typedef struct Count {
    int n, freq;
} Count;

typedef struct Node {
    Count count;
    struct Node *next;
} Node;

#define NODE_COUNT 1000

typedef struct Map {
    Node *entries[NODE_COUNT];
    int len;
} Map;

void map_init(Map *map) {
    // init dummy nodes
    Node *mem = malloc(sizeof(Node) * NODE_COUNT);
    for (int i = 0; i < NODE_COUNT; i++) {
        map->entries[i] = &mem[i];
        map->entries[i]->count = (Count){21000, 21000};
        map->entries[i]->next = NULL;
    }
    map->len = 0;
}

void map_insert(Map *map, int n) {
    int idx = abs(n) % NODE_COUNT;
    Node *curr = map->entries[idx];
    while (curr->next) {
        if (curr->count.n == n) {
            curr->count.freq++;
            return;
        }
        curr = curr->next;
    }
    if (curr->count.n == n) {
        curr->count.freq++;
        return;
    }
    Node *new_node = malloc(sizeof(Node));
    new_node->count = (Count){n, 1};
    new_node->next = NULL;
    curr->next = new_node;
    map->len++;
}

int desc_cmp_count(const void *a, const void *b) {
    Count x = *(Count*) a;
    Count y = *(Count*) b;
    return y.freq - x.freq;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    Map map;
    map_init(&map);
    for (int i = 0; i < numsSize; i++) {
        map_insert(&map, nums[i]);
    }

    Count *sorted_by_freq = malloc(sizeof(Count) * map.len);
    int j = 0;
    for (int i = 0; i < NODE_COUNT; i++) {
        // skip dummy node
        Node *curr = map.entries[i]->next;
        while (curr) {
            sorted_by_freq[j++] = curr->count;
            curr = curr->next;
        }
    }
    qsort(sorted_by_freq, j, sizeof(Count), desc_cmp_count);
    
    int *top_k = malloc(sizeof(int) * k);
    for (int i = 0; i < k; i++) {
        top_k[i] = sorted_by_freq[i].n;
    }
    *returnSize = k;
    return top_k; 
}
