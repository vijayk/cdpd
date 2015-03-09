import json
#
# Literally, take hdp.json and make into a .dot graph-file.
#
# Output written to <stdout> for now.
#

infile = "hdp.json"

with open(infile, "r") as fd:
    tab = json.load(fd)

print("digraph G {")
for (r,v) in tab.items():
   if type(v) == type({}) and v.has_key("repo-url"):
     color = "black"
     if v.has_key("enable-merge") and v['enable-merge'] == False:
         color="red"
     print("\"%s\" [ color=\"%s\"] ; " % (r,  color))
     if v.has_key("depends-on"):
         for d in v['depends-on']:
            print('"%s" -> "%s" ; '   % (r,  d))
print("}")
 
