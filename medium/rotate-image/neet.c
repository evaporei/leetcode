void rotate(int** m, int matrixSize, int* matrixColSize) {
    int left = 0,
        right = matrixSize - 1;
    
    while (left < right) {
        for (int i = 0; i < (right - left); i++) {
            int top = left,
                bottom = right;
            
            // save
            int top_left = m[top][left + i];

            m[top][left + i] = m[bottom - i][left];
            
            m[bottom - i][left] = m[bottom][right - i];

            m[bottom][right - i] = m[top + i][right];

            m[top + i][right] = top_left;
        }

        left += 1;
        right -= 1;
    }

}
