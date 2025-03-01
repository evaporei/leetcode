typedef struct Counter {
    int values[26];
} Counter;

Counter counter_of_str(char *s) {
    Counter counter = {0};
    for (char *ch = s; *ch; ch++)
        counter.values[*ch - 'a'] += 1;
    return counter;
}

int hash_counter(Counter c) {
    long long h = 0;
    long long p = 31, mod = 1e9 + 9;
    
    for (int i = 0; i < 26; i++) {
        h = (h * p + c.values[i]) % mod;
    }
    return (int)h;
}

typedef struct Node {
    int key;
    char **values;
    int values_len;
    struct Node *next;
} Node;

#define NODE_COUNT 1000

typedef struct Map {
    Node *buckets[NODE_COUNT];
    int len;
} Map;

void map_init(Map *map) {
    Node *mem = malloc(sizeof(Node) * NODE_COUNT);
    for (int i = 0; i < NODE_COUNT; i++) {
        map->buckets[i] = &mem[i];
        map->buckets[i]->key = -1;
        map->buckets[i]->values = NULL;
        map->buckets[i]->values_len = 0;
        map->buckets[i]->next = NULL;
    }
    map->len = 0;
}

void map_insert(Map *map, char *value) {
    size_t value_len = strlen(value);
    Counter counter = counter_of_str(value);
    int key = hash_counter(counter);
    int idx = key % NODE_COUNT;
    Node *curr = map->buckets[idx];
    while (curr->next) {
        if (curr->key == key) {
            curr->values = realloc(curr->values, sizeof(char*) * (++curr->values_len));
            curr->values[curr->values_len-1] = strdup(value);
            return;
        }
        curr = curr->next;
    }
    if (curr->key == key) {
        curr->values = realloc(curr->values, sizeof(char*) * (++curr->values_len));
        curr->values[curr->values_len-1] = strdup(value);
        return;
    }
    map->len += 1;
    Node *new_node = malloc(sizeof(Node));
    new_node->key = key;
    new_node->values_len = 1;
    new_node->values = malloc(sizeof(char*));
    new_node->values[0] = strdup(value);
    new_node->next = NULL;
    curr->next = new_node;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    Map map;
    map_init(&map);
    for (int i = 0; i < strsSize; i++) {
        char *s = strs[i];
        map_insert(&map, s);
    }

    char ***groups = malloc(sizeof(char*) * map.len);
    *returnColumnSizes = malloc(sizeof(int) * map.len);
    int g = 0;
    for (int i = 0; i < NODE_COUNT; i++) {
        // first is dummy node
        Node *curr = map.buckets[i]->next;
        while (curr) {
            groups[g] = malloc(sizeof(char**) * curr->values_len);
            (*returnColumnSizes)[g] = curr->values_len;
            for (int j = 0; j < curr->values_len; j++) {
                groups[g][j] = curr->values[j];
            }
            g++;
            curr = curr->next;
        }
    }

    *returnSize = map.len;// or `g`
    return groups;
}
