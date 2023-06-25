#include <stdio.h>
#include <math.h>

int is_prime(long long n) {
  for (int i = 2; i < n; i++) {
    if (n % i == 0) { return 0; }
  }
  return 1;
}

int max(long long a, long long b) {
  if (a > b) { return a; }
  return b;
}

int main() {
    long long maxv = 0;
    for (long long i = 2; i <= sqrtl(600851475143ll); i++) {
        if (is_prime(i) && (600851475143ll % i == 0)) {
            maxv = max(maxv, i);
        }
    }
    printf("%lld", maxv);
    return 0;
}

