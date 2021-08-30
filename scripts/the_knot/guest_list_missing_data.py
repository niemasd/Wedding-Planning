#!/usr/bin/env python3
from csv import reader
from sys import argv

# main function
if __name__ == "__main__":
    # check usage
    if len(argv) != 3:
        print("USAGE: %s <input_guestlist> <output_tsv>" % argv[0]); exit(1)

    # find missing data
    missing = dict()
    for row in reader(open(argv[1])):
        party = row[2].strip()
        if party == 'Party':
            continue # header
        if party not in missing:
            missing[party] = [label for i,label in [(3,'Phone'), (4,'Email'), (5,'Home Address')] if len(row[i].strip()) == 0]

    # output parties with missing data
    out = open(argv[2],'w'); out.write("Party\tMissing Data\n")
    for party in sorted(missing.keys()):
        if len(missing[party]) != 0:
            out.write('%s\t%s\n' % (party, ', '.join(missing[party])))
    out.close()
