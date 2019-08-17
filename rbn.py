#!/usr/bin/env python3

import collections
import glob
import os
import sys
import zipfile


def printStats(d):
    
    global c
    for k, v in sorted(d.items(), reverse=False):
         if isinstance(v, dict):
             print("\n%s UTC" % str(c).rjust(2,'0'))
             c += 1
             printStats(v)
         else:
             print("%-10s : %s" % (k.ljust(4), v))


def makehash():
    return collections.defaultdict(lambda : collections.defaultdict(int))


def rollFile(iterator):
    next(iterator)
    prev = next(iterator)
    for item in iterator:
        yield prev
        prev = item


def process(rbnFile, skimmer):

    global c
    skimmer = ''.join(skimmer.split())
    fo = os.path.splitext(os.path.basename(rbnFile))[0] + ".txt"

    with open(rbnFile, "r") as r, open(fo, "w") as of:
        print("Processing file: %s..." % rbnFile)
        sys.stdout = of

        for row in rollFile(r):
            a = row.split(',')
            h = int((a[10].split()[1]).split(':')[0])
            
            if a[0] in skimmer:
  
                d[h][a[5]] += 1 # calls by hour
                e[h][a[6]] += 1 # DXCC by hour
                f[h][a[7]] += 1 # continents by hour
                g[h][a[4]] += 1 # bands by hour

            else:
                
                t[h][a[5]] += 1 # calls by hour
                u[h][a[6]] += 1 # DXCC by hour
                v[h][a[7]] += 1 # continents by hour
                w[h][a[4]] += 1 # bands by hour
                
        statinfo = os.stat(rbnFile)
        fl = statinfo.st_size
        print("RBN File Analyzer, v0.2. (c) Jari Perkiömäki OH6BG\n")
        print("Analyzing file: %s (%d MB)" % (rbnFile, round(fl/1000000)))

        if skimmer:
            
            print("Statistics from skimmer(s): %s\n" % skimmer)
            print("SPOTS BY CONTINENT BY HOUR")
            print(80 * '.')
            printStats(f)
            c = 0

            print("\nSPOTS BY BAND BY HOUR")
            print(80 * '.')
            printStats(g)
            c = 0
            
            print("\nSPOTS OF DXCC COUNTRIES BY HOUR")
            print(80 * '.')
            printStats(e)
            c = 0
            
            print("\nSPOTS OF CALLS BY HOUR")
            print(80 * '.')
            printStats(d)
            c = 0

        else:
            
            print("Statistics from ALL skimmers.\n")            
            print("SPOTS BY CONTINENT BY HOUR")
            print(80 * '.')
            printStats(v)
            c = 0

            print("\nSPOTS BY BAND BY HOUR")
            print(80 * '.')
            printStats(w)
            c = 0
            
            print("\nSPOTS OF DXCC COUNTRIES BY HOUR")
            print(80 * '.')
            printStats(u)
            c = 0
            
            print("\nSPOTS OF CALLS BY HOUR")
            print(80 * '.')
            printStats(t)
            c = 0

        print("\n--- END OF FILE: %s\n" % rbnFile)

        sys.stdout = sys.__stdout__


d = makehash()
e = makehash()
f = makehash()
g = makehash()
t = makehash()
u = makehash()
v = makehash()
w = makehash()
c = 0
skimmer = ''

print("Rudimentary RBN Raw Data Analyzer, v0.2, 2019 OH6BG.")
print(80 * '.')

print("Unzipping the ZIP files...")
for filename in glob.iglob('[0-9]*.zip'):
    with zipfile.ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall(os.getcwd())

print("Found %d CSV file(s).\n" % len(list(glob.iglob('[0-9]*.csv'))))
skimmer = input("Enter the skimmer(s), separated by comma (e.g. OH6BG, SK3W): ")

for filename in glob.iglob('[0-9]*.csv'):
    sys.__stdout__ = sys.stdout
    process(filename, skimmer)

print("Done.")
