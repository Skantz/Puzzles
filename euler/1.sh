#!/bin/bash
SUM=0
for i in $(seq 1 999)
do
  A=$(($i % 3))
  B=$(($i % 5))
  if [ "$A" = 0 ]; 
  then SUM=$(expr $SUM + $i)
  elif [ "$B" = 0 ];
  then SUM=$(expr $SUM + $i)
  fi
done
echo $SUM
