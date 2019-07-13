#!/bin/bash
#
# Create a QR image for plain text, e.g. URL of README.md, which is very
# helpful to send text from PC to cell phone
#
# NOTE: (On fedora) sudo dnf -y install qrencode
#

FILE=$(readlink -f ${BASH_SOURCE})
NAME=$(basename $FILE)
CDIR=$(dirname $FILE)
TMPDIR=${TMPDIR:-"/tmp"}

f_img=$TMPDIR/$NAME.out.$$.png
trap "rm -f $f_img" EXIT

qrencode -o $f_img -s 9 "$@"
eog $f_img
