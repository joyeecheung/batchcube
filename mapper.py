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
        for head in (B[0] for B in C):
            k = [e[i] for i in head]
            # batch head | head value <TAB> uid, country, ..., product
            # country | USA <TAB> 1, USA, ... , iPhone
            print "%s|%s\t%s" % (' '.join([str(i) for i in head]),
                                 ' '.join(k),
                                 ' '.join(e[i] for i in useful))
if __name__ == "__main__":
    main()
