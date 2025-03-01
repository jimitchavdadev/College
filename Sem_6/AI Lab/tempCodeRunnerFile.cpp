#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cmath>

using namespace std;

struct Node {
    vector<vector<int>> state;
    int x, y; // Position of blank
    int cost, heuristic;
    string path;

    bool operator>(const Node &other) const {
        return (cost + heuristic) > (other.cost + other.heuristic);
    }
};

vector<vector<int>> goal = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
vector<pair<int, int>> moves = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

// Convert state to string
string serialize(const vector<vector<int>> &state) {
    string s;
    for (auto &row : state)
        for (int val : row)
            s += to_string(val);
    return s;
}

// Manhattan Distance heuristic
int heuristic(const vector<vector<int>> &state) {
    int h = 0;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (state[i][j] != 0) {
                int goalX = (state[i][j] - 1) / 3;
                int goalY = (state[i][j] - 1) % 3;
                h += abs(i - goalX) + abs(j - goalY);
            }
    return h;
}

// Solve using A* Search
void solveAStar(vector<vector<int>> start) {
    priority_queue<Node, vector<Node>, greater<Node>> pq;
    map<string, int> visited;
    int x, y;

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (start[i][j] == 0) { x = i; y = j; }

    pq.push({start, x, y, 0, heuristic(start), ""});
    visited[serialize(start)] = 0;

    while (!pq.empty()) {
        Node node = pq.top();
        pq.pop();

        if (node.state == goal) {
            cout << "Solved using A* Search! Path: " << node.path << " Steps: " << node.cost << endl;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = node.x + moves[i].first;
            int ny = node.y + moves[i].second;
            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                vector<vector<int>> newState = node.state;
                swap(newState[node.x][node.y], newState[nx][ny]);

                int newCost = node.cost + 1;
                string serialized = serialize(newState);
                
                if (visited.find(serialized) == visited.end() || newCost < visited[serialized]) {
                    visited[serialized] = newCost;
                    pq.push({newState, nx, ny, newCost, heuristic(newState), node.path + to_string(i)});
                }
            }
        }
    }
    cout << "No solution found using A*!" << endl;
}

int main() {
    vector<vector<int>> start = {{1, 2, 3}, {4, 5, 6}, {7, 0, 8}};
    
    cout << "Solving with A* Search...\n";
    solveAStar(start);

    return 0;
}
