#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

struct Node
{
    vector<vector<int>> state;
    int x, y; // Position of blank (0)
    string path;
};

vector<vector<int>> goal = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

// Possible moves: Left, Right, Up, Down
vector<pair<int, int>> moves = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

// Convert matrix to string for visited state tracking
string serialize(const vector<vector<int>> &state)
{
    string s;
    for (auto &row : state)
        for (int val : row)
            s += to_string(val);
    return s;
}

// Function to perform BFS (Shortest path guaranteed)
void solveBFS(vector<vector<int>> start)
{
    queue<Node> q;
    set<string> visited;
    int x, y;

    // Find blank tile position
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (start[i][j] == 0)
            {
                x = i;
                y = j;
            }

    q.push({start, x, y, ""});
    visited.insert(serialize(start));

    while (!q.empty())
    {
        Node node = q.front();
        q.pop();

        if (node.state == goal)
        {
            cout << "Solved using BFS! Path: " << node.path << endl;
            return;
        }

        for (int i = 0; i < 4; i++)
        {
            int nx = node.x + moves[i].first;
            int ny = node.y + moves[i].second;
            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3)
            {
                vector<vector<int>> newState = node.state;
                swap(newState[node.x][node.y], newState[nx][ny]);

                if (visited.find(serialize(newState)) == visited.end())
                {
                    visited.insert(serialize(newState));
                    q.push({newState, nx, ny, node.path + to_string(i)});
                }
            }
        }
    }
    cout << "No solution found using BFS!" << endl;
}

int main()
{
    vector<vector<int>> start = {{1, 3, 2}, {5, 4, 6}, {7, 0, 8}};

    cout << "Solving with BFS...\n";
    solveBFS(start);

    return 0;
}
