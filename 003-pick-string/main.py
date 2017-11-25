import argparse
import requests
import time

parser = argparse.ArgumentParser(description='Sending http request one by one')

parser.add_argument("--file", help="filename",
                    default="httpbody.txt", type=str)


args = parser.parse_args()
print type(args.file)
print args.file


bodys = []

httpm = {}
with open(args.file, 'r') as infile:
    for line in infile:
        try:
            jret = json.loads(line)
        except ValueError:
            print 'error'
        if 'cmd' in jret:
            httpm[jret['cmd']] = line
        else:
            httpm['nocmd'] = line

print httpm.keys()
