bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int low = 0,
        high = matrixSize * matrixColSize[0] - 1;
    
    while (low <= high) {
        int mid = (low + high) / 2;

        int row = mid / matrixColSize[0];
        int column = mid % matrixColSize[0];

        if (matrix[row][column] == target)
            return true;
        else if (matrix[row][column] > target)
            high = mid - 1;
        else // if (matrix[row][column] < target)
            low = mid + 1;
    }

    return false;
}
