#!/bin/bash
total=${1:-"218"}
yuelilv=${2:-"0.049"}
i_start=${3:-"15"}
i_end=${4:-"20"}

echo '```bash'
echo
for (( i = i_start; i <= i_end; i++ )); do
	echo "=========================$total::$i============================="
	for j in 0.15 0.20; do
		echo "********* $total::$i::$j *********"
		python3 ./daikuan $total $yuelilv $j $i
		echo
	done
	echo
done
echo '```'
