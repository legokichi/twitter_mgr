# coding: utf-8
import sys
import csv
from api import read_tsv_file
param = sys.argv

if len(param) != 3:
    print """
Usage:

    python find_author.py [filename] [screen_name]

Example:

    python find_author.py user/log3.tsv duxca >> del.tsv
    
    python find_author.py user/log3.tsv Fukuso_Sutaro| tee -a del.tsv user/Fukuso_Sutaro.tsv
    """
    exit()
 
filename = param[1]
target = param[2]

dels = read_tsv_file(filename)
for _del in dels:
    id = _del[0]
    author = _del[2]
    if target == author:
        print "\t".join(list(_del))
    
print "\n"


