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
import string
import re
# import datetime
# import re
# import pdb


DEF_FOLDER = '/var/log/nginx'
DEF_OUTPUT_FILE = 'of.txt'


'''Read directory, build list of files and execute file listing
'''


def dread(folder):
    """Directory read
    LogFormats:
        host logname user date/time request status

    """
    line = 'x'
    # RegEx string to match log line in http access log
    acces_log_regex =re.compile(r"^(\d{1,3}\.\d+\.\d+\.\d+)\s+([\w-]+)\s+([\w-]+)\s+\[(\d{1,2} \
                                    \/\w{3}\/\d{4})\:(\d{2}\:\d{2}\:\d{2})\s*([\+\-]*\d{0,4}) \
                                    \]\s(\"\"|\".*\")\s(\d{3})\s(\d*)\s(\".*\")\s(\".*\")$")
#   breakpoint()
# should build separate method to read file
    for fname in os.listdir(folder):
        print(folder+'/'+fname)
        if fname.endswith('.gz'):
            try:
                with gzip.open(folder+"/"+fname, 'r') as fopen:
                    for line in fopen:
                        line_elements = acces_log_regex.match(line.decode(encoding='UTF-8'))
                        print(line_elements)
                        # breakpoint()
            except IOError:
                print(os.path.dirname(os.path.abspath(__file__)))
                print("Could not read file: ")
            line = ''
            fopen.close()

        elif fname.endswith('.log') or fname.endswith('.log.1'):
            try:
                with open(folder+"/"+fname, 'r') as fopen:
                    for line in fopen:
                        line_elements = acces_log_regex.match(line)
                        print(line_elements)
                        # breakpoint()
            except IOError:
                print(os.path.dirname(os.path.abspath(__file__)))
                print("Could not read file: ")
            fopen.close()
            line = ''


def main(argv):
    """ Start a parser and run a main program loop
    Options:
        -d OR --dir for directory
        -i or --ifile for input file
        -o or --ofile for output file name
        ... add some more
        optparse - parsing library
    """


parser = OptionParser()


parser.add_option("-d", "--dir", dest="folder", type="string", action="store",
                  help="Log folder to analyse - default /var/log",
                  default="/var/log")
parser.add_option("-i", "--ifile", dest="ifile", type="string", action="store",
                  help="input file for single file analysis")
parser.add_option("-o", "--ofile", dest="ofile", type="string", action="store",
                  help="output file to save results")

# breakpoint()

(options, args) = parser.parse_args()


if options.folder in ("-d", "--dir"):
    dread(options.folder)
elif options.ofile in ("-o", "--ofile"):
    print("do something %s" % args.ofile)
elif options.ifile is not None:
    print(options.ifile)
else:
    dread(options.folder)

if __name__ == '__main__':
    main(sys.argv[1:])
