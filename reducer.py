#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
from collections import deque
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
    (topic, country),
    (topic, country, state),
    (topic, category, country, state),
    (topic, category, product, country, state)
), (
    (category,),
    (country, category),
    (country, category, product)
), (
    (product,),
)]

head_dict = {
    2: 0,
    5: 1,
    6: 2,
    7: 3
}


index_dict = ("2", "3", "4", "5", "6", "7", "1")


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = read_input(sys.stdin)
    # group by batch head
    for head, batch in groupby(data, itemgetter(0)):
        area = deque(e.split() for head, e in batch)  # get useful fields
        head_value = int(head.split('|')[0])
        regions = C[head_dict[head_value]]
        for R in regions:
            for region, group in groupby(area, itemgetter(*R)):
                disdinct = len(set(record[-1] for record in group))
                print "%s|%s\t%s" % (' '.join([index_dict[i] for i in R]),
                                     ' '.join(region),
                                     disdinct)

if __name__ == "__main__":
    main()
