# We are now ready to discuss the replication process in more detail. 
# As illustrated in the figure below (top), the two complementary DNA strands 
# running in opposite directions around a circular chromosome unravel, starting at ori. 
# As the strands unwind, they create two replication forks, which expand in 
# both directions around the chromosome until the strands completely separate 
# at the replication terminus (denoted ter). The replication terminus is 
# located roughly opposite to ori in the chromosome.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "naive_replication.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DirectionalDNA.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: 
# Four imaginary DNA polymerases at work replicating a chromosome as the 
# replication forks extend from ori to ter. The blue strand is directed clockwise, 
# and the green strand is directed counterclockwise.

# ----------------------------------------------------------------------------------
# An important thing to know about replication is that a DNA polymerase does not 
# wait for the two parent strands to completely separate before initiating 
# replication; instead, it starts copying while the strands are unraveling. 
# Thus, just four DNA polymerases (each responsible for one half-strand) 
# can all start at ori and replicate the entire chromosome. To start replication, 
# a DNA polymerase needs a primer, a very short complementary segment 
# (shown in red in the figure below) that binds to the parent strand and 
# jump starts the DNA polymerase. After the strands start separating, 
# each of the four DNA polymerases starts replication by adding nucleotides, 
# beginning with the primer and proceeding around the chromosome from ori to 
# ter in either the clockwise or counterclockwise direction. When all four 
# DNA polymerases have reached ter, the chromosome’s DNA will have been 
# completely replicated, resulting in two pairs of complementary strands 
# (figure below), and the cell is ready to divide.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "naive_replication_complete.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Yet while you were reading the preceding description, 
# biology professors were writing a petition to have us fired and sent 
# back to Biology 101. And they would be right, because our exposition 
# suffers from a major flaw; we only described the replication process 
# in this way so that you can better appreciate what we are about to reveal.

# ---------------------------------------------------------------------------------

# The problem with our current description is that it assumes that DNA polymerases 
# can copy DNA in either direction along a strand of DNA (i.e., both 5' → 3' 
# and 3' → 5'). However, nature has not yet equipped DNA polymerases with this 
# ability, as they are unidirectional, meaning that they can only traverse a 
# template strand of DNA in the 3' → 5' direction. Notice that this is opposite 
# from the 5' → 3' direction of DNA. 

# STOP and Think: If you were a unidirectional DNA polymerase, how would you 
# replicate DNA? How many DNA polymerases would be needed to complete this task?

# ----------------------------------------------------------------------------------

# The unidirectionality of DNA polymerase requires a major revision to our naive 
# model of replication. Imagine that you decided to walk along DNA from ori to ter. 
# There are four different half-strands of parent DNA connecting ori to ter, 
# as highlighted in the figure below. Two of these half-strands are traversed 
# from ori to ter in the 5' → 3' direction and are thus called forward half-strands 
# (represented by thin blue and green lines in the figure below). 
# The other two half-strands are traversed from ori to ter in the 3' → 5' direction 
# and are thus called reverse half-strands (represented by thick blue and 
# green lines in the figure below).

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "half_strands.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: 
# Complementary DNA strands with forward and reverse half-strands shown as thin 
# and thick lines, respectively.

# ----------------------------------------------------------------------------------

# While biologists will feel at home with the following description of DNA replication, 
# those new to biology may find it overloaded with new terms. If it seems too biologically complex, 
# then feel free to skim this section, as long as you believe us that the replication 
# process is asymmetric, i.e., that forward and reverse half-strands have very different 
# fates with respect to replication.

# Since a DNA polymerase can only move in the reverse (3' → 5') direction, 
# it can copy nucleotides non-stop from ori to ter along reverse half-strands. 
# However, replication on forward half-strands is very different because a DNA polymerase 
# cannot move in the forward (5' → 3') direction; on these half-strands, a DNA polymerase 
# must replicate backwards toward ori. Take a look at the figure below to see why this must be the case.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "replication_fork.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: Replication begins at ori (primers shown in red) with the synthesis of 
# fragments on the reverse half-strands (shown by thick lines). 
# A DNA polymerase must wait until the replication fork has opened some (small) 
# distance before it starts copying the forward half-strands (shown by thin lines) backward to ori.

# ----------------------------------------------------------------------------------

# On a forward half-strand, in order to replicate DNA, a DNA polymerase must wait for the 
# replication fork to open a little (approximately 2,000 nucleotides) until a new primer 
# is formed at the end of the replication fork; afterwards, the DNA polymerase starts 
# replicating a small chunk of DNA starting from this primer and moving backward in 
# the direction of ori. When the two DNA polymerases on forward half-strands reach ori, 
# we have the situation shown in the figure below.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "asymmetric_replication.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: The daughter fragments are now synthesized (with some delay) on the 
# forward half-strands (shown by thin lines).

# ----------------------------------------------------------------------------------

# Note the contrast between the correct replication figure (top) and the incorrect replication figure (bottom).

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "asymmetric_replication_right.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "naive_replication_wrong.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# ----------------------------------------------------------------------------------
# After this point, replication on each reverse half-strand progresses continuously; however, 
# a DNA polymerase on a forward half-strand has no choice but to wait again until the replication 
# fork has opened another 2,000 nucleotides or so. It then requires a new primer to begin 
# synthesizing another fragment back toward ori. On the whole, replication on a forward 
# half-strand requires occasional stopping and restarting, which results in the synthesis 
# of short Okazaki fragments that are complementary to intervals on the forward half-strand. 
# You can see these fragments forming in the figure below.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "okazaki.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: The replication fork continues growing. 
# Only one primer is needed for each of the reverse half-strands (shown by thick lines), 
# while the forward half-strands (shown by thin lines) require multiple primers in order 
# to synthesize Okazaki fragments. Two of these primers are shown in red on each forward half-strand.

# ----------------------------------------------------------------------------------

# When the replication fork reaches ter, the replication process is almost complete, 
# but gaps still remain between the disconnected Okazaki fragments, as shown in the figure below.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "asymmetric_replication_almost_complete.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: Replication is nearly complete, as all daughter DNA is synthesized. 
# However, half of each daughter chromosome contains disconnected Okazaki fragments.

# ----------------------------------------------------------------------------------

# Finally, consecutive Okazaki fragments must be sewn together by an enzyme called DNA ligase, 
# resulting in two intact daughter chromosomes, each consisting of one parent strand and one 
# newly synthesized daughter strand, as shown in the figure below. In reality, 
# DNA ligase does not wait until after all the Okazaki fragments have been replicated to 
# start sewing them together.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "asymmetric_replication_complete.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: Okazaki fragments have been sewn together, resulting in two intact daughter chromosomes.

# ----------------------------------------------------------------------------------

# Biologists call a reverse half-strand (thick lines) a leading half-strand since a single DNA 
# polymerase traverses this half-strand non-stop, and they call a forward half-strand (thin lines) 
# a lagging half-strand since it is used as a template by many DNA polymerases stopping and 
# starting replication.

# If you are confused about the differences between the leading and lagging half-strands, 
# you are not alone — we and legions of biology students are also confused. 
# The confusion is exacerbated by the fact that different textbooks use different 
# terminology depending on whether the authors intend to refer to a leading template 
# half-strand or a leading half-strand that is being synthesized from a (lagging) 
# template half-strand. You hopefully see why we have chosen the terms "reverse" and 
# "forward" half-strands in an attempt to mitigate some of this confusion.

# Below is an excellent YouTube video helping to visualize the replication process.

# -----------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DNA.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

https://www.youtube.com/watch?v=Qqe4thU-os8

# Where? 
# - In the Nucleus, not all cells have a nucleus, such as Prokaryotes cells. (With nucleus: Eukaryotes cells).
# Both still do DNA replication.

# When?
# - Before it devides, so the new daughter cell can also get a copy of DNA.
# In the Eukoryotes cells, that's going to be before Mitosis (M phase) or Miosis, in the time known as "Interphase".

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "interphase.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()


# Key Players: Enzymes (-ase)

# - Helicase: "The Unzipper" Unzips the DNA, breaking the hydrogen bonds between the bases.
# - DNA Polymerase: "The builder", it replicates DNA molecules to build a new strand of DNA (adds new nucleotides to the new strand).
# - Primase: "The initialiser" Adds a short RNA primer to the DNA strand, so the DNA Polymerase can start adding nucleotides.
# - Ligase: "The Gluer" Seals the gaps between the Okazaki fragments on the lagging strand.


# DNA Replication starts at the "Origin of Replication" (Ori), usually this part is identified by certain DNA sequences.
# (Typically, eukaryotes have multiple Origins, Prokaryotes have only one).

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "ori.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# At the Origin, Helicase "The Unzipper" comes in and unwinds the DNA.
# You don't want these strands to come back together, 
# so single-strand binding proteins (SSBPs) bind the DNA strands to keep them separated.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "SSB.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Topoisomerase keeps the DNA from supercoiling.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "Topoisomerase.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Primase "The Initialiser" comes in and makes RNA primers on both strands.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "Primase.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Important, because otherwise, DNA Polymerase "The Builder" don't know where to start.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DNA_Polymerase.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DNA_structure.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# The strands are antiparallel, meaning they run in opposite directions.
# We don't say north or south, we say 5' (five prime) to 3' (three prime) or 3' to 5'.
# The sugar of DNA is part of the backbone of DNA, it has carbons.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "carbons.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# The carbons on the sugar are numbered right after the oxygen, in a clockwise direction.
# The 5' carbon is outside of the ring structure.

# You do the same for the other side, but keep in mind that the strands are antiparallel to each other.
# Again after the oxygen, in a clockwise direction, 5' is outside of the ring structure.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "direction.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# This strand on the left runs from 5' to 3',

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "5_to3.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# and the strand on the right runs from 3' to 5'.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "3_to_5.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# DNA Polymerase is building the new strand in the 5' to 3' direction.
# This means it moves along the old template strand in the 3' to 5' direction.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DNA_Polymerase_building.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# As DNA unwinds, because DNA Polymerase can only build the new strand in the 5' to 3' direction,
# it has to keep racing up where the unwinding is happening.
# It is known as the lagging strand.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DNA_Polymerase_building_1.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# On this "Lagging Strand", Primers have to keep being placed in order for DNA Polymerase to build.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "DNA_Polymerase_lagging.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# These fragments are called Okazaki Fragments.
# Primers have to get replaced with DNA bases, the primers where made of RNA.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "okazaki_fragments.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Ligase "The Gluer" has to take care of the gaps between the Okazaki fragments, sealing them together.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "Ligase.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# At the end of replicating, you have two identical double helix DNA molecules from your one original double helix DNA molecule.

# SEMI-CONREVATIVE, because the two copies, each contain one old original strand and one newly made one.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "semi-conservative.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# ----------------------------------------------------------------------------------
# 1.3 Peculiar Statistics of the Forward and Reverse Half-Strands

# Fortunately, we already know how to count the number of occurrences of C in a window 
# of ExtendedGenome: use the function PatternCount()! We can therefore define the following 
# function that takes strings Genome and symbol as input and returns the symbol array 
# of Genome corresponding to symbol.

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

Code Challenge (1 point): Re-type this algorithm into the code window below.


# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    # This dictionary will hold the result: keys are start indices i (0..n-1) and values are counts of symbol in the corresponding window.
    array = {}
    # Stores the length of Genome in the variable n. Example: for "AAAAGGGG", n will be 8.
    n = len(Genome)
    # Builds ExtendedGenome by concatenating Genome with its first n//2 characters. 
    # This simulates a circular genome so windows that cross the end wrap around to the start.
    # Example: Genome="AAAAGGGG", n//2 = 4, so ExtendedGenome = "AAAAGGGG" + "AAAA" = "AAAAGGGGAAAA".
    ExtendedGenome = Genome + Genome[0:n//2]
    # A loop that iterates i from 0 to n-1. Each i represents a starting position in 
    # the original genome for which we compute the symbol count in the window.
    for i in range(n):
        # Example for i=0 with the sample: substring is "AAAA", PatternCount("AAAA", "A") → 4, so array[0] = 4.
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array


# Reproduce the PatternCount function here.
# Defines PatternCount, which counts how many times Pattern occurs in Text (exact substring matches). 
# Parameters: Text (string to search in) and Pattern (string to search for).
def PatternCount(Text, Pattern):
    # Initializes an integer count to zero. This accumulates matches.
    count = 0
    # Loops i over all starting positions in Text where a full Pattern can fit. 
    # If len(Pattern) is greater than len(Text), the range is empty and the loop body 
    # is not executed (resulting in 0 matches).
    for i in range(len(Text)-len(Pattern)+1):
        # For each i, extracts the substring of Text starting at i and of length len(Pattern). 
        # If that substring equals Pattern, then a match is found.
        if Text[i:i+len(Pattern)] == Pattern:
            # Increments the count when a match is found.
            count += 1
    # Returns the total number of matches found.
    return count   

Genome = open("E_coli_genome.txt", "r").read()
symbol = "C"

print(SymbolArray(Genome, symbol))

# --------------------------------------------------------------------------------
# From an inefficient to an efficient algorithm

# Just because SymbolArray() is inefficient does not imply that a quick algorithm 
# for constructing a symbol array does not exist. To develop a faster algorithm, 
# we will think about what currently happens in the for loop within SymbolArray(), 
# reproduced below.

def SymbolArray(Genome, symbol):
    array = []
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        count = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
        array.append(count)
    return array

# To compute PatternCount(symbol, ExtendedGenome[0:n//2]), 
# the algorithm consults n//2 positions of ExtendedGenome, 
# starting at position 0. It then returns all the way back to position 1 of 
# ExtendedGenome to compute PatternCount(symbol, ExtendedGenome[1:1+(n//2)], symbol), 
# which consults positions 1 through 1+(n//2) of ExtendedGenome.

# Can we generate a symbol array using only one pass down ExtendedGenome and 
# therefore only n+(n//2) total symbol comparisons? Such a method would reduce 
# the running time of an algorithm generating the symbol array from a 
# few days to a few seconds.

# ----------------------------------------------------------------------------------
# To speed up SymbolArray(), we observe that when we slide a window one symbol to the right, 
# the number of occurrences of symbol in the window does not change much, and so 
# regenerating the entire array from scratch is inefficient.

# For example, in "CTGCTTCGCCCGCCGGACCGGCCTCGTGATGGGGTATGCTTCGCCCGCCGGA", 
# the number of occurrences of C in the window starting at position 1 ("TGCTTCGCCCGCCGGA") 
# can be easily computed from the number of positions of occurrences of C in the window 
# starting at position 0 ("CTGCTTCGCCCGCCGG"). Indeed, we can view this sliding of the 
# window as simply removing the first symbol from the window (C) and adding a new symbol 
# to the end (A). Thus, when shifting the window right by one symbol, 
# the number of occurrences of C in the window decreased by 1 and increased by 0. 
# Once we compute that array[0] is equal to 8, we automatically know that array[1] is equal to 7.

# -----------------------------------------------------------------------------------

# This idea motivates the following algorithm, 
# in which we only need to consider two symbols each time we slide the window.  
# It uses a form of range,

for i in range(a, b)

# in which we consider values of i starting with a and ending with b-1.

# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))


# What is the problem?

# We want to know, for every starting position i in a genome string, 
# how many times a symbol (like "A") appears in a sliding window of length n/2.

# n = length of the genome

# Window size = n//2

# We slide the window one step at a time around a “circular” genome.


# The FasterSymbolArray function
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]


# 1. array = {}
# A dictionary to store the answer.
# Keys = index (0…n-1).
# Values = count of symbol inside the current window.

# 2. n = len(Genome)
# The length of the genome string.

# 3. ExtendedGenome = Genome + Genome[0:n//2]
# We “extend” the genome by copying its first half and sticking it at the end.
# Why? → So when the window slides past the end, it can wrap around like a circle.


# First window
array[0] = PatternCount(symbol, Genome[0:n//2])


# Look at the first window: Genome[0:n//2].

# Count how many times symbol occurs inside it.

# Save it as array[0].

# ⚠️ Small bug: 
# arguments to PatternCount are flipped here (but I’ll explain what the code thinks it’s doing). 
# It should be PatternCount(Genome[0:n//2], symbol) (Text first, Pattern second).


# Sliding the window
for i in range(1, n):
    array[i] = array[i-1]

    if ExtendedGenome[i-1] == symbol:
        array[i] = array[i]-1
    if ExtendedGenome[i+(n//2)-1] == symbol:
        array[i] = array[i]+1


# Now we move the window from left to right:
# - Start with the previous count: array[i] = array[i-1].
# - When you slide the window:
    # - One character falls out on the left (ExtendedGenome[i-1]).
    # - One character comes in on the right (ExtendedGenome[i+(n//2)-1]).
# If the character that left was the symbol, subtract 1.
# If the character that entered was the symbol, add 1.

# This way we don’t recount everything every time. We only adjust by ±1.


# Return result
return array


# Now we have all counts for all windows.



# The PatternCount function
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count


# This is a helper function.
# It counts how many times Pattern appears in Text.

# Example:

# PatternCount("A", "AAAG")

# → Looks at "A", "A", "A", "G"
# → Matches 3 times
# → Returns 3


# The input/output part
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))

# Reads two lines from input:
# - First line = Genome
# - Second line = symbol
# Runs FasterSymbolArray(Genome, symbol)
# Prints the result dictionary.


# Big Picture

# SymbolArray (your first version) recomputed the count from scratch for every window. 
# That’s slow (O(n²)).

# FasterSymbolArray is smart:
# - It computes the first window count with PatternCount.
# - Then, as the window slides, it just updates the count by checking the characters that 
#   left and entered.
# - Much faster: O(n) time.


# ------------------------------------------------------------------------------------------

# Finding ori

# The figure below visualizes the symbol array for E. coli and symbol equal to 'C'. 
# Notice the clear pattern in the data! The maximum value of the array occurs around position 1600000, 
# and the minimum value of the array occurs around position 4000000. We can therefore infer that 
# the reverse half-strand begins around position 1600000, and that the forward half-strand 
# begins around position 4000000. Because we know that ori occurs where the reverse half-strand 
# transitions to the forward half-strand, we have discovered that ori is located in the 
# neighborhood of position 4000000 of the E. coli genome, without ever needing to put on a lab coat!

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "e-coli_symbol_array_c.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: A plot of the symbol array for the E. coli genome for symbol equal to 'C'.


# 1. What are we even trying to find?

# We’re looking for the origin of replication (ori) in the E. coli genome.
# That’s the place in the DNA where replication starts.

# DNA replication in bacteria:
# - The circular genome has two halves (two replichores).
# - Replication starts at ori and goes in two opposite directions 
#   (like unzipping a zipper in both directions).
# - Half the genome is replicated on one “forward strand,” the other half on the “reverse strand.”

# So ori is the “border” where one half-strand ends and the other half-strand begins.


# 2. What is a symbol array again?

# - We pick a symbol, e.g. 'C'.
# - We count how many times 'C' appears in a sliding window of length n/2 around the circular genome.
# - For each genome position, we record that number.
# Result: a curve that shows how “C-rich” each half of the genome is.


# 3. Why does this matter?

# Bacterial genomes aren’t random — the forward strand has a different nucleotide bias than 
# the reverse strand.
# For E. coli:
# - One half-strand tends to have more C’s.
# - The other half-strand tends to have fewer C’s.

# So when you compute the symbol array:
# - In the region corresponding to the reverse half-strand, the count of C’s in the window is high → maximum.
# - In the region corresponding to the forward half-strand, the count of C’s in the window is low → minimum.


# 4. Why 1,600,000 and 4,000,000?

# The array shows:
# - Around 1,600,000 → the counts of C’s reach a peak (maximum). 
#   This means the window here is filled with the “C-rich” strand → reverse half-strand begins here.
# - Around 4,000,000 → the counts of C’s hit the lowest point (minimum). 
#   This means the window here is in the “C-poor” strand → forward half-strand begins here.

# Because ori is where the switch happens (reverse → forward), the ori is near 4,000,000.


# 5. Super simple analogy 🥞

# Imagine a giant pancake with chocolate chips unevenly spread:
# - The left half has lots of chips (C-rich).
# - The right half has fewer chips (C-poor).

# If you slide a circular cookie-cutter halfway across the pancake and count chips:
# - When your cutter covers the left half → max chip counts.
# - When your cutter covers the right half → min chip counts.
# - The boundary between chip-rich and chip-poor halves = the ori.


# ✅ So the takeaway:
# Max value (~1.6M) → beginning of C-rich half (reverse strand).
# Min value (~4.0M) → beginning of C-poor half (forward strand).

# Ori lies at the transition = around 4.0M.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "ori_4m.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# ______________________________________________________________________

# 1.4 The Skew Diagram

# In the table containing nucleotide counts for T. petrophila (reproduced below), 
# we noted that not just C but also G has peculiar statistics on the forward and 
# reverse half-strands.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "t_petrophila_nucleotide_counts.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# In practice, scientists use a more accurate approach that accounts for both G 
# and C when searching for ori. As the above figure illustrates, the difference 
# between the total amount of guanine and the total amount of cytosine is 
# negative on the reverse half-strand and positive on the forward half-strand.

# ----------------------------------------------------------------------

# Thus, our idea is to traverse the genome, keeping a running total of the 
# difference between the counts of G and C. If this difference starts 
# increasing, then we guess that we are on the forward half-strand; 
# on the other hand, if this difference starts decreasing, 
# then we guess that we are on the reverse half-strand (see figure below).

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "increasing_decreasing_skew.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: Because of deamination, each forward half-strand has more 
# guanine than cytosine, and each reverse half-strand has more 
# cytosine than guanine. The difference between the counts of 
# G and C is therefore positive on the forward half-strand and 
# negative on the reverse half-strand.

# ---------------------------------------------------------------------

# We will keep track of the difference between the total number of 
# occurrences of G and the total number of occurrences of C that we 
# have encountered so far in Genome by using a skew array. 
# This array, denoted Skew, is defined by setting Skew[i] 
# equal to the number of occurrences of G minus the number of 
# occurrences of C in the first i nucleotides of Genome (see figure below). 
# We also set Skew[0] equal to zero.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "skew_array_clipped.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: The skew array for Genome equal to "CATGGGCATCGGCCATACGCC".

# Given a DNA string Genome, we can form its skew array by setting 
# Skew[0] equal to 0, and then ranging﻿ through Genome.  
# At position i of Genome, if we encounter A or T, then we 
# set Skew[i+1] equal to Skew[i]; if we encounter a G, 
# then we set Skew[i+1] equal to Skew[i]+1; if we encounter a C, 
# then we set Skew[i+1] equal to Skew[i]-1.

# Exercise Break (0 points): Give all values of Skew for Genome 
# equal to "GAGCCACCGCGATA" as a collection of space-separated integers. 
# Use the sample dataset below to help!

# Sample Input:
#      CATGGGCATCGGCCATACGCC

# Sample Output:
#      0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2


# "GAGCCACCGCGATA"

# 0 1 1 2 1 0 0 -1 -2 -1 -2 -1 -1 -1 -1

# ---------------------------------------------------------------------

# Code Challenge (3 points): Write a function SkewArray(Genome) that 
# takes as input a DNA string Genome and returns the skew array of 
# Genome in the form of a list whose i-th element is Skew[i]. 
# Then add this function to Replication.py.

import matplotlib.pyplot as plt
# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    # Initialize array with 0 for position 0
    skew = [0]
    # Track running total of G minus C counts
    count = 0
    
    for i in range(len(Genome)):
        # Add previous value to array
        if Genome[i] == 'C':
            count -= 1
        elif Genome[i] == 'G':
            count += 1
        skew.append(count)
    
    return skew

# Example genome
genome = open("E_coli_genome.txt", "r").read()
# Compute skew values
import matplotlib.pyplot as plt

# Compute skew values
skew = SkewArray(genome)

# Plot with colors
plt.figure(figsize=(10,5))

for i in range(len(genome)):
    x_vals = [i, i+1]
    y_vals = [skew[i], skew[i+1]]
    
    if genome[i] == "G":
        plt.plot(x_vals, y_vals, color="green", marker="o")
    elif genome[i] == "C":
        plt.plot(x_vals, y_vals, color="red", marker="o")
    else:
        plt.plot(x_vals, y_vals, color="black", marker="o")

plt.title("Skew Diagram for Genome")
plt.xlabel("Position (i)")
plt.ylabel("Skew[i] = #G - #C")

# ✅ Force y-axis to show only integer ticks between min and max skew
ymin, ymax = min(skew), max(skew)
plt.yticks(range(ymin, ymax+1))

plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# The skew diagram of Genome is defined by plotting i against Skew[i] as 
# i ranges from 0 to len(Genome). The figure below shows the skew 
# diagram for the genome from the previous step.


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "skew_array.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# Figure: (Top) The skew array for Genome equal to 
# "CATGGGCATCGGCCATACGCC", reproduced from the previous step. 
# (Bottom) The skew diagram corresponding to Genome. 
# The skew increases when we encounter G and decreases when we 
# encounter C.

# --------------------------------------------------------------------
# The figure below depicts the skew diagram for a linearized E. coli 
# genome. The pattern is even stronger than the pattern observed when 
# we visualized the symbol array! It turns out that the skew diagram 
# for many bacterial genomes has a similar characteristic shape.

# STOP and Think: After looking at the E. coli skew diagram, where do 
# you think that ori is located in E. coli?

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "skew_diagram_ecoli.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()


# Figure: The skew diagram for E. coli achieves a maximum and minimum 
# at positions 1550413 and 3923620, respectively.

# -------------------------------------------------------------------

# Let’s follow the 5' → 3' direction of DNA and walk along the chromosome 
# from ter to ori (along a reverse half-strand), then continue on from 
# ori to ter (along a forward half-strand). In the figure below, 
# we see that the skew is decreasing along the reverse half-strand and 
# increasing along the forward half-strand. Thus, the skew should achieve 
# a minimum at the position where the reverse half-strand ends and 
# the forward half-strand begins, which is exactly the location of ori!

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "increasing_decreasing_skew (1).png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# -------------------------------------------------------------------
# We have just developed an insight for a new algorithm for locating ori: 
# it should be found where the skew array attains a minimum.

# Minimum Skew Problem: Find a position in a genome where the skew 
# diagram attains a minimum.

# Input: A DNA string Genome.
# Output: All integer(s) i minimizing Skew[i] among all values of i 
# (from 0 to len(Genome)).

# We can outline the following function to find these minimum skew 
# positions, using our subroutine SkewArray(Genome) that generates the 
# skew array from a genome.

def MinimumSkew(Genome):
    # generate an empty list positions
    # set a variable equal to SkewArray(Genome)
    # find the minimum value of all values in the skew array
    # range over the length of the skew array and add all positions achieving the min to positions
    
# Code Challenge (3 points): Write a function MinimumSkew() taking as 
# input a DNA string Genome and returning all integers i minimizing 
# Skew[i] for Genome. Then add this function to Replication.py.

# Hint: make sure to call Skew(Genome) as a subroutine, and keep in 
# mind that Python has a built-in min() function in addition to max().

# Click here for this problem's test datasets.

# Sample Input:

# TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
# Sample Output:

# 11 24
    
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew = SkewArray(Genome)
    # find the minimum value of all values in the skew array
    min_val = min(skew)
    
    i = 0
    for value in skew:
        if value == min_val:
            positions.append(i)
        i += 1
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    skew = [0] # output variable
    count = 0
    
    for i in range(len(Genome)):
        # Add previous value to array
        if Genome[i] == 'C':
            count -= 1
        elif Genome[i] == 'G':
            count += 1
        skew.append(count)
    
    return skew

# Goal of the code
# We want to find all positions in a DNA string where the "skew" is 
# minimized.

# Skew is a number that tells us:
#  +1 for each G
#  -1 for each C
#   0 for A or T

# It’s basically a running “G vs C balance” along the genome.

# SkewArray function

# This builds a list of skew values as we go along the DNA.

def SkewArray(Genome):
    skew = [0]  # start with 0 at the very beginning
    count = 0   # our running skew total

    for i in range(len(Genome)):
        if Genome[i] == 'C':
            count -= 1  # C lowers skew
        elif Genome[i] == 'G':
            count += 1  # G increases skew
        # A or T do nothing
        skew.append(count)  # add current skew to the list
    
    return skew

# Example:
# DNA = "GCCG"

# Start: skew = [0]

# G → +1 → skew = [0, 1]

# C → -1 → skew = [0, 1, 0]

# C → -1 → skew = [0, 1, 0, -1]

# G → +1 → skew = [0, 1, 0, -1, 0]

# So the skew array = [0, 1, 0, -1, 0]

# Notice how we start with 0 at the very beginning. That’s important!

# MinimumSkew function

# This finds all positions where skew is the smallest.

def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)       # get the skew array
    min_val = min(skew)            # find the smallest skew

    i = 0
    for value in skew:             # go through the skew array
        if value == min_val:       # if this value is the minimum
            positions.append(i)    # record its position
        i += 1                     # move to the next position

    return positions

# Example:
# Using skew array [0, 1, 0, -1, 0]

# Minimum skew = -1

# Only at position 3 → return [3]

# ✅ Key points

# Always start skew array with [0]. Otherwise, your positions will be off by 1.

# Count Gs as +1, Cs as -1, A/T as 0.

# Then just find all indices where the skew is the smallest.

# -------------------------------------------------------------------
# STOP and Think: Note that the skew diagram (reproduced below for 
# E. coli) changes depending on where we start our walk along the 
# circular chromosome. Does the minimum of the skew diagram point 
# to the same genomic location regardless of where we begin walking 
# to generate the skew diagram?

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "skew_diagram_ecoli (1).png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()