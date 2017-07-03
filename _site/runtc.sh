#!/bin/sh

pwd
FILES=tc*
for f in $FILES
do
  tmp=$tmp" "${f%.*}
done
runsikulix -r $tmp
