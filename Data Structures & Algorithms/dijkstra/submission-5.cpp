#include <queue>

class Solution {
public:
    unordered_map<int, int> shortestPath(int n, vector<vector<int>>& edges, int src) {
        vector<vector<pair<int, int>>> adj_list(n);
        for (const auto& edge : edges) {
            int s = edge[0];
            int d = edge[1];
            int w = edge[2];
            adj_list[s].push_back({d, w});
        }

        unordered_map<int, int> distance;
        priority_queue<pair<int, int>> min_heap;
        min_heap.push({0, src});

        while (min_heap.size() > 0) {
            auto [weight, dst] = min_heap.top();
            min_heap.pop();
            if (distance.contains(dst)) {
                continue;
            }
            weight *= -1;
            distance[dst] = weight;

            for (const auto& [d, w] : adj_list[dst]) {
                if (!distance.contains(d)) { 
                    min_heap.push({-(w + weight), d});
                }
            }
        }

        for (int i = 0; i < n; ++i) { 
            if (!distance.contains(i)) { 
                distance[i] = -1;
            }
        }

        return distance;
    }
};
