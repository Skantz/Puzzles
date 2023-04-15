const x = Z3.Int.const('x');
const y = Z3.Int.const('y');
const z = Z3.Int.const('z');
const w = Z3.Int.const('w')
Z3.solve(x.gt(0), y.gt(0),
  z.gt(0), x.neq(y), x.neq(z), y.neq(z),
  ((x.mul(x)).add(y.mul(y)).eq(z.mul(z))),
  x.add(y).add(z).eq(1000),
  x.mul(y).mul(z).eq(w))
