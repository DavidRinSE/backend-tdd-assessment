#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "DavidRinSE"


import sys
import argparse


def get_text(text, upper=False, lower=False, title=False):
    if title:
        return text.title()
    if lower:
        return text.lower()
    if upper:
        return text.upper()

    return text


def create_parser():
    """Create a cmd line parser object"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('-u',
                        '--upper', help='convert text to uppercase',
                        action='store_true', default=False)
    parser.add_argument('-l',
                        '--lower',
                        help='convert text to lowercase',
                        action='store_true', default=False)
    parser.add_argument('-t',
                        '--title',
                        help='convert text to titlecase',
                        action='store_true', default=False)
    parser.add_argument('text',
                        help='text to be manipulated')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    print(get_text(ns.text, upper=ns.upper, lower=ns.lower, title=ns.title))


if __name__ == '__main__':
    main(sys.argv[1:])
