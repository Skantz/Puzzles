#include <iostream>
#include <string>
using namespace std;

int main() {

  int case_n;
  case_n = 1;
  while (1) {
    if(cin.eof()){
      return 0;
    }

    int a;
    int b;
    int c;
    int d;

    if (!(cin >> a)) {
      return 0;}
    cin >> b;
    cin >> c;
    cin >> d;

    int determinant;
    determinant = 1/(a*d-b*c);

    cout << "Case " << case_n << ":" << "\n" << determinant * d << " " << determinant * (-b) << "\n";
    cout << determinant * (-c) << " " << determinant * (a) << "\n";

    case_n++;

    string blank_line;
    getline(cin, blank_line);
    getline(cin, blank_line);

  }

  return 0;

}

