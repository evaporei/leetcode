struct Node {
    int val;
    struct Node *next;
};

struct Queue {
    struct Node *head, *tail;
    int len;
};

struct Queue queue_init() {
    struct Queue queue = {
        .head = NULL,
        .tail = NULL,
        .len = 0,
    };
    return queue;
}

void queue_push(struct Queue *self, int x) {
    struct Node *new_node = malloc(sizeof(struct Node));
    new_node->val = x;
    new_node->next = NULL;
    if (!self->tail) {
        self->head = self->tail = new_node;
    } else {
        self->tail->next = new_node;
        self->tail = self->tail->next;
    }
    self->len++;
}

int queue_pop(struct Queue *self) {
    int item = self->head->val;
    struct Node *next = self->head->next;
    free(self->head);
    self->head = next;
    if (!next) {
        self->tail = NULL;
    }
    self->len--;
    return item;
}

int queue_peek(struct Queue *self) {
    return self->head->val;
}

void free_queue(struct Queue *self) {
    struct Node *curr = self->head;
    while (curr) {
        struct Node *next = curr->next;
        free(curr);
        curr = next;
    }
    self->head = self->tail = NULL;
    self->len = 0;
}

typedef struct {
    struct Queue queue;
} MyStack;


MyStack* myStackCreate() {
    MyStack *obj = malloc(sizeof(MyStack));
    obj->queue = queue_init();
    return obj;
}

void myStackPush(MyStack* obj, int x) {
    queue_push(&obj->queue, x);
    int initial_len = obj->queue.len;
    for (int i = 1; i < initial_len; i++) {
        queue_push(&obj->queue, queue_pop(&obj->queue));
    }
}

int myStackPop(MyStack* obj) {
    return queue_pop(&obj->queue);
}

int myStackTop(MyStack* obj) {
    return queue_peek(&obj->queue);
}

bool myStackEmpty(MyStack* obj) {
    return obj->queue.len == 0;
}

void myStackFree(MyStack* obj) {
    free_queue(&obj->queue);
    free(obj);
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
