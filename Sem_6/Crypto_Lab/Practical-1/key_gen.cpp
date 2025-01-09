#include <iostream>
#include <vector>

using namespace std;

// p10 fixed 10 bit keys
vector<int> P10 = {2, 4, 1, 6, 3, 9, 0, 8, 7, 5};

// p8 fixed for all keys
vector<int> P8 = {5, 2, 6, 3, 7, 4, 9, 8};

// Permutation function
vector<int> permute(const vector<int> &bits, const vector<int> &table)
{
    vector<int> permuted(bits.size());
    for (size_t i = 0; i < table.size(); i++)
    {
        permuted[i] = bits[table[i]];
    }
    return permuted;
}

// Left shift function
vector<int> left_shift(const vector<int> &bits, int n)
{
    vector<int> shifted(bits.size());
    for (int i = 0; i < bits.size(); i++)
    {
        shifted[i] = bits[(i + n) % bits.size()];
    }
    return shifted;
}

// Key Generation
pair<vector<int>, vector<int>> key_generation(const vector<int> &key_10bit)
{
    // Step 1 P10 permutation
    vector<int> permuted_key = permute(key_10bit, P10);

    // Step 2 Split into two halves
    vector<int> left(permuted_key.begin(), permuted_key.begin() + 5);
    vector<int> right(permuted_key.begin() + 5, permuted_key.end());

    // First left shift for K1
    vector<int> left1 = left_shift(left, 1);
    vector<int> right1 = left_shift(right, 1);

    vector<int> combined1;
    combined1.insert(combined1.end(), left1.begin(), left1.end());
    combined1.insert(combined1.end(), right1.begin(), right1.end());

    vector<int> K1 = permute(combined1, P8);

    // Second left shift for 2 positions
    vector<int> left2 = left_shift(left1, 2);
    vector<int> right2 = left_shift(right1, 2);
    vector<int> combined2;

    combined2.insert(combined2.end(), left2.begin(), left2.end());
    combined2.insert(combined2.end(), right2.begin(), right2.end());

    vector<int> K2 = permute(combined2, P8);

    return make_pair(K1, K2);
}

int main()
{
    // Example 10-bit key
    vector<int> key_10bit = {0, 1, 1, 0, 0, 1, 0, 1, 1, 0};

    // Generate subkeys K1 and K2
    auto [K1, K2] = key_generation(key_10bit);

    // Output the subkeys K1 and K2
    cout << "K1: ";
    for (int bit : K1)
    {
        cout << bit;
    }
    cout << endl;

    cout << "K2: ";
    for (int bit : K2)
    {
        cout << bit;
    }
    cout << endl;

    return 0;
}
