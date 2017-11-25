import argparse
import requests
import time
import json

parser = argparse.ArgumentParser(description='Sending http request one by one')

parser.add_argument("--file", help="filename",
                    default="httpbody.txt", type=str)


args = parser.parse_args()
print type(args.file)
print args.file


bodys = []

httpm = {}
skip = 0
with open(args.file, 'r') as infile:
    for line in infile:
        skip += 1
        try:
            jret = json.loads(line)
        except ValueError:
            print 'error'
            continue
        if 'cmd' in jret:
            httpm.setdefault(jret['cmd'], [])
            httpm[jret['cmd']].append(line[:10])
        else:
            httpm.setdefault('nocmd', [])
            httpm['nocmd'].append(line)
        if skip == 10:
            break


print httpm
