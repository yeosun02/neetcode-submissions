class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int prev_end = intervals[0][1];
        int count = 0;

        for (auto vec : intervals) {
            if (vec[0] < prev_end) { 
                prev_end = min(prev_end, vec[1]);
                count++;
            } else { 
                prev_end = vec[1];
            }
        }

        return count - 1;
    }
};
