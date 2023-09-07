#define max(x, y) ((x) > (y) ? (x) : (y))

char *strrev(char *str) {
    char *p1, *p2;

    if (!str || !*str)
        return str;

    for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2) {
        *p1 ^= *p2;
        *p2 ^= *p1;
        *p1 ^= *p2;
    }

    return str;
}

char *addBinary(char *a, char *b) {
    strrev(a); strrev(b);

    int a_len = strlen(a),
        b_len = strlen(b),
        max_len = max(a_len, b_len);

    // +1 -> if it carries, +1 -> to hold \0
    char *sum = malloc(sizeof(char) * (max_len + 2));
    int carry = 0, i, digit_a, digit_b, total;
    
    for (i = 0; i < max_len; i++) {
        digit_a = i < a_len ? a[i] - '0' : 0;
        digit_b = i < b_len ? b[i] - '0' : 0;

        total = digit_a + digit_b + carry;
        sum[i] = total % 2 + '0';
        carry = total / 2;
    }

    if (carry) {
        sum[i++] = '1';
    }
    sum[i] = '\0';

    return strrev(sum);
}
