#!/usr/bin/env python3
from csv import reader
from sys import argv, stderr

# main function
if __name__ == "__main__":
    # check usage
    if len(argv) != 2:
        print("USAGE: %s <input_first_last_table_tsv>" % argv[0], file=stderr); exit(1)

    # find missing data
    for first, last, table in reader(open(argv[1]), delimiter='\t'):
        num = int(table.split(' - ')[0])
        num_s = str(num).rjust(2)
        print("%s %s — %s" % (first, last, num_s))
