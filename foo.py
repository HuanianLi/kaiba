#!/usr/bin/python

import sys

def main(argc, argv):
    if argc != 2:
        sys.stderr.write("Usage: %s <num>\n" % argv[0])
        return -1

    i = 0
    while i < int(argv[1]):
        print "%02d: Hello World." % i
        i += 1

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    sys.exit(main(argc, argv))
