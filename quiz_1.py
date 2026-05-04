# Question 1
# True or False: The Hidden Message Problem is a well-defined computational problem.
# - False:
#     The Hidden Message Problem is introduced in bioinformatics 
# (e.g., in the Rosalind/CS50 Bioinformatics context) as a storytelling problem 
# to motivate algorithms (like finding frequent k-mers, motifs, etc.), 
# but by itself it is not well-defined computationally — it needs to be 
# reformulated into a precise problem (like “Frequent Words Problem” or 
# “Motif Finding Problem”).The Hidden Message Problem is introduced in 
# bioinformatics (e.g., in the Rosalind/CS50 Bioinformatics context) as a 
# storytelling problem to motivate algorithms (like finding frequent k-mers, 
# motifs, etc.), but by itself it is not well-defined computationally — 
# it needs to be reformulated into a precise problem 
# (like “Frequent Words Problem” or “Motif Finding Problem”).

# Question 2
# A variable that can have only two values – True or False – is called what?
# - Boolean

# Question 3
# Compute PatternCount("CGCG", "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC").
# 5

# Question 4
# The expression "True and not (False or False)" returns what?
# - True

# Question 5
# What is the most frequent 3-mer of "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT" ?
# - CCT

# Question 6
# Which data structure in Python consists of a set of key-value pairs?
# - dictionaries

# Question 7
# What is the reverse complement of "GCTAGCT" ?
# - AGCTAGC

# Question 8
# In Python, how do we initialize an empty list named items?
# - items = []

# ---------------------------------------------------------------------------------

# Where in a Genome does DNA replication begin?


# Search for Hidden Messages in Replication Origin


# - What is a Hidden Message in Replication Origin, 
#   that help E. coli genome to figure out where to start?

# Finding oriC Problem
# Input: A genome
# Output: The location of oriC in the genome.
# ill computational problem.

# How does the cell know to begin replication in short oriC?

# Right formulation of the problem
# Hidden Message Problem. Finding a hidden message in a string.
# Input: A string Text (representing replication origin).
# Output: A hidden message in Text.

# Redifine
# Hint:
# For various biological signals, certain words appear surprisingly frequently
# in small regions of the genome.
# AATTT is surprisingly frequent 5-mer in:
# ACAAATTTGCATAATTTCGGGAAATTTCCT

# Formulate again
# Frequent Words Problem: Finding most frequent k-mers in a string.
# Input: A string Text and an integer k.
# Output: All most frequent k-mers in Text.

# A k-mer Pattern is a most frequent k-mer in a text if no other k-mer is more
# frequent than Pattern.
# AATTT is a most frequent 5-mer in:
# ACA AATTT GCAT AATTT CGGGA AATTT CCT

# Replication is performed by DNA polymerase and the initiation of replication
# is mediated by a protein called DnaA.

# DnaA binds to short (typically 9 nucleotides long) segments within the 
# replication origin known as a DnaA box.

# A DnaA box is a hidden message telling DnaA: "bind here!"
# And DnaA wants to see multiple DnaA boxes.

# |Text|² * k
# 4^k + |Text| * k
# |Text| * k * log(|Text|)
# |Text|

# You will later see how a naive and slow algorithm with |Text|² * k
# runtime can be turned into a fast algorighm with |Text| runtime
# (|Text| stands for the length of string Text).


# - Some Hidden Messages are more surprising than others.

# oriC VIBRIO CHOLERAE
# ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC

# Most frequent 9-mers in oriC (all appear 3 times):
# ATGATCAAG
# CTTGATCAT
# TCTTGGATCA
# CTCTTGATC

# It is STATISTICALLY surprising to find 9-mer appearing
# 3 or more times within ~500 nucleotides?

# ATGATCAAG are TACTAGTTC are reverse complements and likely DnaA boxes
# (DnaA does not care what strand to bind to).

# Can we now find Hidden Messages in Thermotoga Petrophila?
# AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGAAAAGAGGTGGTAAAAAA

# No single occurrence of ATGATCAAG or CTTGATCAT from Vibro Cholerae oriC!!!

# Applying the Frequent Wonds Problem to this replication origin:
# AACCTACCA
# ACCTACCAC
# GGTAGGTTT
# TGGTAGGTT
# AAACCTACC
# CCTACCACC

seq = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGAAAAGAGGTGGTAAAAAA"

# make lowercase
seq = seq.lower()

# list of motifs to make uppercase
motifs = [
    "aacctacca",
    "acctaccac",
    "ggtaggttt",
    "tggtaggtt",
    "aaacctacc",
    "cctaccacc"
]

# replace each motif with uppercase version
for motif in motifs:
    seq = seq.replace(motif, motif.upper())

print(seq)

# aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatGGTAGGTTTggtGGTAGGTTTtgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaAACCTACCAccaaactctgtattgaccattttaggacaacttcagggtGGTAGGTTTctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaAACCTACCActtACCTACCACttACCTACCACccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaAACCTACCAcctgcgtcccctattatttactactactaataatagcagtataattgatctgaaaagaggtggtaaaaaa

# Different genomes -> different hidden messages (DnaA boxes)

# Hidden Messages in Thermotoga Petrophila

# Ori-Finder software confirms that
# CCTACCACC and
# GGATGGTGG
# are candidate hidden messages.

seq = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGAAAAGAGGTGGTAAAAAA"

# make lowercase
seq = seq.lower()

# list of motifs to make uppercase
motifs = [
    "ggtggtagg",
    "ggatggtgg",
    "cctaccacc",
    "ccaccatcc"
]

# replace each motif with uppercase version
for motif in motifs:
    seq = seq.replace(motif, motif.upper())

print(seq)

# aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatg
# gtaggtttGGTGGTAGGttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtat
# taaattgacgaacaattgcatggaattgaatatatgcaaaacaaaCCTACCACCaaactctgtattgacc
# attttaggacaacttcagGGTGGTAGGtttctgaagctctcatcaatagactattttagtctttacaaac
# aatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaa
# aatccagtatccaagccgatttcagagaaacctaccacttacctaccacttaCCTACCACCcgggtggta
# agttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaaCCTACCACCt
# gcgtcccctattatttactactactaataatagcagtataattgatctgaaaagaggtggtaaaaaa

# We learned how to find hidden messages IF oriC is given.
# But we have no clue WHERE oriC is located in a (long) genome.


# - Clumps of Hidden Messages

# Our strategy BEFORE: given a previously known oriC (a 500-nucleotide window),
# find frequent words (clumps) in oriC as candidate DnaA boxes.
# replication origin -> frequent words

# But what if the position of the replication origin within a genome is unknown?

# NEW strategy:
# find frequent words in ALL windows within a genome.
# Windows with clumps of frequent words are candidate replication origins.
# frequent words -> replication origin

# WHAT IS A CLUMP?

# Formal:
# A k-mer forms an (L, t)-clump inside Genome if there is a short
# (length L) interval of Genome in which it appears many (at least t) times.

# Clump Finding Problem: 
# Find patterns forming clumps in a string.
# - Input: A string Genome and integers k (length of a pattern), 
#          L (window length), and t (number of patterns in a clump).
# - Output: All k-mers forming (L, t)-clumps in Genome.

# There exist 1904 different 9-mers forming (500, 3)-clumps in E. coli genome.
# It is absolutely unclear which of them point to the replication origin...

# From a Biological Insight toward an Algorithm for Finding Replication Origin
# - Asymmetry of Replication
# - Why would a computer scientist care about assymetry of replication?
# - Skew Diagrams
# - Finding Frequent Words with Mismatches
# - Open Problems
