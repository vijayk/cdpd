import json
#
# Literally, take hdp.json and make into a .dot graph-file.
#
# Output written to <stdout> for now.
#

import argparse

parser = argparse.ArgumentParser( description='Process JUnit file/tree' )
parser.add_argument( '--file', '-f',  dest='infile', type=str, default="cdpd-base.json" )
parser.add_argument( '--top-level', '-t',  dest='toplevel', type=str, default=None) 
args = parser.parse_args( )


with open(args.infile, "r") as fd:
    tab = json.load(fd)

print("digraph G {")

if args.toplevel is not None:
   tab = tab[args.toplevel]
for (r,v) in tab.items():
   if type(v) == type({}) and v.has_key("repo-url"):
     color = "black"
     if v.has_key("enable-merge") and v['enable-merge'] == False:
         color="red"
     print("\"%s\" [ color=\"%s\"] ; " % (r,  color))
     if v.has_key("depends-on") and v['depends-on'] is not None:
         for d in v['depends-on']:
            print('"%s" -> "%s" ; '   % (r,  d))
print("}")
 
