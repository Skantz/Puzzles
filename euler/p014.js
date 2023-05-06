function f(n) {
  if (n % 2 != 0) {
    return 3 * n + 1;
  }
  return n / 2;
}

function c(n) {
  c_ = 0;
  while (n != 1) {
    c_ += 1;
    n = f(n);
  }
  return c_;
}

maxx = 1;
maxno = -1;
for (var i = 2; i < 1000000; i++)  {
  t = c(i);
  if (t > maxx) {
    maxno = i;
    maxx = t;
  }
}

console.log(maxno);

