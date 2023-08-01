#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STACK_INIT_CAP 16
#define panic_if_null(x) \
    if (x == NULL) { \
        perror("memory allocation error"); \
        exit(1); \
    }

struct Stack {
    int len;
    int cap;
    char *ptr;
};

struct Stack stack_new_with_cap(int cap) {
    struct Stack stack;

    stack.len = 0;
    stack.cap = cap;
    stack.ptr = malloc(sizeof(char) * cap);

    panic_if_null(stack.ptr);

    return stack;
}

struct Stack stack_new() {
    return stack_new_with_cap(STACK_INIT_CAP);
}

void stack_grow(struct Stack *stack) {
    if (stack->len >= stack->cap) {
        stack->cap *= 2;
        stack->ptr = realloc(stack->ptr, sizeof(char) * stack->cap);
        panic_if_null(stack->ptr);
    }
}

void stack_push(struct Stack *stack, char c) {
    stack_grow(stack);
    stack->ptr[stack->len] = c;
    stack->len++;
}

char stack_pop(struct Stack *stack) {
    if (stack->len <= 0) {
        return '\0';
    }
    return stack->ptr[--stack->len];
}

void stack_free(struct Stack stack) {
    free(stack.ptr);
}

bool is_even(int n) { return n % 2 == 0; }

bool is_valid(char *s) {
    struct Stack stack;
    char last;
    int final_len;

    if (!is_even(strlen(s))) {
        return false;
    }

    stack = stack_new_with_cap(strlen(s) / 2);
    
    for (char *c = s; *c != '\0'; c++) {
        switch (*c) {
            case '(':
            case '[':
            case '{':
                stack_push(&stack, *c);
                break;
            case ')':
                last = stack_pop(&stack);
                if (last != '(')
                    return false;
                break;
            case ']':
                last = stack_pop(&stack);
                if (last != '[')
                    return false;
                break;
            case '}':
                last = stack_pop(&stack);
                if (last != '{')
                    return false;
                break;
        }
    }

    final_len = stack.len;

    stack_free(stack);

    return final_len == 0;
}

int main() {
    char *inputs[] = {
        "()",
        "()[]{}",
        "(]",
        "(])",
        "([)]",
        "){",
        "([{}{}()][]()()[([])])[{{()}}([])]{({{}{}}())}"
    };
    bool outputs[] = {
        true,
        true,
        false,
        false,
        false,
        false,
        true
    };
    int len = sizeof(outputs) / sizeof(outputs[0]);

    for (int i = 0; i < len; i++) {
        printf("case %d, expected: %s, output: %s\n", i, outputs[i] ? "true" : "false", is_valid(inputs[i]) ? "true" : "false");
    }

    struct Stack stack = stack_new();
    stack_push(&stack, 'e');
    stack_push(&stack, 'v');
    stack_push(&stack, 'a');
    printf("pop: %c\n", stack_pop(&stack));
    printf("pop: %c\n", stack_pop(&stack));
    printf("pop: %c\n", stack_pop(&stack));
    stack_free(stack);
}
