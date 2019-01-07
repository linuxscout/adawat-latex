#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  convert.py
#  
#  Copyright 2016 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
import sys
import re
import string
import argparse
import os

import adawat.adawat

scriptversion = '0.1'
AuthorName="Taha Zerrouki"

MAX_LINES_TREATED=1100000;
COMMANDS = [
"lang",
"tabulize",
"tabulize_md",
"reshape",
"trans",
]           

def grabargs():
    parser = argparse.ArgumentParser(description='Convert Quran Corpus into CSV format.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-c", dest="command", required=True,
    help="Command to excecute [%s]"%", ".join(COMMANDS), metavar="COMMAND")
    
    parser.add_argument("-a", dest="arabictag", nargs='?', 
    help="Type of tag for arabic text", metavar="ARABIC_TAG", const="\aRL")
    
    parser.add_argument("-n", dest="shape", type=int, nargs='?', 
    help="Size of new shape", metavar="SHAPE_SIZE", const=2)
    
    parser.add_argument("-e", dest="enumerate", type=bool, const=False, nargs='?', 
    help="Choose enumerate instead of itemize", metavar="ENUMERATE")

    parser.add_argument("-d", dest="display", nargs='?', 
    help="Display format [latex, markdown, html]", metavar="DISPLAY_FORMAT", const="latex")
    parser.add_argument("-s", dest="sep", nargs='?', 
    help="Separator format [" ",',', ';']", metavar="SEPARATOR")
    
    args = parser.parse_args()
    return args
#~ def usage():
#~ # "Display usage options"
    #~ print "(C) CopyLeft 2009, %s"%AuthorName
    #~ print "Usage: %s -f filename [OPTIONS]" % scriptname
#~ #"Display usage options"
    #~ print "\t[-h | --help]\t\toutputs this usage message"
    #~ print "\t[-v | --version]\tprogram version"
    #~ print "\t[-f | --file= filename]\tinput file to %s"%scriptname
    #~ print "\t[-l | --limit= limit_ number]\tthe limit of treated lines %s"%scriptname
    #~ print "\r\nThis program is licensed under the GPL License\n"

#~ def grabargs():
#~ #  "Grab command-line arguments"
    #~ fname = ''
    #~ limit = 0;
    #~ command =""
    #~ if not sys.argv[1:]:
        #~ usage()
        #~ sys.exit(0)
    #~ try:
        #~ opts, args = getopt.getopt(sys.argv[1:], "hv:f:l:c:",
                               #~ ["help", "version", "file=","limit=", "command="],)
    #~ except getopt.GetoptError:
        #~ usage()
        #~ sys.exit(0)
    #~ for o, val in opts:
        #~ if o in ("-h", "--help"):
            #~ usage()
            #~ sys.exit(0)
        #~ if o in ("-v", "--version"):
            #~ print scriptversion
            #~ sys.exit(0)
        #~ if o in ("-f", "--file"):
            #~ fname = val
        #~ if o in ("-c", "--command"):
            #~ command = val
        #~ if o in ("-l", "--limit"):
            #~ try:
                #~ limit = int(val);
            #~ except:
                #~ limit=MAX_LINES_TREATED;

            
    #~ return fname,limit, command
#~ import re
class consoleInterface:
    def __init__(self,):
        self.adw = adawat.adawat.Adawat()
        
    def update(self, method, text, options):
        """
        
        """
        command = method
        value = text
        tagToUse = options['tagarabic']
        sep = options['sep']
        display = options['sep']
        n = options['display']
        tag = "enumerate" if  options['enumerate'] else "itemize"
        if command == "lang":
            result =  self.adw.delimite_language(value, tag = tagToUse)    
        elif command == "tabulize":
            result = self.adw.tabulize(value, sep, display)
        elif command == "inverse":
            result = pyarabic.unshape.unshaping_text(value)
        elif command == "tokenize":
            tokens = pyarabic.araby.tokenize(value)
            result = u"\n".join(tokens)
        elif command == "tabbing":
            result= self.adw.tabbing(value,sep)
        elif command == "pythonlist":
            result= self.adw.csv_to_python_table(value,sep)
        elif command == "reshape":
            result = self.adw.reshape(value, n)
        elif command == "trans":
            code = self.trans_opt.get()
            result = self.adw.transliterate(value, code)
        elif command == "itemize":
            result = self.adw.itemize(value, tag)
        else: # reset
            result = value
        return result

def main():
    args = grabargs()
    filename = args.filename
    #~ limit = args.limit
    command = args.command
    options={}
    options['tagarabic'] = args.arabictag
    options['sep'] = args.sep
    options['display'] = args.display
    options['shape'] = args.shape
    options['enumerate'] = args.enumerate
    #~ filename, limit, command = grabargs()
    try:
        fl=open(filename);
    except:
        print " Error :No such file or directory: %s" % filename
        sys.exit(0)
    text = fl.read().decode("utf8");
    fl.close();
    ci = consoleInterface()
    result = ci.update(command, text, options)
    print (result)
    return 0

if __name__ == '__main__':
    main()

