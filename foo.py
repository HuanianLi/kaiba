#!/usr/bin/python

import sys

def main(argc, argv):
    i = 0
    while i < int(argv[1]):
        print "%02d: Hello World." % i
        i += 1

    return 0

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    sys.exit(main(argc, argv))
