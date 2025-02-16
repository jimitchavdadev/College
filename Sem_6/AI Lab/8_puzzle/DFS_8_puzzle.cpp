#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;

// Puzzle state representation
struct PuzzleState
{
    vector<int> board;
    string moves;
    int empty_pos;

    PuzzleState(vector<int> b, string m, int e) : board(b), moves(m), empty_pos(e) {}

    bool operator==(const PuzzleState &other) const
    {
        return board == other.board;
    }
};

// Custom hash function for unordered_set
namespace std
{
    template <>
    struct hash<PuzzleState>
    {
        size_t operator()(const PuzzleState &state) const
        {
            size_t hash_value = 0;
            for (int num : state.board)
            {
                hash_value = hash_value * 31 + num;
            }
            return hash_value;
        }
    };
}

// Function to print the puzzle
void printPuzzle(const vector<int> &board)
{
    for (int i = 0; i < 9; ++i)
    {
        if (i % 3 == 0)
            cout << endl;
        cout << board[i] << " ";
    }
    cout << endl;
}

// Function to generate possible moves
vector<PuzzleState> generateMoves(PuzzleState current)
{
    vector<PuzzleState> next_states;
    int empty_pos = current.empty_pos;
    vector<int> directions = {-1, 1, -3, 3}; // Left, Right, Up, Down

    for (int dir : directions)
    {
        int new_pos = empty_pos + dir;
        if (new_pos >= 0 && new_pos < 9 &&
            !(empty_pos % 3 == 0 && dir == -1) && // Prevent wrap-around on left
            !(empty_pos % 3 == 2 && dir == 1))    // Prevent wrap-around on right
        {
            vector<int> new_board = current.board;
            swap(new_board[empty_pos], new_board[new_pos]);
            string new_moves = current.moves + (dir == -1 ? "L" : dir == 1 ? "R"
                                                              : dir == -3  ? "U"
                                                                           : "D");
            next_states.push_back(PuzzleState(new_board, new_moves, new_pos));
        }
    }
    return next_states;
}

// Solve using BFS (optimal)
bool bfsSolve(vector<int> initial, vector<int> goal)
{
    unordered_set<PuzzleState> visited;
    queue<PuzzleState> q;

    PuzzleState start(initial, "", find(initial.begin(), initial.end(), 0) - initial.begin());
    PuzzleState goal_state(goal, "", find(goal.begin(), goal.end(), 0) - goal.begin());

    q.push(start);
    visited.insert(start);

    while (!q.empty())
    {
        PuzzleState current = q.front();
        q.pop();

        // Print the current state
        cout << "Current State:";
        printPuzzle(current.board);
        cout << "Moves: " << current.moves << endl
             << endl;

        if (current.board == goal)
        {
            cout << "\nSolution found! Moves: " << current.moves << endl;
            cout << "Number of moves: " << current.moves.length() << endl;
            return true;
        }

        // Generate valid next states
        for (auto &next : generateMoves(current))
        {
            if (visited.find(next) == visited.end())
            {
                visited.insert(next);
                q.push(next);
            }
        }
    }

    cout << "No solution found!" << endl;
    return false;
}

int main()
{
    vector<int> initial = {1, 2, 3, 4, 5, 6, 7, 0, 8}; // Example scrambled state
    vector<int> goal = {1, 2, 3, 4, 5, 6, 7, 8, 0};    // Goal state

    cout << "Initial State:";
    printPuzzle(initial);
    cout << "Solving the 8-puzzle using BFS..." << endl;
    bfsSolve(initial, goal);

    return 0;
}
