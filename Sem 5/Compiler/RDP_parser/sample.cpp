#include <iostream>
#include <string>
#include <cctype>

class Parser
{
public:
    Parser(const std::string &input) : input(input), pos(0), currentToken(0)
    {
        nextToken();
    }

    bool parse()
    {
        try
        {
            expr();
            return currentToken == '\0'; // Ensure the entire input was parsed
        }
        catch (const std::runtime_error &)
        {
            return false;
        }
    }

private:
    std::string input;
    size_t pos;
    char currentToken;

    void nextToken()
    {
        while (pos < input.size() && isspace(input[pos]))
        {
            ++pos;
        }
        if (pos < input.size())
        {
            currentToken = input[pos++];
        }
        else
        {
            currentToken = '\0';
        }
    }

    void expr()
    {
        term();
        while (currentToken == '+')
        {
            nextToken();
            term();
        }
    }

    void term()
    {
        factor();
        while (currentToken == '*')
        {
            nextToken();
            factor();
        }
    }

    void factor()
    {
        if (isdigit(currentToken))
        {
            nextToken();
        }
        else if (currentToken == '(')
        {
            nextToken(); // consume '('
            expr();
            if (currentToken == ')')
            {
                nextToken(); // consume ')'
            }
            else
            {
                throw std::runtime_error("Expected ')'");
            }
        }
        else
        {
            throw std::runtime_error("Unexpected token");
        }
    }
};

int main()
{
    std::string input;
    std::cout << "Enter an expression: ";
    std::getline(std::cin, input);

    Parser parser(input);
    if (parser.parse())
    {
        std::cout << "Parsing successful!" << std::endl;
    }
    else
    {
        std::cout << "Parsing failed!" << std::endl;
    }

    return 0;
}
