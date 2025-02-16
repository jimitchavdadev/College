#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

// Puzzle state representation
struct PuzzleState
{
    vector<int> board;
    string moves;
    int empty_pos;
    int cost;
    int heuristic;

    PuzzleState(vector<int> b, string m, int e, int c, int h)
        : board(b), moves(m), empty_pos(e), cost(c), heuristic(h) {}

    bool operator>(const PuzzleState &other) const
    {
        return (cost + heuristic) > (other.cost + other.heuristic);
    }
};

// Print the board state
void printBoard(const vector<int> &board)
{
    for (int i = 0; i < 9; i++)
    {
        if (i % 3 == 0)
            cout << "\n";
        cout << (board[i] == 0 ? "_ " : to_string(board[i]) + " ");
    }
    cout << "\n";
}

// Manhattan Distance heuristic
int manhattanDistance(const vector<int> &board, const vector<int> &goal)
{
    int distance = 0;
    for (int i = 0; i < 9; i++)
    {
        if (board[i] == 0)
            continue;
        int target = find(goal.begin(), goal.end(), board[i]) - goal.begin();
        distance += abs(i / 3 - target / 3) + abs(i % 3 - target % 3);
    }
    return distance;
}

// Custom hash function
namespace std
{
    template <>
    struct hash<vector<int>>
    {
        size_t operator()(const vector<int> &board) const
        {
            size_t hash_value = 0;
            for (int num : board)
            {
                hash_value = hash_value * 31 + num;
            }
            return hash_value;
        }
    };
}

// Function to generate possible moves
vector<PuzzleState> generateMoves(PuzzleState current, const vector<int> &goal)
{
    vector<PuzzleState> next_states;
    int empty_pos = current.empty_pos;
    vector<int> directions = {-1, 1, -3, 3}; // Left, Right, Up, Down
    char move_chars[] = {'L', 'R', 'U', 'D'};

    for (int i = 0; i < 4; i++)
    {
        int new_pos = empty_pos + directions[i];
        if (new_pos >= 0 && new_pos < 9 &&
            !(empty_pos % 3 == 0 && directions[i] == -1) &&
            !(empty_pos % 3 == 2 && directions[i] == 1))
        {
            vector<int> new_board = current.board;
            swap(new_board[empty_pos], new_board[new_pos]);
            int h = manhattanDistance(new_board, goal);
            next_states.push_back(PuzzleState(new_board, current.moves + move_chars[i], new_pos, current.cost + 1, h));
        }
    }
    return next_states;
}

// Solve using A* search
bool aStarSolve(vector<int> initial, vector<int> goal)
{
    priority_queue<PuzzleState, vector<PuzzleState>, greater<PuzzleState>> pq;
    unordered_set<vector<int>> visited;

    PuzzleState start(initial, "", find(initial.begin(), initial.end(), 0) - initial.begin(), 0, manhattanDistance(initial, goal));
    pq.push(start);

    while (!pq.empty())
    {
        PuzzleState current = pq.top();
        pq.pop();

        cout << "\nCurrent State (g: " << current.cost << ", h: " << current.heuristic << ", f: " << current.cost + current.heuristic << ")";
        printBoard(current.board);

        if (current.board == goal)
        {
            cout << "\nSolution found! Moves: " << current.moves << endl;
            cout << "Number of moves: " << current.moves.length() << endl;
            return true;
        }

        if (visited.count(current.board))
            continue;
        visited.insert(current.board);

        for (auto &next : generateMoves(current, goal))
        {
            if (!visited.count(next.board))
                pq.push(next);
        }
    }

    cout << "No solution found!" << endl;
    return false;
}

int main()
{
    vector<int> initial = {8, 7, 6, 5, 4, 3, 2, 1, 0}; // Example scrambled state
    vector<int> goal = {1, 2, 3, 4, 5, 6, 7, 8, 0};    // Goal state

    cout << "Solving the 8-puzzle using A* search..." << endl;
    aStarSolve(initial, goal);

    return 0;
}
