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

head_dict = {
    2: 0,
    5: 1,
    6: 2,
    7: 3
}


index_dict = ("2", "3", "4", "5", "6", "7", "1")


def read_input(file):
    for line in file:
        key, value = line.rstrip().split('\t')
        head = key.split('+')[0]
        yield (head, value)


def main():
# f = open('maped')
# data = [line for line in read_input(f)]
    data = read_input(sys.stdin)
    # group by batch head
    # e.g. head = "1|2" (country batch, country=2)
    # group = [("1|2", "..... uid"), ("1|2", ".... uid") ....]
    for head, group in groupby(data, itemgetter(0)):
        which_batch = int(head.split('|')[0])
        # regions = the batch scheme
        regions = C[head_dict[which_batch]]
        # area = [(country, state, ...., uid)...]
        bottom = regions[-1]
        raw_area = sorted([e for head, e in group], key=itemgetter(*bottom))
        area = [e.split() for e in raw_area]  # get useful fields
        for R in regions:
            for region, group in groupby(area, itemgetter(*R)):
                reach = len(set(record[-1] for record in group))
                if type(region) is str:
                    region_value = region
                else:
                    region_value = ' '.join(region)
                print "%s|%s\t%s" % (' '.join([index_dict[i] for i in R]), region_value, reach)

if __name__ == "__main__":
    main()
