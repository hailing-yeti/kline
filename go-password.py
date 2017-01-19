#!/usr/bin/env python

import random

def main():
    with open('wlist_match6.txt') as fh:
        words = [line[0:-1] for line in fh if len(line) > 4]
    print ' '.join([random.choice(words) for i in xrange(5)])

if __name__ == "__main__":
    main()
