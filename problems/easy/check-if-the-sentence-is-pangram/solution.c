bool checkIfPangram(char * sentence){
    bool letters[26] = { false };

    for (char *c = sentence; *c != '\0'; c++) {
        letters[*c - 97] = true;
    }

    for (int i = 0; i < 26; i++) {
        if (letters[i] == false) {
            return false;
        }
    }

    return true;
}
