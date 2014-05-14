#!/usr/bin/env python

import sys

uid = 6
country, state, city = 0, 1, 2
topic, category, product = 3, 4, 5

head_dict = {
    2: 0,
    5: 1,
    6: 2,
    7: 3
}

index_dict = ("2", "3", "4", "5", "6", "7", "1")

watching = [(product, category, topic, city, state, country),
            (product, category, state, country, topic),
            (product, country, category),
            (product,)]


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    # f = open('maped')
    # data = sorted([line for line in read_input(f)])
    data = read_input(sys.stdin)

    # initialize
    sets = []
    current_values = []
    current_batch = 0  # index in watching

    for pair in data:
        # get 2->0 in "2|1", index in watching
        which_batch = head_dict[int(pair[0].split('|')[0])]
        # get the tuple
        values = pair[1].split()
        # for 2(country), get the watching list (product, ...)
        watch_list = watching[which_batch]  #
        watched_number = len(watch_list)  # size of the watching list
        # print pair, which_batch, values, watched_number

        # initialize, set the first tuple as current
        if not current_values:
            current_values = [values[i] for i in watch_list]
            sets = [set((values[uid],)) for i in range(watched_number)]
            current_batch = which_batch

        # another batch
        if current_batch != which_batch:
            old_watch_list = watching[current_batch]
            old_watched_number = len(old_watch_list)
            for watched_index in range(old_watched_number):
                indexes = sorted(old_watch_list[watched_index:])
                print "%s|%s\t%s" % (' '.join(index_dict[i] for i in indexes),
                                     ' '.join(
                                         current_values[i] for i in indexes),
                                     len(sets[watched_index]))
            current_values = [values[i] for i in watch_list]
            sets = [set((values[uid],)) for i in range(watched_number)]
            current_batch = which_batch
            # print current_batch, current_values, sets

        # watch for changes, output the measure for each group
        for watched_index in range(watched_number):
            if values[watch_list[watched_index]] != current_values[watched_index]:
                indexes = sorted(watch_list[watched_index:])
                print "%s|%s\t%s" % (' '.join(index_dict[i] for i in indexes),
                                     ' '.join(
                                         current_values[i] for i in indexes),
                                     len(sets[watched_index]))
                sets[watched_index].clear()
                current_values[watched_index] = values[watched_index]
            else:
                sets[watched_index].add(values[uid])

    # for the last batch
    for watched_index in range(watched_number):
        indexes = sorted(watching[current_batch][watched_index:])
        print "%s|%s\t%s" % (' '.join(index_dict[i] for i in indexes),
                             ' '.join(current_values[i] for i in indexes),
                             len(sets[watched_index]))

if __name__ == "__main__":
    main()
