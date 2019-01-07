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
#~ import sys
import re
import string
import unicodedata
#~ import getopt
#~ import os
#~ import transliterate
import pyarabic.trans
import pyarabic.unshape
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

#~ @staticmethod 
def is_arabic_bidi(letter):
    try: 
        return unicodedata.name(letter).startswith("ARABIC")
    except:
        return False

class Adawat:
    def __init__(self,):
        pass
    @staticmethod        
    def segment_language(text):
        """
        Detect language
        """
        if not text: return text
        resultlist = []
        if re.search(u"[\u0600-\u06ff]", text[0]):
            arabic = True
        else:
            arabic = False
        actual_text = u""
        for  k in text:
            if re.search(u"[\u0600-\u06ff]", k):
                if arabic:
                    actual_text += k
                else:
                    resultlist.append(('latin', actual_text))
                    arabic = True
                    actual_text = k
            elif re.search(u"[\s\d\?, :\!\(\)]", k):
                actual_text += k
            else:
                if arabic:
                    i = len(actual_text)
                    temp_text = u""
                    while not re.search(u"[\u0600-\u06ff]", actual_text[i:i+1]):
                        i -= 1
                    temp_text = actual_text[i+1:]
                    actual_text = actual_text[:i+1]
                    resultlist.append(('arabic', actual_text))
                    arabic = False
                    actual_text = temp_text+k
                else:
                    actual_text += k
        if arabic:
            resultlist.append(('arabic', actual_text))
        else:
            resultlist.append(('latin', actual_text))
        return resultlist



           
    def delimite_language(self,text, tag="\\aRL"):
        if not tag:
            tag = "\\aRL"
        new_chunks_list = [] 
        chunks = self.segment_language(text)
        for (lang, chunk) in chunks:
            if lang == "arabic":
                if tag  == "\\begin{arab}":
                    new_chunks_list.append("\\begin{arab}\n%s\n\end{arab}"%chunk)
                else:
                    new_chunks_list.append("%s{%s}"%(tag, chunk))
            else:
                new_chunks_list.append(chunk)
        return u" ".join(new_chunks_list)
        
    def delimite_language_bidi(self, text, bidi_function):
        new_chunks_list = [] 
        chunks = self.segment_bidi(text)
        #~ print(chunks)
        if not chunks: 
            return text
        for (lang, chunk) in chunks:
            if lang == "arabic":
                    new_chunks_list.append(bidi_function(chunk))
            else:
                new_chunks_list.append(chunk)
        return u"".join(new_chunks_list)
    @staticmethod
    def segment_bidi(text):
        """
        Detect language
        """
        if not text: return text
        resultlist = []
        if is_arabic_bidi(text[0]):
            arabic = True
        else:
            arabic = False
        actual_text = u""
        for  k in text:
            if is_arabic_bidi(k):
                if arabic:
                    actual_text += k
                else:
                    resultlist.append(('latin', actual_text))
                    arabic = True
                    actual_text = k
            else: # latin
                if not arabic:
                    actual_text += k
                else:
                    resultlist.append(('arabic', actual_text))
                    arabic = False
                    actual_text = k
        if arabic:
            resultlist.append(('arabic', actual_text))
        else:
            resultlist.append(('latin', actual_text))
        return resultlist        
    @staticmethod        
    def reshape(text, nb_col):
        """ return latex text"""
        if not nb_col:
            nb_col =2
        lines = text.split("\n")
        newlines =[]
        for i in range(0, len(lines)-1, nb_col):
            newlines.append(u"\t".join(lines[i:i+nb_col]))
        return  u"\n".join(newlines)
    @staticmethod        
    def tabulize_md(text, sep="\t"):
        """
        Convert lines into markdown 
        return Text
        """
        if not sep:
            sep="\t"
        lines = text.splitlines()
        lines =[l.strip() for l in lines]
        lines =[l for l in lines if l]
        resulttext = ""
        for line in lines:
            fields = line.split(sep)
            resulttext += u" | ".join(fields) + "\n"
        return resulttext
        
    @staticmethod        
    def tabulize_html(text, sep="\t"):
        """
        Convert lines into html
        return Text
        """
        if not sep:
            sep="\t"
        lines = text.splitlines()
        lines =[l.strip() for l in lines]
        lines =[l for l in lines if l]
        resulttext = "<table>\n"
        for line in lines:
            fields = line.split(sep)
            resulttext += u"<tr><td>" +u" </td><td>".join(fields) + "</td></tr>\n"
        resulttext += u"</table>\n"
        
        return resulttext
    #~ @staticmethod
    def tabulize(self, text, sep="\t", format_display="latex"):
        """
        Convert lines into Latex tabular
        return Text
        """
        if not sep:
            sep="\t"
        
        if not format_display:
           return self.tabulize_latex(text, sep)
        elif format_display.lower() == "markdown":
           return self.tabulize_md(text, sep)
        elif format_display.lower() == "html":
           return self.tabulize_html(text, sep)
        else:
           return self.tabulize_latex(text, sep)           

    #~ @staticmethod
    def tabulize_latex(self, text, sep="\t"):
        """
        Convert lines into Latex tabular
        return Text
        """
        if not sep:
            sep ="\t"
        lines = text.splitlines()
        lines =[l.strip() for l in lines]
        lines =[l for l in lines if l]
        resulttext = ""

        if len(lines)>1:
            
            length = len(lines[0].split(sep))
            param = "|c"*length+"|"
            resulttext = u"\\begin{table}\n \\begin{tabular}{"+param+u"}\n"
            for line in lines:
                #~ line = delimite_language(line)
                fields =[self.delimite_language(f) for f in line.split(sep)]
                resulttext += u'\\hline '+" & ".join(fields) + "\\"*2+"\n"
            resulttext += u"""\hline\n
    \\end{tabular}\n
    \\label{mytab:table}\n
    \\caption{mytab:table}\n
     \\end{table}\n
                        """
        return resulttext
    @staticmethod        
    def itemize(text, tag="itemize"):
        """
        Convert lines into Latex itemize
        return Text
        """
        if not tag:
            tag ="itemize"
        lines = text.splitlines()
        lines = [l.strip() for l in lines]
        lines = [l for l in lines if l]
        # add item tag
        lines = [u"\item "+l for l in lines]
        lines = u"\n".join(lines)

        resulttext = u"\\begin{%s}\n%s \n\\begin{%s}"%(tag, lines, tag)
        return resulttext
    @staticmethod
    def tabbing(text, sep="\t"):
        """
        Convert lines into Latex tabular
        return Text
        """
        if not sep:
            sep="\t"
        lines = text.splitlines()
        if u'' in lines:
            lines.remove(u'')
        resulttext = ""

        if len(lines) > 1:
            length = len(lines[0].split(sep))
            #~param = "|c"*length+"|"
            resulttext = u"\\begin{tabbing}\n"
            resulttext += "\hspace{4cm}\="*length+"\kill\n"
            for line in lines:
                resulttext += " \\> ".join(line.split(sep))+"\\"*2+"\n"
            resulttext += u"""\end{tabbing}\n
                        """
        return resulttext
        
    @staticmethod    
    def csv_to_python_table(text, sep="\t"):
        """
        Convert CSV text to python syntax Array
        return Text
        """
        if not sep:
            sep ="\t"
        lines = text.splitlines()
        if u'' in lines:
            lines.remove(u'')
        resulttext = ""

        if len(lines)>1:
            tablename = lines[0]
            if tablename == "":
                tablename = "#Table"
            else :
                tablename = tablename.split()[0]
            # if there only two lines, the array is a list
            if len(lines) == 2:
                fieldsnames = lines[1].split(sep)
                for i in range(len(fieldsnames)):
                    fieldsnames[i] = "'%s'" % fieldsnames[i].strip()
                resulttext += tablename + "=("+", ".join(fieldsnames)+u")\n"
            else:
                resulttext += tablename+u"={}\n"
                fieldsnames = lines[1].split(sep)
                for i in range(len(fieldsnames)):
                    fieldsnames[i] = fieldsnames[i].strip()
                    resulttext += tablename+u"['%s']={}\n" % fieldsnames[i]

                if len(lines) == 3:
                    for line in lines[1:]:
                        line = line.strip()
                        fields = line.split(sep)
                        for i in range(len(fields)):
                            fields[i] = fields[i].strip()
                ##            fields[i]=re.sub('\\', ''', fields[i])
                            fields[i] = re.sub("'", "\\'", fields[i])
                            fields[i] = re.sub("\"", "\\\"", fields[i])
                        resulttext += tablename+u"[u'%s']={}\n" % fields[0]
                        for i in range(0, len(fields)):
                            if i < len(fieldsnames):
                                fieldname = fieldsnames[i]
                            else:
                                fieldname = u"Field#%d" % i
                                fieldsnames.append(fieldname)
                                resulttext += tablename+u"[u'%s']={}\n" % fieldname

                            resulttext += tablename+u"[u'%s']=u'%s'" % (fieldname, 
                              fields[i])+"\n"

                else:
                    for line in lines[1:]:
                        line = line.strip()
                        fields = line.split(sep)
                        for i in range(len(fields)):
                            fields[i] = fields[i].strip()
                ##            fields[i] = re.sub('\\', ''', fields[i])
                            fields[i] = re.sub("'", "\\'", fields[i])
                            fields[i] = re.sub("\"", "\\\"", fields[i])

                        for i in range(1, len(fields)):
                            if i < len(fieldsnames):
                                fieldname = fieldsnames[i]
                            else:
                                fieldname = u"Field#%d" % i
                                fieldsnames.append(fieldname)
                                resulttext += tablename+u"[u'%s']={}\n" % fieldname

                            resulttext += tablename + u"[u'%s'][u'%s']='%s'" % (
                            fieldname, fields[0], fields[i]) +"\n"

        return resulttext
    @staticmethod
    def transliterate(text, code="tim3utf8"):
        if code =="tim2utf8":
            result =  pyarabic.trans.tim2utf8(text)
        elif code =="utf2tim":
            result =  pyarabic.trans.utf82tim(text)
        elif code =="tim2sampa":
            result =  pyarabic.trans.tim2sampa(text)
        else:
            return text
        return result
def main():
    filename, limit, command = grabargs()
    try:
        fl=open(filename);
    except:
        print " Error :No such file or directory: %s" % filename
        sys.exit(0)
    text = fl.read().decode("utf8");
    fl.close();
    if command == "lang":
        print delimite_language(text).encode('utf8')    
    elif command == "tabulize":
        print tabulize(text).encode('utf8')
    elif command == "reshape":
        print " would to reshape text, give n"
        n = int(input())
        print reshape(text, n).encode('utf8')
    elif command == "tabulize_md":
        print tabulize_md(text).encode('utf8')
    elif command == "trans":
        print pyarabic.trans.tim2utf8(text)
    else:
        print "Choose a command from  ", ",".join(COMMANDS)     

    return 0

if __name__ == '__main__':
    main()

