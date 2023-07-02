include "globals.mzn";

int: items_n;
int: boxes_n;

array[int] of int: items_array = array1d(1..items_n);
array[1..boxes_n] of var 0..boxes_n: boxes_array;

constraint forall(i in items_array)(member(boxes_array,i));
constraint forall(i in boxes_array)(member(items_array,i) \/ i == 0);
constraint alldifferent_except_0(boxes_array);

solve satisfy;
