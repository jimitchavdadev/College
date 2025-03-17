#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void printGraph(const vector<vector<int>> &adjList)
{
    cout << "Graph Structure (Adjacency List):" << endl;
    for (int i = 1; i < adjList.size(); ++i)
    {
        cout << i << " -> ";
        for (int neighbor : adjList[i])
        {
            cout << neighbor << " ";
        }
        cout << endl;
    }
}

void bfs(int start, vector<vector<int>> &adjList)
{
    vector<bool> visited(adjList.size(), false);
    queue<int> q;

    q.push(start);
    visited[start] = true;

    cout << "\nBFS Traversal: ";
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : adjList[node])
        {
            if (!visited[neighbor])
            {
                q.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
    cout << endl;
}

int main()
{
    vector<vector<int>> adjList = {
        {},        // 0 (unused)
        {2, 3},    // 1 -> 2, 3
        {1, 4, 5}, // 2 -> 1, 4, 5
        {1},       // 3 -> 1
        {2},       // 4 -> 2
        {2}        // 5 -> 2
    };

    printGraph(adjList);

    bfs(1, adjList);

    return 0;
}
