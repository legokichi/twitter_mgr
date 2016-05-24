# coding: utf-8
import csv
from api import *

target = ""
filename = "log2.tsv"

dels = read_tsv_file(filename)
for _del in dels:
    id = _del[0]
    author = _del[2]
    if target == author:
        print "\t".join(list(_del))
    
print "ok"


