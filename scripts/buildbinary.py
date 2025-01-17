#!/usr/bin/env python3
# Tool to check final CanBoot binary size
#
# Copyright (C) 2022  Kevin O'Connor <kevin@koconnor.net>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import sys, argparse

ERR_MSG = """
The CanBoot binary is too large for the configured APPLICATION_START.

Rerun "make menuconfig" and either increase the APPLICATION_START or
disable features to reduce the final binary size.
"""

def main():
    parser = argparse.ArgumentParser(description="Build CanBoot binary")
    parser.add_argument("-b", "--base", help="Address of flash start")
    parser.add_argument("-s", "--start", help="Address of application start")
    parser.add_argument("input_file", help="Raw binary filename")
    parser.add_argument("output_file", help="Final binary filename")
    args = parser.parse_args()

    start = int(args.start, 0)
    base = int(args.base, 0)
    max_size = start - base

    f = open(args.input_file, 'rb')
    data = f.read()
    f.close()

    if len(data) > max_size:
        msg = "\nMaximum size %d. Current size %d.\n\n" % (max_size, len(data))
        sys.stderr.write(ERR_MSG + msg)
        sys.exit(-1)

    f = open(args.output_file, 'wb')
    f.write(data)
    f.close()

if __name__ == '__main__':
    main()
