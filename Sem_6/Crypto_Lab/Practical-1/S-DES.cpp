#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    // Permutation functions
    vector<int> permute(const vector<int> &input, const vector<int> &permTable)
    {
        vector<int> output(permTable.size());
        for (size_t i = 0; i < permTable.size(); ++i)
        {
            output[i] = input[permTable[i] - 1];
        }
        return output;
    }

    // Left shift function
    vector<int> leftShift(const vector<int> &input, int shifts)
    {
        vector<int> output = input;
        int size = input.size();
        for (int i = 0; i < shifts; ++i)
        {
            int temp = output[0];
            for (int j = 0; j < size - 1; ++j)
            {
                output[j] = output[j + 1];
            }
            output[size - 1] = temp;
        }
        return output;
    }

    // XOR function
    vector<int> XOR(const vector<int> &a, const vector<int> &b)
    {
        vector<int> result(a.size());
        for (size_t i = 0; i < a.size(); ++i)
        {
            result[i] = a[i] ^ b[i];
        }
        return result;
    }

    // S-Boxes
    vector<int> SBox(const vector<int> &input, const vector<vector<int>> &S)
    {
        int row = input[0] * 2 + input[3];
        int col = input[1] * 2 + input[2];
        int value = S[row][col];
        return {(value >> 1) & 1, value & 1};
    }

    // Function F
    vector<int> F(const vector<int> &right, const vector<int> &subKey)
    {
        // Expansion permutation
        vector<int> expansionTable = {4, 1, 2, 3, 2, 3, 4, 1};
        vector<int> expanded = permute(right, expansionTable);

        // XOR with subKey
        vector<int> xorResult = XOR(expanded, subKey);

        // Split into two 4-bit halves
        vector<int> left4(xorResult.begin(), xorResult.begin() + 4);
        vector<int> right4(xorResult.begin() + 4, xorResult.end());

        // S-Box lookup
        vector<vector<int>> S0 = {
            {1, 0, 3, 2},
            {3, 2, 1, 0},
            {0, 2, 1, 3},
            {3, 1, 3, 2}};
        vector<vector<int>> S1 = {
            {0, 1, 2, 3},
            {2, 0, 1, 3},
            {3, 0, 1, 0},
            {2, 1, 0, 3}};

        vector<int> leftS = SBox(left4, S0);
        vector<int> rightS = SBox(right4, S1);

        // Combine S-Box outputs
        vector<int> combined = {leftS[0], leftS[1], rightS[0], rightS[1]};

        // P4 permutation
        vector<int> P4Table = {2, 4, 3, 1};
        return permute(combined, P4Table);
    }

    // Encryption function
    vector<int> encrypt(const vector<int> &plaintext, const vector<int> &key1, const vector<int> &key2)
    {
        vector<int> IP = {2, 6, 3, 1, 4, 8, 5, 7};        // Initial permutation
        vector<int> inverseIP = {4, 1, 3, 5, 7, 2, 8, 6}; // Inverse initial permutation

        vector<int> permuted = permute(plaintext, IP);
        vector<int> left(permuted.begin(), permuted.begin() + 4);
        vector<int> right(permuted.begin() + 4, permuted.end());

        // Round 1
        vector<int> fResult = F(right, key1);
        vector<int> leftXorF = XOR(left, fResult);
        swap(left, right); // Switch halves (correct the swap)

        // Round 2
        fResult = F(right, key2);
        left = XOR(leftXorF, fResult);

        // Combine halves and apply inverse permutation
        vector<int> combined = left;
        combined.insert(combined.end(), right.begin(), right.end());
        return permute(combined, inverseIP);
    }

    // Decryption function
    vector<int> decrypt(const vector<int> &ciphertext, const vector<int> &key1, const vector<int> &key2)
    {
        return encrypt(ciphertext, key2, key1); // Reverse the keys for decryption
    }

    // Helper function to print vector
    void printVector(const vector<int> &vec)
    {
        for (int bit : vec)
        {
            cout << bit;
        }
        cout << endl;
    }
};

int main()
{
    Solution temp;
    // Example usage
    vector<int> plaintext = {1, 0, 1, 0, 0, 1, 0, 1}; // 8-bit plaintext
    vector<int> key1 = {1, 0, 1, 0, 0, 1, 0, 0};      // First 8-bit key
    vector<int> key2 = {0, 1, 0, 0, 0, 0, 1, 1};      // Second 8-bit key

    cout << "Plaintext: ";
    temp.printVector(plaintext);

    vector<int> ciphertext = temp.encrypt(plaintext, key1, key2); // Use temp object
    cout << "Ciphertext: ";
    temp.printVector(ciphertext);

    vector<int> decryptedText = temp.decrypt(ciphertext, key1, key2); // Use temp object
    cout << "Decrypted text: ";
    temp.printVector(decryptedText);

    return 0;
}
