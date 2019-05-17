#!/bin/bash

typeset a_set
a_set[0]="20:0.67:3:GF 18:0.375:2:ZH"
a_set[1]="12:0.67:3:GF 18:0.375:2:ZH"
a_set[2]="13:0.67:3:GF 17:0.375:2:ZH"
a_set[3]="14:0.67:3:GF 16:0.375:2:ZH"
a_set[4]="15:0.67:3:GF 15:0.375:2:ZH"
a_set[5]="16:0.67:3:GF 14:0.375:2:ZH"
a_set[6]="17:0.67:3:GF 13:0.375:2:ZH"
a_set[7]="18:0.67:3:GF 12:0.375:2:ZH"
a_set[8]="19:0.67:3:GF 11:0.375:2:ZH"
a_set[9]="20:0.67:3:GF 10:0.375:2:ZH"

echo '```Bash'
for (( i = 0; i < ${#a_set[@]}; i++ )); do
	echo ">>> $i"
	python3 ./bank ${a_set[$i]}
	echo
done
echo '```'
