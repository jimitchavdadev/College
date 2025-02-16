#include <iostream>
#include <vector>
#include <stack>
#include <set>

using namespace std;

// Function to print the graph structure (adjacency list)
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

// Function to perform DFS using a stack
void dfs(int start, const vector<vector<int>> &adjList)
{
    vector<bool> visited(adjList.size(), false);
    stack<int> s;

    s.push(start);
    visited[start] = true;

    cout << "\nDFS Traversal: ";
    while (!s.empty())
    {
        int node = s.top();
        s.pop();

        cout << node << " ";

        // Traverse all adjacent nodes of the current node
        for (int neighbor : adjList[node])
        {
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                s.push(neighbor);
            }
        }
    }
    cout << endl;
}

int main()
{
    // Example graph represented as an adjacency list
    vector<vector<int>> adjList = {
        {},        // 0 (unused)
        {2, 3},    // 1 -> 2, 3
        {1, 4, 5}, // 2 -> 1, 4, 5
        {1},       // 3 -> 1
        {2},       // 4 -> 2
        {2}        // 5 -> 2
    };

    // Print the graph structure
    printGraph(adjList);

    // Perform DFS traversal starting from node 1
    dfs(1, adjList);

    return 0;
}
