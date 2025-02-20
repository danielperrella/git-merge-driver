#!/usr/bin/env python3

import argparse
from heapq import merge
from profileparser import parse
from comparator import compare
from xmlgenerator import generatexml
from writerutils import writeonfile

# Initialize parser
parser = argparse.ArgumentParser()


parser.add_argument("Our",      type=str, help = "Tmp filepath to our version of the conflicted file")
parser.add_argument("Base",     type=str, help = "Tmp filepath to the base version of the file")
parser.add_argument("Other",    type=str, help = "Tmp filepath to the other branches version of the file")
parser.add_argument("Filename", type=str, help = "Placeholder / real file name")

# parser.add_argument("%A", "--Our", help = "Tmp filepath to our version of the conflicted file")
# parser.add_argument("%O", "--Base", help = "Tmp filepath to the base version of the file")
# parser.add_argument("%B", "--Other", help = "Tmp filepath to the other branches version of the file")
# parser.add_argument("%P", "--Filename", help = "Placeholder / real file name")
# parser.add_argument("%L", "--Size", help = "Conflict marker size (to be able to still serve according to this setting)")

args = parser.parse_args()

print('args.Our:',args.Our)
print('args.Base:',args.Base)
print('args.Other:',args.Other)
print('args.Filename:',args.Filename)
 
try:
    parse1 = parse(args.Our)
    parse2 = parse(args.Other)
    merged = compare(parse1,parse2)
    print('merged complete')
    outputxml = generatexml(merged)
    writeonfile(outputxml,args.Our,'')
except Exception as e:
    print(e)