void rotate(int** m, int matrixSize, int* matrixColSize) {
    // transpose
    for (int i = 0; i < matrixSize; i++) {
        for (int j = i; j < *matrixColSize; j++) {
            int tmp = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = tmp;
        }
    }

    // reverse each row
    for (int i = 0; i < matrixSize; i++) {
        int end = *matrixColSize - 1;
        for (int j = 0; j < *matrixColSize / 2; j++) {
            int tmp = m[i][j];
            m[i][j] = m[i][end];
            m[i][end] = tmp;
            end--;
        }
    }
}
