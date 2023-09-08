bool canConstruct(char * ransomNote, char * magazine){
    int letters[26] = {0};
    int r_len = strlen(ransomNote),
        m_len = strlen(magazine);

    for (int i = 0; i < r_len; i++) {
        letters[ransomNote[i] - 97]++;
    }

    for (int i = 0; i < m_len; i++) {
        letters[magazine[i] - 97]--;
    }

    for (int i = 0; i < 26; i++) {
        if (letters[i] > 0)
            return false;
    }

    return true;
}
