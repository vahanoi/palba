'''
Created on 18 Nov 2018
Updete on 15 Sep 2020

Palba startup file
Python 3

@author: vahanoi
'''
import sys
import log
import getopt
import datetime
import re


DefaultFolder='/var/log/nginx'


def loadl():
    #TODO: check if file exist and open in read only mode
    None

def palba():
    None
    
def main (argv):
    ''' Start a parser and run a main program loop
        pylogsparser - parsing library with XML normalizers -  by Wallix
        why to rewrite it?? Just use existing Just find out how to use
        Options:
            -o then c for csv (-oc), h for html (-oh)
            -y auto answer yes
            ...
    
    '''
        # Get startup options using getopt
    try:
        opts, args = getopt.getopt(argv,"hi:o:d:D:",["ifile=","ofile=","date=","directory="])
    except getopt.GetoptError as err: # FIXME: not throwing error correctly - 
        print(err)
        print('Error use format palba.py -i <inputfile>|<ipnutfolder> -o <outputfile> -d YYYY/MM/dd')
        sys.exit(2)

#TODO: check input options from command line sys.argv[]
     
    for o,a in opts:
        if o == -D or o == --Directory:
            None 
    while True:      
        if len(sys.argv)==1:
            print ('Entering default mode - analyse %s folder' % DefaultFolder)
            break
        else:
            print('Entering command line mode - Check command line options')
            print (len(sys.argv))
            for option in sys.argv:
                #TODO: Check options provided and create table with them
                if str(option)=='-oh':
                    None
                elif str(option)=='-oc':
                    None    
                print (str(option))
            break
if __name__ == '__main__':
    main(sys.argv[1:])
