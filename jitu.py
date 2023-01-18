import sys
import itertools
from itertools import groupby
from contextlib import contextmanager
from time import time
from sys import stdout
import re

@contextmanager
def duration(outfile=stdout):
    start = time()
    yield
    end = time()
    outfile.write(str(end - start) + '\n')
    

def strMUT(text, dic):
    """ Replaces keys of dic with values of dic in text. 2005-02 by Emanuel Rumpf """
    pat = "(%s)" % "|".join(map(re.escape, dic.keys()))
    return re.sub(pat, lambda m: dic[m.group()], text)

def getEasy(f):
    for header, group in itertools.groupby(f, key = lambda x: x.startswith(">") ):
      if header:
         line = next(group)
         tag = line[1:].strip().split()
      else:
         sequence = ''.join(line.strip() for line in group)
         yield tag, sequence.strip()

def getSeqD(fastaFiler = "Genome.fasta"):
   """

   """
   seqD = {}
   tube =[] 
   with open(fastaFiler, 'r' ) as inpFast:
    for h, seq in getEasy(inpFast):
        seqD[tuple(h)]= seq
        tube.append(tuple(h))
   return tube, seqD
