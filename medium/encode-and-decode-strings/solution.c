#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

#define SEPARATOR "#"

char *encode(char **input, int input_len) {
    char *encoded = NULL;
    int e = 0;
    for (int i = 0; i < input_len; i++) {
        char *s = input[i];
        size_t s_len = strlen(s);
        char s_len_str[32];
        sprintf(s_len_str, "%d", (int) s_len);
        size_t total_len = strlen(s_len_str) + strlen(SEPARATOR) + s_len;

        encoded = realloc(encoded, (e + total_len) * sizeof(char) + 1);
        sprintf(&encoded[e], "%s%s%s", s_len_str, SEPARATOR, s);
        e += total_len;
    }
    encoded[e] = '\0';
    return encoded;
}

char **decode(char *encoded, int *out_len) {
    // I gave up writing to a triple pointer out parameter
    char **out = NULL;
    int i = 0;
    *out_len = 0;
    while (i < strlen(encoded)) {
        int j = i;
        while (encoded[j] != SEPARATOR[0]) j++;
        char *s_len_str = strndup(&encoded[i], j - i);
        int s_len = atoi(s_len_str);
        j++; // SEPARATOR
        out = realloc(out, (*out_len + 1) * sizeof(char*));
        out[*out_len] = strndup(&encoded[j], s_len);
        (*out_len)++;
        j += s_len;
        i = j;
    }
    return out;
}

typedef struct TestCase {
    char **input;
    int input_len;
} TestCase;

void encode_and_decode_test(void) {
    // setup
    TestCase cases[2] = {0};
    int c = 0;

    cases[c].input_len = 4;
    cases[c].input = malloc(cases[c].input_len * sizeof(char*));
    char *input0[] = {"neet","code","love","you"};
    for (int i = 0; i < cases[c].input_len; i++) {
        cases[c].input[i] = input0[i];
    }
    c++;

    cases[c].input_len = 4;
    cases[c].input = malloc(cases[c].input_len * sizeof(char*));
    char *input1[] = {"we","say",":","yes"};
    for (int i = 0; i < cases[c].input_len; i++) {
        cases[c].input[i] = input1[i];
    }
    c++;

    // test
    for (int i = 0; i < c; i++) {
        char *encoded = encode(cases[i].input, cases[i].input_len);
        /* printf("encoded: %s\n", encoded); */
        int decoded_len = 0;
        char **decoded = decode(encoded, &decoded_len);
        /* printf("decoded_len %d\n", decoded_len); */
        assert(decoded_len == cases[i].input_len);
        for (int j = 0; j < decoded_len; j++) {
            /* printf("decoded[j] = %s, cases[i].input[j] = %s\n", decoded[j], cases[i].input[j]); */
            assert(strcmp(decoded[j], cases[i].input[j]) == 0);
        }
        printf("test case %d passed!\n", i);
    }
}

int main(void) {
    encode_and_decode_test();
    return 0;
}
