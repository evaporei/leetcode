#define CHARSET 26

struct TrieNode {
    struct TrieNode *children[CHARSET];
    bool final;
};

struct TrieNode * empty_node() {
    struct TrieNode *node = malloc(sizeof(struct TrieNode));
    for (int i = 0; i < CHARSET; i++) {
        node->children[i] = NULL;
    }
    node->final = false;
    return node;
}

void freeTrieNode(struct TrieNode *node) {
    if (!node) {
        return;
    }
    for (int i = 0; i < CHARSET; i++) {
        if (node->children[i])
            freeTrieNode(node->children[i]);
    }
    free(node);
}

typedef struct {
    struct TrieNode *root;
} Trie;


Trie* trieCreate() {
    Trie *trie = malloc(sizeof(Trie));
    trie->root = empty_node();
    return trie;
}

void trieInsert(Trie* obj, char* word) {
    struct TrieNode *curr = obj->root;
    for (char *c = word; *c; c++) {
        if (!curr->children[*c - 97]) {
            curr->children[*c - 97] = empty_node();
        }
        curr = curr->children[*c - 97];
    }
    curr->final = true;
}

bool trieSearch(Trie* obj, char* word) {
    struct TrieNode *curr = obj->root;
    for (char *c = word; *c; c++) {
        if (!curr->children[*c - 97]) {
            return false;
        }
        curr = curr->children[*c - 97];
    }
    return curr->final;
}

bool trieStartsWith(Trie* obj, char* prefix) {
    struct TrieNode *curr = obj->root;
    for (char *c = prefix; *c; c++) {
        if (!curr->children[*c - 97]) {
            return false;
        }
        curr = curr->children[*c - 97];
    }
    return true;
}

void trieFree(Trie* obj) {
    freeTrieNode(obj->root);
    free(obj);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/
