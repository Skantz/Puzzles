#include <stdint.h>

uint32_t reverseBits(uint32_t n) {
  uint32_t m;
  for (uint32_t _ = 0; _ < 32; _++) {
    m = m << 1;
    if (n & 1) {
      m = m | 1;
    }
    n >>= 1;
  }
  return m;
}
