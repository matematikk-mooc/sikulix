#!/bin/sh

pwd
FILES=selfregister*
for f in $FILES
do
  tmp=$tmp" "${f%.*}
done
runsikulix -r $tmp
