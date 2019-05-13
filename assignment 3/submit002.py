import os
import sys


cwd = os.getcwd() 
filename = cwd + "/33609_reads.txt"
with open(filename, 'r') as fobj:
    all_lines = fobj.read().splitlines()

n = int(input("Number of reads: "))
a = set()
from random import randint
while len(a) < n:
	a.add(randint(0, len(all_lines)-1))

reads = []
for i in a:
	reads.append(all_lines[i])
reads = sorted(reads)

for read in reads:
	print (read)


def whether_opt(n, reads):
	k_mers = set()
	for re_ad in reads:
		for i in range(0, len(re_ad)-n+1):
			k_mers.add(re_ad[i:i+n])
	prefixes = set()
	suffixes = set()
	for kmer in k_mers:
		prefixes.add(kmer[:-1])
		suffixes.add(kmer[1:])
	return prefixes == suffixes

READ_LENGTH = len(reads[0])
for n in range(READ_LENGTH, 1, -1):
	if whether_opt(n, reads):
		print(n)
		break