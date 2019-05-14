#!/bin/bash

base_max=${1:-"630"}
base_min=${2:-"550"}

echo '```Bash'
n=$(( (base_max - base_min) / 5 ))
for (( i = 0; i <= n; i++ )); do
	total=$(( base_max - 5 * i ))
	echo "=========================$total================================="
	for j in 0.90 0.91 0.92 0.93 0.94 0.95; do
		echo "********* $total::$j *********"
		python3 ./fang $total $j 20
		echo
	done
	echo
done
echo '```'
