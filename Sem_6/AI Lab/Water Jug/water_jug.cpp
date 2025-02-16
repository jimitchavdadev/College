#include <iostream>
#include <queue>
#include <set>
#include <tuple>

using namespace std;

struct State
{
    int jug1, jug2;

    bool operator<(const State &other) const
    {
        return tie(jug1, jug2) < tie(other.jug1, other.jug2);
    }
};

void solveWaterJug(int capacity1, int capacity2, int target)
{
    set<State> visited;
    queue<State> q;

    q.push({0, 0});
    visited.insert({0, 0});

    while (!q.empty())
    {
        State current = q.front();
        q.pop();

        int jug1 = current.jug1, jug2 = current.jug2;

        // Just print the volume state of the jugs
        cout << "State: (" << jug1 << ", " << jug2 << ")" << endl;

        if (jug1 == target || jug2 == target)
        {
            cout << "Solution Found: (" << jug1 << ", " << jug2 << ")" << endl;
            return;
        }

        // Generate next possible states
        vector<State> nextStates = {
            {capacity1, jug2},                                              // Fill Jug1
            {jug1, capacity2},                                              // Fill Jug2
            {0, jug2},                                                      // Empty Jug1
            {jug1, 0},                                                      // Empty Jug2
            {min(jug1 + jug2, capacity1), max(0, jug1 + jug2 - capacity1)}, // Pour Jug2 into Jug1
            {max(0, jug1 + jug2 - capacity2), min(jug1 + jug2, capacity2)}  // Pour Jug1 into Jug2
        };

        // Push the next states into the queue if they haven't been visited
        for (const State &nextState : nextStates)
        {
            if (visited.find(nextState) == visited.end())
            {
                visited.insert(nextState);
                q.push(nextState);
            }
        }
    }

    cout << "No solution found." << endl;
}

int main()
{
    int capacity1 = 4, capacity2 = 3, target = 2;
    cout << "Capacity of bucket 1: " << capacity1 << endl
         << "Capacity of bucket 2: " << capacity2 << endl
         << "Target: " << target << endl
         << endl;
    solveWaterJug(capacity1, capacity2, target);

    return 0;
}
