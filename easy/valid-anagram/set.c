bool isAnagram(char *s, char *t) {
  int s_letters[26] = {0};
  int t_letters[26] = {0};
  int s_len = strlen(s),
      t_len = strlen(t);

  if (s_len != t_len)
    return false;

  
  for (int i = 0; i < s_len; i++) {
    s_letters[s[i] - 97]++;
  }

  for (int i = 0; i < t_len; i++) {
    t_letters[t[i] - 97]++;
  }

  for (int i = 0; i < 26; i++) {
    if (s_letters[i] != t_letters[i]) {
      return false;
    }
  }

  return true;
}
