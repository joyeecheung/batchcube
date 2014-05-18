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
    (topic, country),
    (topic, country, state),
    (topic, category, country, state),
    (topic, category, product, country, state)
), (
    (topic, category),
    (topic, category, country),
    (topic, category, product, country)
), (
    (topic, category, product),
)]

batch_number = len(C)

useful = (country, state, city, topic, category, product, uid)


def read_input(file):
    for line in file:
        yield line.split()


def main():
    data = read_input(sys.stdin)
    for e in data:
        for batch in range(batch_number):
            # batch_head | head_value <TAB> country, ..., product uid
            print "%s|%s\t%s" % (str(batch),
                                 ' '.join(e[i] for i in C[batch][0]),
                                 ' '.join(e[i] for i in useful))
if __name__ == "__main__":
    main()
