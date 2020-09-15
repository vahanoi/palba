'''
Created on 18 Nov 2018
Updete on 15 Sep 2020

Palba startup file
Python 3

@author: vahanoi
'''
import sys

def loadl():
    #TODO: check if file exist and open in read only mode
    None

def palba():
    None
    
def main ():
    ''' Start a parser and run a main program loop
        pylogsparser - parsing library with XML normalizers -  by Wallix
        why to rewrite it?? Just use existing Just find out how to use
        Options:
            -o then c for csv (-oc), h for html (-oh)
            -y auto answer yes
            ...
    
    '''
#TODO: check input options from command line sys.argv[]
    while True:      
        if len(sys.argv)==1:
            print ('Entering default mode - analyse /var/log folder')
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
    main()
