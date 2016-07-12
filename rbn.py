#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections, glob, os, sys, zipfile

c = 0
skimmer = ''

def printStats(d):
    
    global c
    for k, v in sorted(d.items(), reverse=False):
         if isinstance(v, dict):
             print("\n" + str(c).rjust(2,'0') + " UTC")
             c += 1
             printStats(v)
         else:
             print("{0} : {1}".format(k.ljust(4), v))

def makehash():
    return collections.defaultdict(lambda : collections.defaultdict(int))

def rollFile(iterator):
    next(iterator)
    prev = next(iterator)
    for item in iterator:
        yield prev
        prev = item

d = makehash()
e = makehash()
f = makehash()
g = makehash()
t = makehash()
u = makehash()
v = makehash()
w = makehash()

def process(rbnFile, skimmer):

    global c
    skimmer = ''.join(skimmer.split())
    fo = os.path.splitext(os.path.basename(rbnFile))[0] + ".txt"

    with open(rbnFile, "r") as r, open(fo, "w") as of:
        print("Processing file: " + rbnFile + "...")
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
        print("RBN File Analyzer, v0.1. Jari Perkiömäki OH6BG\n")
        print("Analyzing file: " + rbnFile + " (" + str(round(fl/1000000)) + " MB)")

        if skimmer is not '':
            
            print("Statistics from skimmer(s): " + skimmer + ".\n")            
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

        print("--- END OF FILE: " + rbnFile + " ---\n")

        sys.stdout = sys.__stdout__

print("Rudimentary RBN Raw Data Analyzer, v0.1. 2016 OH6BG.\n" + 80 * '.')

print("Unzipping the ZIP files...")
for filename in glob.iglob('[0-9]*.zip'):
    with zipfile.ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall(os.getcwd())

print("Found " + str(len(list(glob.iglob('[0-9]*.csv')))) + " CSV file(s).\n")
skimmer = input("Enter the skimmer(s), separated by comma (e.g. OH6BG,SK3W): ")

for filename in glob.iglob('[0-9]*.csv'):
    sys.__stdout__ = sys.stdout
    process(filename,skimmer)

print("Done.")

