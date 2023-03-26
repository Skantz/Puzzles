%minizinc model.mzn -a --solver-statistics

var int : a;
var int : b;
var int : c;
var int : d;
var int : e;
var int : f;
var int : g;
var int : h;

constraint a >= 0 /\ b >= 0 /\ c >= 0  /\ d >= 0 
        /\ e >= 0 /\ f >= 0 /\ g >= 0 /\ h >= 0;

constraint 1*a + 2*b + 5*c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h = 200;

constraint a <= 200;
constraint b <= 100;
constraint c <= 40;
constraint d <= 20;
constraint e <= 10;
constraint f <= 4;
constraint g <= 2;
constraint h <= 1;

solve satisfy;
