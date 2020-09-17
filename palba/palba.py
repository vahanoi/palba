#!/usr/bin/env python3
"""Created on 18 Nov 2018

Updete on 15 Sep 2020

Palba startup file
Python 3

@author: vahanoi
"""

import sys
import os
import gzip
from optparse import OptionParser
# import log.py
# import datetime
# import re
# import pdb


DEF_FOLDER = '/var/log/nginx'
DEF_OUTPUT_FILE = 'of.txt'


'''Read directory, build list of files and execute file listing
'''


def dread(folder):
    """Directory read

    """
    line = 'x'
#   breakpoint()
    for fname in os.listdir(folder):
        print(folder+'/'+fname)
        if fname.endswith('.gz'):
            try:
                with gzip.open(folder+"/"+fname, 'r') as fopen:
                    while line != '':
                        line = fopen.readline()
                        print(line)
                        breakpoint()
            except IOError:
                print(os.path.dirname(os.path.abspath(__file__)))
                print("Could not read file: ")
            fopen.close()

        elif fname.endswith('.log') or fname.endswith('.log.1'):
            try:
                with open(folder+"/"+fname, 'r') as fopen:
                    while line != '':
                        line = fopen.readline()
                        print()
                        breakpoint()
            except IOError:
                print(os.path.dirname(os.path.abspath(__file__)))
                print("Could not read file: ")
            fopen.close()


def main(argv):
    """ Start a parser and run a main program loop
    Options:
        -d OR --dir for directory
        -i or --ifile for input file
        -o or --ofile for output file name
        ... add some more
    """


parser = OptionParser()


parser.add_option("-d", "--dir", dest="folder", type="string", action="store",
                  help="Log folder to analyse - default /var/log",
                  default="/var/log")
parser.add_option("-i", "--ifile", dest="ifile", type="string", action="store",
                  help="input file for single file analysis")

(options, args) = parser.parse_args()
if options.folder in ("-d", "--dir"):
    dread(options.folder)
elif options.ofile in ("-o", "--ofile"):
    print("do something %s" % args.ofile)
                                             
if __name__ == '__main__':
    main(sys.argv[1:])
