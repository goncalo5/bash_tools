#!/usr/bin/python
import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('values', nargs="*")
    parser.add_argument(
        '-r', '--reverse', action='store_true', help="print the values below")
    args = parser.parse_args()
    return args


def get_values(args):
    if len(args.values) > 0:
        try:
            with open(args.values[0], 'r') as f:
                values = f.read()
                values = values.split()
        except IOError:
            values = args.values
    else:
        values = sys.stdin.read().split()
    return values


def values2numbers(values):
    numbers = []
    for value in values:
        try:
            numbers.append(float(value))
        except ValueError:
            continue
    return numbers
