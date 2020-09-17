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
import getopt
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
       pylogsparser - parsing library with XML normalizers -  by Wallix
       why to rewrite it?? Just use existing Just find out how to use
       Options:
           -o then c for csv (-oc), h for html (-oh)
           -y auto answer yes
           ...
"""
# Get startup options using getopt
    try:
        opts, args = getopt.getopt(argv, "hi:o:d:D:", ["ifile=", "ofile=",
                                                       "date=", "dir="])
    except getopt.GetoptError as err:
        print(err)
        print('Error use format palba.py -i <inputfile>|<ipnutfolder> \
              -o <outputfile> -d YYYY/MM/dd')
        sys.exit(2)

    for startup_opt, startup_arg in opts:
        if '-D' or '--dir' in startup_opt:
            dread(startup_arg)  # read given directory and read log files
        elif '-i' or '--ofile' in startup_opt:
            None


if __name__ == '__main__':
    main(sys.argv[1:])
