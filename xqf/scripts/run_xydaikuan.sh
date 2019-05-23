#!/bin/bash

typeset a_set
a_set[0]="30 0.05 2"
a_set[1]="30 0.05 3"
a_set[2]="30 0.06 2"
a_set[3]="30 0.06 3"
a_set[4]="30 0.07 2"
a_set[5]="30 0.07 3"
a_set[6]="30 0.08 2"
a_set[7]="30 0.08 3"
a_set[8]="30 0.09 2"
a_set[9]="30 0.09 3"

echo '```Bash'
for (( i = 0; i < ${#a_set[@]}; i++ )); do
	echo ">>> $i"
	python3 ./xydaikuan ${a_set[$i]}
	echo
done
echo '```'
