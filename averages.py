#!/usr/bin/env python
import sys
import statistics
USAGE_MESSAGE = "Usage: ./averages.py --average list. Where -- is either --mean, --median or --mode"


def print_usage():
    print(USAGE_MESSAGE)
    quit()


def main(args):
    if len(args) >= 9:
        print_usage()
    average = sys.argv[1]
    num_list = sys.argv[2:]
    num_list = [int(x) for x in num_list]
    print(num_list)
    if average == '--mode':
        print("mode: ", statistics.mode(num_list))
    elif average == '--median':
        print("median: ", statistics.median(num_list))
    elif average == '--mean':
        print("mean: ", statistics.mean(num_list))
    else:
        print("donkey")


if __name__ == '__main__':
    main(sys.argv[2:])
