class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> rows, cols;
        for (int row = 0; row < matrix.size(); ++row) {
            for (int col = 0; col < matrix[0].size(); ++col) {
                if (matrix[row][col] == 0) {
                    rows.push_back(row);
                    cols.push_back(col);
                }
            }
        }

        for (const int& row : rows) {
            for (int col = 0; col < matrix[0].size(); ++col) {
                matrix[row][col] = 0;
            }
        }

        for (const int& col : cols) {
            for (int row = 0; row < matrix.size(); ++row) {
                matrix[row][col] = 0;
            }
        }
    }
};