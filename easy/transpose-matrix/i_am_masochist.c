/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    int **result = malloc(sizeof(int*) * *matrixColSize);
    *returnSize = *matrixColSize;
    *returnColumnSizes = malloc(sizeof(int) * *matrixColSize);
    for (int i = 0; i < *matrixColSize; i++) {
        result[i] = malloc(sizeof(int) * matrixSize);
        (*returnColumnSizes)[i] = matrixSize;
        for (int j = 0; j < matrixSize; j++) {
            result[i][j] = matrix[j][i];
        }
    }
    return result;
}
