#include<bits/stdc++.h>
using namespace std;

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
