struct Node {
    int val;
    struct Node *next;
};

struct Stack {
    struct Node *head;
    int len;
};

struct Stack stack_init() {
    struct Stack obj;
    obj.head = NULL;
    obj.len = 0;
    return obj;
}

void stack_push(struct Stack *self, int x) {
    struct Node *new_node = malloc(sizeof(struct Node));
    new_node->val = x;
    new_node->next = self->head;
    self->head = new_node;
    self->len++;
}

int stack_pop(struct Stack *self) {
    int item = self->head->val;
    struct Node *next = self->head->next;
    free(self->head);
    self->head = next;
    self->len--;
    return item;
}

int stack_peek(struct Stack *self) {
    return self->head->val;
}

bool stack_is_empty(struct Stack self) {
    return self.len == 0;
}

// beaurifu
void free_stack(struct Stack *stack) {
    while (stack->len) {
        stack_pop(stack);
    }
}

typedef struct {
    struct Stack push;
    struct Stack pop;
} MyQueue;


MyQueue* myQueueCreate() {
    MyQueue *obj = malloc(sizeof(MyQueue));
    obj->push = stack_init();
    obj->pop = stack_init();
    return obj;
}

void myQueuePush(MyQueue* obj, int x) {
    stack_push(&obj->push, x);
}

void myQueue_populate_pop_stack(MyQueue *self) {
    if (stack_is_empty(self->pop))
        while (!stack_is_empty(self->push)) {
            int element = stack_pop(&self->push);
            stack_push(&self->pop, element);
        }
}

int myQueuePop(MyQueue* obj) {
    myQueue_populate_pop_stack(obj);
    return stack_pop(&obj->pop);
}

int myQueuePeek(MyQueue* obj) {
    myQueue_populate_pop_stack(obj);
    return stack_peek(&obj->pop);
}

bool myQueueEmpty(MyQueue* obj) {
    return stack_is_empty(obj->push) && stack_is_empty(obj->pop);
}

void myQueueFree(MyQueue* obj) {
    free_stack(&obj->push);
    free_stack(&obj->pop);
    free(obj);
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);
 
 * int param_2 = myQueuePop(obj);
 
 * int param_3 = myQueuePeek(obj);
 
 * bool param_4 = myQueueEmpty(obj);
 
 * myQueueFree(obj);
*/
