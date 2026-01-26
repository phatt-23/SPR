#include<bits/stdc++.h>
using namespace std;

/**
 *
Puvodne v Pythonu s vysledkem Time limit exceeded.

import sys

def cutting(start, end, cuts, cut_start, cut_end, memo):
    if cut_start == cut_end:
        return 0
    elif memo[cut_start][cut_end] != -1:
        return memo[cut_start][cut_end]
    else:
        stick_len = end - start
        min_cutting = -1
        for i in range(cut_start, cut_end):
            cut = cuts[i]
            left_stick = cutting(start, cut, cuts, cut_start, i, memo)
            right_stick = cutting(cut, end, cuts, i + 1, cut_end, memo)
            if min_cutting == -1:
                min_cutting = stick_len + left_stick + right_stick
            else:
                min_cutting = min(min_cutting, stick_len + left_stick + right_stick)
        memo[cut_start][cut_end] = min_cutting
        return min_cutting

memo = [[-1] * 50 for _ in range(50)]

def sticks(amount, cuts):
    n = len(cuts)
    for i in range(n):
        for j in range(n):
            memo[i][j] = -1

    result = cutting(0, amount, cuts, 0, n, memo) 
    return result

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    while data[idx] != 0:
        amount = data[idx]
        cut_count = data[idx + 1]
        idx += 2
        cuts = [0] * cut_count
        for i in range(cut_count):
            cuts[i] = data[idx + i]
        idx += cut_count
        result = sticks(amount, cuts)
        print(f"The minimum cutting is {result}.")
 *
 * */

int cuts[49] = {0};
int memo[50][50] = {0};

int cutting(int start, int end, int cut_start, int cut_end, int idx = 0)
{
    // cout << "start: " << start << ", end: " << end << ", cut_start: " << cut_start << ", cut_end: " << cut_end << "\n";
    if (cut_start == cut_end)
    {
        return 0;
    }
    else if (memo[cut_start][cut_end] != -1)
    {
        return memo[cut_start][cut_end];
    }
    else
    {
        int min_cutting = -1;
        int stick_len = end - start;
        for (int i = cut_start; i < cut_end; i++)
        {
            int cut = cuts[i];
            int left = cutting(start, cut, cut_start, i,       idx + 1);
            int right = cutting(cut, end,  i + 1,     cut_end, idx + 1);
            if (min_cutting == -1)
                min_cutting = left + right + stick_len;
            else
                min_cutting = min(min_cutting, left + right + stick_len);
        }
        memo[cut_start][cut_end] = min_cutting;
        return min_cutting;
    }
}

int sticks(int amount, int cut_count)
{
    for (int i = 0; i < cut_count + 1; i++)
    {
        for (int j = 0; j < cut_count + 1; j++)
        {
            memo[i][j] = -1;
        }
    }

    return cutting(0, amount, 0, cut_count);
}

int main()
{
    int amount, cut_count;
    while(cin >> amount && amount != 0)
    {
        cin >> cut_count;
        // cout << "amount: " << amount << ", cut_count: " << cut_count << endl;
        for (size_t i = 0; i < cut_count; i++)
        {
            cin >> cuts[i];
            // cout << cuts[i] << " ";
        }
        // cout << endl;

        

        int result = sticks(amount, cut_count);
        cout << "The minimum cutting is " << result << "." << endl;
    }

    return 0;
}
