#!/usr/bin/env python

"""
Module to run keyword search across a source code and print a snippet of code
(3 lines prior and 3 lines after)
"""

__author__ = "Kannan Piedy"
__copyright__ = ""
__credits__ = ["Kannan Piedy"]
__license__ = "Kannan Piedy"
__version__ = "1.0.1"
__maintainer__ = ""
__email__ = "kannanpiedy@gmail.com"
__status__ = "Test"


import os

def grep(root_path, query):
    result = {}
    for path,subdir,files in os.walk( root_path ):
        for each_file in files:
            with open( path + "/" + each_file, 'r' ) as file_obj:
                all_lines = file_obj.readlines()
                if query in "\n".join(all_lines):
                    max_len = len(all_lines)
                    all_indexes= filter(lambda x: query in all_lines[x],range(len(all_lines)))
                    """
                        Code here begins to mark from 3 lines before the
                        search phrase and 3 lines after search phrase to display.
                    """
                    for each_index in all_indexes: 
                        if (each_index - 3) > 0:
                            if (each_index + 3) < max_len:
                                result[ str(path) + "/" + str(each_file) + " : " + str( each_index ) + " - " + "3," + str( each_index ) + " + " + "3 "] \
                                = "".join(all_lines [ each_index - 3:each_index + 3 ])
                            else:
                                result[ str(path) + "/" + str(each_file) + " : " + str( each_index ) + " - " + "3," + str( max_len )] \
                                = "".join(all_lines [ each_index - 3: ])
                        else:
                            if (each_index + 3) < max_len:
                                result[ str(path) + "/" + str(each_file) + " : " + " 0," + str( each_index ) + " + " + "3 "] \
                                = "".join(all_lines [ :each_index + 3 ])
                            else:
                                result[ str(path) + "/" + str(each_file)] = "".join(all_lines [:])
                    """
                        data collation process completes
                    """
    return result

if __name__ == '__main__':
    root_path = raw_input("Enter the path of the source code : ")
    query = raw_input("Enter search string :")
    result = grep(root_path, query)
    for each_key in result :
        print "*"*10
        print each_key
        print result[each_key]
        print "*"*10