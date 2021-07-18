#!/bin/bash

FILE=$(readlink -f $BASH_SOURCE)
NAME=$(basename $FILE)
CDIR=$(dirname $FILE)
TMPDIR=${TMPDIR:-"/tmp"}

json_file=${1?"*** JSON FILE, e.g. data/01b.json"}
f_tmp=$TMPDIR/$NAME.tmp.$$
typeset -a a_subject
a_subject[0]="Chinese"
a_subject[1]="Math"
a_subject[2]="English"

for (( i = 0; i < ${#a_subject[@]}; i++ )); do
    subject=${a_subject[$i]}
    if (( i == 0 )); then
        $CDIR/xxcjfoo $json_file $subject > $f_tmp
    else
        $CDIR/xxcjfoo $json_file $subject | tail -1 >> $f_tmp
    fi
done

cat $f_tmp
rm -f $f_tmp
exit 0
