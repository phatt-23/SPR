#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef unordered_map<int, int> mii;
typedef unordered_map<char, char> mcc;
typedef long long ll;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define opt optional

string decrypt_word(mcc& mapping, string& word)
{
    string decrypted;
    for (char c : word)
        decrypted.PB(mapping[c]);
    return decrypted;
}

bool decrypts(mcc& mapping, vs& words, vs& vocab)
{
    for (auto& word : words)
    {
        string decrypted = decrypt_word(mapping, word);
        if (find(vocab.begin(), vocab.end(), decrypted) == vocab.end())
            return false;
    }

    return true;
}

vector<mcc> decrypt_rec(vs& words, vs& vocabulary, int k, vi& used)
{

    if (k == 0)
        return {};

    string& word = words[k - 1];


}

opt<mcc> decrypt(vs& words, vs& vocabulary)
{
    vector<int> used(vocabulary.size());
    vector<mcc> mappings = decrypt_rec(words, vocabulary, words.size(), used);

    for (auto& m : mappings)
    {
        if (decrypts(m, words, vocabulary))
            return m;
    }

    return nullopt;
}

int main()
{
    int n, ln;
    cin >> n;
    vs vocab(n);
    while (n)
        cin >> vocab[--n];

    string line;
    getline(cin, line);
    stringstream ss;

    while (getline(cin, line))
    {
        cout << "line: " << line << endl;

        ss.clear(); ss << line;

        vs words;
        while(ss >> line)
            words.PB(line);
            

        mcc mapping = decrypt(words, vocab);

        for (auto& w : words)
        {
            string decrypted;
            for (auto c : w)
                decrypted.push_back(mapping[c]);
            cout << "w: " << w << " => " << decrypted << "." << endl;
        }
    }

}
