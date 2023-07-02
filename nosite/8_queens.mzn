include "globals.mzn";

array[1..8, 1..8] of var 0..1: x;

%8 Queens
constraint sum([1 | i, j in 1..8 where x[i,j] == 1]) == 8;

%Row conflict handling
constraint forall(i in 1..8) (sum([1 | j in 1..8 where x[i,j] == 1]) <= 1);

%Column conflict handling

constraint forall(j in 1..8) (sum([1 | i in 1..8 where x[i,j] == 1]) <= 1);

%Diagonal conflict handling 45 degrees 

constraint forall(k in 3..15) (sum([1 | i, j in 1..8 where i + j == k /\ x[i,j] == 1]) <= 1);

%Diagonal conflict handling -45 degrees

constraint forall(k in -6..6) (sum([1 | i, j in 1..8 where i - j == k /\ x[i,j] == 1]) <= 1);

solve satisfy; 

%output from http://hakank.org/minizinc/queens_ip.mzn

output 
[
  if j = 1 then "\n" else " " endif ++
    show(x[i,j])
  | i,j in 1..8
];
