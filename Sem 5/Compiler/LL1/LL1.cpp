#include <iostream>
#include <stack>
#include <map>
#include <vector>
#include <string>
using namespace std;

// Grammar symbols
enum Symbol
{
    E,
    E_PRIME,
    T,
    T_PRIME,
    F,
    PLUS,
    STAR,
    ID,
    LPAREN,
    RPAREN,
    EPSILON,
    DOLLAR
};

// Parsing table type
typedef map<Symbol, map<Symbol, vector<Symbol>>> ParsingTable;

// Production rules in the grammar
vector<Symbol> rule1 = {T, E_PRIME};        // E -> T E'
vector<Symbol> rule2 = {PLUS, T, E_PRIME};  // E' -> + T E'
vector<Symbol> rule3 = {EPSILON};           // E' -> ε
vector<Symbol> rule4 = {F, T_PRIME};        // T -> F T'
vector<Symbol> rule5 = {STAR, F, T_PRIME};  // T' -> * F T'
vector<Symbol> rule6 = {EPSILON};           // T' -> ε
vector<Symbol> rule7 = {LPAREN, E, RPAREN}; // F -> ( E )
vector<Symbol> rule8 = {ID};                // F -> id

// Function to initialize the parsing table
void initializeParsingTable(ParsingTable &parsingTable)
{
    // E → TE'
    parsingTable[E][ID] = rule1;
    parsingTable[E][LPAREN] = rule1;

    // E' → +TE' | ε
    parsingTable[E_PRIME][PLUS] = rule2;
    parsingTable[E_PRIME][RPAREN] = rule3;
    parsingTable[E_PRIME][DOLLAR] = rule3;

    // T → FT'
    parsingTable[T][ID] = rule4;
    parsingTable[T][LPAREN] = rule4;

    // T' → *FT' | ε
    parsingTable[T_PRIME][PLUS] = rule6;
    parsingTable[T_PRIME][STAR] = rule5;
    parsingTable[T_PRIME][RPAREN] = rule6;
    parsingTable[T_PRIME][DOLLAR] = rule6;

    // F → (E) | id
    parsingTable[F][ID] = rule8;
    parsingTable[F][LPAREN] = rule7;
}

// Function to display the stack
void displayStack(stack<Symbol> &st)
{
    stack<Symbol> temp = st;
    vector<string> symbols;
    while (!temp.empty())
    {
        switch (temp.top())
        {
        case E:
            symbols.push_back("E");
            break;
        case E_PRIME:
            symbols.push_back("E'");
            break;
        case T:
            symbols.push_back("T");
            break;
        case T_PRIME:
            symbols.push_back("T'");
            break;
        case F:
            symbols.push_back("F");
            break;
        case PLUS:
            symbols.push_back("+");
            break;
        case STAR:
            symbols.push_back("*");
            break;
        case ID:
            symbols.push_back("id");
            break;
        case LPAREN:
            symbols.push_back("(");
            break;
        case RPAREN:
            symbols.push_back(")");
            break;
        case DOLLAR:
            symbols.push_back("$");
            break;
        default:
            symbols.push_back("?");
            break;
        }
        temp.pop();
    }
    for (auto it = symbols.rbegin(); it != symbols.rend(); ++it)
    {
        cout << *it << " ";
    }
    cout << endl;
}
