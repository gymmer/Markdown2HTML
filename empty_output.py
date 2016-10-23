#!/usr/bin/python
# -*- encoding: utf-8 -*-

'''
This program is main to empty the 'output' folder.
Only the files in it will be deleted.
The folder will still exist.

To start, you can:
  
  1.Open the python shell, the run the command:
        python empty_output.py

Enjoy yourself!

'''

import os
import markdown
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

ouput_dir = './output'

print '\n'
for file_name in os.listdir(ouput_dir):
    print 'Deleting ' + file_name + ' ...'

    full_file_name = ouput_dir + '/' + file_name
    os.remove(full_file_name)
    
print '\nAll Done!'
