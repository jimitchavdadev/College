#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

// Representing the 8-puzzle state
struct PuzzleState
{
    vector<int> board; // 3x3 grid flattened as a vector of size 9
    string moves;      // Record the moves that led to this state
    int empty_pos;     // Position of the empty space (0)

    // Constructor for PuzzleState
    PuzzleState(vector<int> board, string moves, int empty_pos)
    {
        this->board = board;
        this->moves = moves;
        this->empty_pos = empty_pos;
    }

    // Helper function to check if two PuzzleState objects are equal
    bool operator==(const PuzzleState &other) const
    {
        return board == other.board;
    }
};

// Hash function to use PuzzleState in unordered_set
namespace std
{
    template <>
    struct hash<PuzzleState>
    {
        size_t operator()(const PuzzleState &state) const
        {
            return hash<string>()(to_string(state.board[0]) + to_string(state.board[1]) +
                                  to_string(state.board[2]) + to_string(state.board[3]) +
                                  to_string(state.board[4]) + to_string(state.board[5]) +
                                  to_string(state.board[6]) + to_string(state.board[7]) +
                                  to_string(state.board[8]));
        }
    };
}

// Function to print the puzzle
void printPuzzle(const vector<int> &board)
{
    for (int i = 0; i < 9; ++i)
    {
        if (i % 3 == 0 && i != 0)
            cout << endl;
        cout << board[i] << " ";
    }
    cout << endl;
}

// Function to generate possible moves from the current state
vector<PuzzleState> generateMoves(PuzzleState current)
{
    vector<PuzzleState> next_states;
    int empty_pos = current.empty_pos;
    vector<int> directions = {-1, 1, -3, 3}; // left, right, up, down moves
    vector<int> new_board;

    for (int dir : directions)
    {
        int new_pos = empty_pos + dir;

        // Ensure valid position after the move
        if (new_pos >= 0 && new_pos < 9 &&
            !(empty_pos % 3 == 0 && dir == -1) && // prevent left move on the first column
            !(empty_pos % 3 == 2 && dir == 1))
        { // prevent right move on the last column
            new_board = current.board;
            swap(new_board[empty_pos], new_board[new_pos]);

            // Append the new state
            next_states.push_back(PuzzleState(new_board, current.moves + (dir == -1 ? "L" : dir == 1 ? "R"
                                                                                        : dir == -3  ? "U"
                                                                                                     : "D"),
                                              new_pos));
        }
    }
    return next_states;
}

// Function to solve the 8-puzzle using BFS
bool bfsSolve(vector<int> initial, vector<int> goal)
{
    // Set to keep track of visited states
    unordered_set<PuzzleState> visited;

    // Start state
    PuzzleState start(initial, "", find(initial.begin(), initial.end(), 0) - initial.begin());

    // Goal state
    PuzzleState goal_state(goal, "", find(goal.begin(), goal.end(), 0) - goal.begin());

    // BFS Queue
    queue<PuzzleState> q;
    q.push(start);
    visited.insert(start);

    while (!q.empty())
    {
        PuzzleState current = q.front();
        q.pop();

        // Print the current puzzle state
        cout << "Current State:" << endl;
        printPuzzle(current.board);
        cout << "Moves so far: " << current.moves << endl
             << endl;

        // If the goal state is found
        if (current.board == goal)
        {
            cout << "\nSolution found! Moves: " << current.moves << endl;
            cout << "Number of moves: " << current.moves.length() << endl;
            return true;
        }

        // Generate all possible moves from current state
        vector<PuzzleState> next_states = generateMoves(current);

        for (auto &next : next_states)
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
    // Scrambled initial state (not the goal state)
    vector<int> initial = {1, 2, 3, 4, 5, 6, 7, 0, 8}; // Starting configuration (not the goal state)

    // Goal state
    vector<int> goal = {1, 2, 3, 4, 5, 6, 7, 8, 0}; // Goal configuration

    cout << "Initial State: " << endl;
    printPuzzle(initial);

    cout << "Solving the 8-puzzle using BFS..." << endl;
    bfsSolve(initial, goal);

    return 0;
}
