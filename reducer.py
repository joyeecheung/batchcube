#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

uid = 6
country, state, city = 0, 1, 2
topic, category, product = 3, 4, 5

C = [(
    (country,),
    (country, state),
    (country, state, city),
    (country, state, city, topic),
    (country, state, city, topic, category),
    (country, state, city, topic, category, product)
), (
    (topic,),
    (country, topic),
    (country, state, topic),
    (country, state, topic, category),
    (country, state, topic, category, product)
), (
    (category,),
    (country, category),
    (country, category, product)
), (
    (product,),
)]


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = read_input(sys.stdin)
    # group by batch head
    for head, batch in groupby(data, itemgetter(0)):
        e = [e.split() for head, e in batch]  # get useful fields
        for R in [B for B in C]:
            for region, group in groupby(e, itemgetter(*R)):
                disdinct = len(set(record[-1] for record in group))
                print "%s|%s\t%s" % (' '.join(R), ' '.join(region), disdinct)

if __name__ == "__main__":
    main()
