#!/bin/sh

pwd
FILES=tc00*
for f in $FILES
do
  cd $f
  FILES2=tc*
  for f2 in $FILES2
  do
    f2nr=${f2:2:1}
    f2ext=${f2:4:5}
    echo $f2
    echo $f2nr
    echo $f2ext
    kommando="mv $f2 tc00$f2nr.$f2ext"
    $kommando
  done  
  cd ..
done
