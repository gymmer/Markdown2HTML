#!/usr/bin/python
# -*- encoding: utf-8 -*-

'''
This program is main to transform MarkDown to HTML.
MarkDown is .md file, and HTML is .html file.

To start, you can:
  
  1.Put .md files into the 'input' folder. 
    What's more, you can put multiple files.
  
  2.Open the python shell, the run the command:
        python run.py
  
  3.Then, you can find the .txt files in the 'output' folder.
    The .html file-name is the same as .md.

This program only supports English MarkDown file-name,
but suppots both English and Chinese MarkDown file-content.

The core algorithm is Sublime Text plugin, Markdown Preview,
which can be get from https://github.com/revolunet/sublimetext-markdown-preview

Enjoy yourself!

'''

import os
import markdown
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

input_dir = './input'
ouput_dir = './output'
input_file_type = '.md'
ouput_file_type = '.html'

print '\n'
for full_input_file_name in os.listdir(input_dir):
    if os.path.splitext(full_input_file_name)[1]==input_file_type:
            
        print 'Converting ' + full_input_file_name + ' ...'

        file_name = os.path.splitext(full_input_file_name)[0]
        full_input_file_name = input_dir + '/' + full_input_file_name
        full_ouput_file_name = ouput_dir + '/' + file_name + ouput_file_type

        with codecs.open(full_input_file_name, 'r') as ifile:
            in_file_content = ifile.read()
            ou_file_content = markdown.markdown(in_file_content)

            with codecs.open(full_ouput_file_name, 'w', 'gbk') as ofile:
                ofile.write(ou_file_content)
    
print '\nAll Done!'
