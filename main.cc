#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> GetFreq(const string &s)
{
  vector<int> freq(26, 0);
  for (char c : s) {
    ++freq[c - 'a'];
  }
  return freq;
}

int main()
{
  int chars, friends;
  cin >> chars >> friends;
  cin.get();

  string line;
  getline(cin, line);

  auto freq = GetFreq(line);
  auto less_than_friends = [friends] (int num) -> bool { return num <= friends; };

  auto good = all_of(freq.begin(), freq.end(), less_than_friends);
  cout << (good ? "YES" : "NO") << "\n";
  return 0;
}
