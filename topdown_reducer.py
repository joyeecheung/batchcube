#!/usr/bin/env python

import sys

uid = 6
country, state, city = 0, 1, 2
topic, category, product = 3, 4, 5

# get the index in b_hier from head number
b_index = {
    2: 0,
    5: 1,
    6: 2,
    7: 3
}

to_o_index = ("2", "3", "4", "5", "6", "7", "1")

b_hier = [(product, category, topic, city, state, country),
          (product, category, state, country, topic),
          (product, country, category),
          (product,)]


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    f = open('maped')
    data = sorted([line for line in read_input(f)])
    # data = read_input(sys.stdin)

    # initialize
    cur_set = []
    cur_value = []
    cur_b_index = 0  # index in b_hier

    for pair in data:
        # get 2->0 in "2|1", index in b_hier
        pair_b_index = b_index[int(pair[0].split('|')[0])]
        # get the tuple
        pair_values = pair[1].split()
        # for 2(country), get the b_hier list (product, ...)
        pair_b_hier = b_hier[pair_b_index]  #
        pair_b_size = len(pair_b_hier)  # size of the b_hier list
        # print pair, pair_b_index, pair_values, pair_b_size

        # initialize, set the first tuple as current
        if not cur_value:
            cur_value = [pair_values[i] for i in pair_b_hier]
            cur_set = [set((pair_values[uid],)) for i in range(pair_b_size)]
            cur_b_index = pair_b_index

        # another batch
        if cur_b_index != pair_b_index:
            old_pair_b_index = b_hier[cur_b_index]
            old_pair_b_size = len(old_pair_b_index)
            for watched_index in range(old_pair_b_size):
                indexes = sorted(old_pair_b_index[watched_index:])
                print "%s|%s\t%s" % (' '.join(to_o_index[i] for i in indexes),
                                     ' '.join(
                                         cur_value[i] for i in indexes),
                                     len(cur_set[watched_index]))
            cur_value = [pair_values[i] for i in pair_b_index]
            cur_set = [set((pair_values[uid],)) for i in range(pair_b_size)]
            cur_b_index = pair_b_index
            # print cur_b_index, cur_value, cur_set

        # watch for changes, output the measure for each group
        for watched_index in range(pair_b_size):
            if pair_values[pair_b_index[watched_index]] != cur_value[watched_index]:
                indexes = sorted(pair_b_index[watched_index:])
                print "%s|%s\t%s" % (' '.join(to_o_index[i] for i in indexes),
                                     ' '.join(
                                         cur_value[i] for i in indexes),
                                     len(cur_set[watched_index]))
                cur_set[watched_index].clear()
                cur_value[watched_index] = pair_values[watched_index]
            else:
                cur_set[watched_index].add(pair_values[uid])

    # for the last batch
    for watched_index in range(pair_b_size):
        indexes = sorted(b_hier[cur_b_index][watched_index:])
        print "%s|%s\t%s" % (' '.join(to_o_index[i] for i in indexes),
                             ' '.join(cur_value[i] for i in indexes),
                             len(cur_set[watched_index]))

if __name__ == "__main__":
    main()
