#!/bin/bash

nstart=${1:-"430"}
nend=${1:-"410"}

echo '```Bash'
for (( i = nstart; i >= nend; i-- )); do
	echo ">>> $i"
	python3 ./long6 $i 6000
	echo
done
echo '```'
