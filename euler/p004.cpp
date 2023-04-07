#include <iostream>

bool is_palindrome(std::string s) {
  int n = s.length();
  for (int i = 0; i < s.length() / 2; i++) {
    if (s[i] != s[n - i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  int maxv = 0;
  for (int i = 0; i < 1000; i++) {
    for (int j = 0; j < 1000; j++) {
      int sum = i * j;
      if (is_palindrome(std::to_string(sum))) {
        if (sum > maxv) {
          maxv = sum;
        }
      }
    }
  }
  std::cout << maxv;
  return 0;
}

