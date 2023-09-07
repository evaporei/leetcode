int cstrcmp(const void *a, const void *b) {
    return *(const char*)a - *(const char*)b;
}

bool isAnagram(char *s, char *t) {
    int s_len = strlen(s),
        t_len = strlen(t);
    if (s_len != t_len)
      return false;
    qsort(s, s_len, sizeof(char), cstrcmp);
    qsort(t, t_len, sizeof(char), cstrcmp);
    return strcmp(s, t) == 0;
}
