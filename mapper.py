#!/usr/bin/env python
import sys
from itertools import product

uid = 1
country, state, city = 2, 3, 4
topic, category, product = 5, 6, 7

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
useful = (country, state, city, topic, category, product, uid)


def read_input(file):
    for line in file:
        yield line.split()


def main():
    data = read_input(sys.stdin)
    for e in data:
        for B in C:
            head = B[0]
            # batch_head | head_value <TAB> country, ..., product uid
            print "%s|%s\t%s" % (' '.join([str(i) for i in head]),
                                 ' '.join([e[i] for i in head]),
                                 ' '.join(e[i] for i in useful))
if __name__ == "__main__":
    main()
