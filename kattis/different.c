//#https://open.kattis.com/problems/different
#include <stdio.h>
/*@
  requires lb: (x >= 0) && (y >= 0);
  requires ub: (x <= 100000000000000 && y <= 100000000000000);
  behavior case_1:
    assumes (x == 10) && (y == 12);
    ensures \result == 2;
  behavior case_2:
    assumes (x == 71293781758123) && (y == 72784);
    ensures \result == 71293781685339;
  behavior case_3:
    assumes (x == 1) && (y == 12345677654321);
    ensures \result == 12345677654320;
  behavior x_geq_y:
    assumes x >= y;
    ensures \result >= 0;
    ensures \result == x - y;
  behavior else:
    assumes x < y;
    ensures \result >= 0;
    ensures \result == y - x;
  assigns \nothing;
*/
long long int max(long long int x, long long int y) {
  if (x >= y) {
    return x - y;
  }
  return y - x;
}

int main() {
  long long int x,y;
  while (scanf("%Ld", &x) == 1) {
  scanf("%Ld", &y);
  long long int sol = max(x, y);
  printf("%Ld\n", sol);
  }
  return 0;
}
