bool checkIfPangram(char * sentence){
    unsigned int letters = 0;

    for (char *c = sentence; *c != '\0'; c++) {
        letters = letters | (1 << (*c - 97));
    }

    // 0b00000011 11111111 11111111 11111111
    return letters == 0x03ffffff;
}
