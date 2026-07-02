class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool top_row = false;
        for (int c = 0; c < n; ++c) {
            if (matrix[0][c] == 0) {
                top_row = true;
                break;
            }
        }

        for (int r = 1; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (matrix[r][c] == 0) {
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }

        // cout << top_row << endl;
        // for (int r = 0; r < m; ++r) {
        //     for (int c = 0; c < n; ++c) {
        //         cout << matrix[r][c] << " ";
        //     }
        //     cout << endl;
        // }
        for (int r = 1; r < m; ++r) {
            if (matrix[r][0] == 0) {
                for (int c = 1; c < n; ++c) {
                    matrix[r][c] = 0;
                }
            }
        }
        
        for (int c = 0; c < n; ++c) {
            if (matrix[0][c] == 0) {
                for (int r = 1; r < m; ++r) {
                    matrix[r][c] = 0;
                }
            }
        }

        if (top_row) {
            for (int c = 0; c < n; ++c) {
                matrix[0][c] = 0;
            }
        }
    }
};
