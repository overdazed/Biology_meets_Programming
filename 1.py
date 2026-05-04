# In the rest of this chapter, we will focus on the relatively easy 
# case of finding ori in bacterial genomes, 
# most of which consist of a single circular chromosome. 
# Research has shown that the region of the bacterial genome encoding ori 
# is typically a few hundred nucleotides long. Our plan is to begin with 
# a bacterium in which ori is known, and then determine what makes this 
# genomic region special in order to design a computational approach for 
# finding ori in other bacteria. Our example is Vibrio cholerae, 
# the pathogenic bacterium that causes cholera; here is the nucleotide 
# sequence appearing in the ori of Vibrio cholerae:

atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc

name = "Mike"
print "Hello %s" % (name)

day = 6
print "03 - %s - 2019" %  (day)
# 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
# 03 - 06 - 2019

my_string = "Helloooo"
print len(my_string)
print my_string.upper()
# --------------------------------------------------------------------------------

count = 0

# --------------------------------------------------------------------------------

3 < 4
5 >= 5
10 == 10
12 != 13

True or False 
(3 < 4) and (5 >= 5)
this() and not that()

if this_might_be_true():
  print "This really is true."
elif that_might_be_true():
  print "That is true."
else:
  print "None of the above."

# 1.
# In the workspace to your right, there is the outline of a function called grade_converter().

# The purpose of this function is to take a number grade (1-100), defined by the variable grade, and to return the appropriate letter grade (A, B, C, D, or F).

# Your task is to complete the function by creating appropriate if and elif statements that will compare the input grade with a number and then return a letter grade.

# Your function should return the following letter grades:

# 90 or higher should get an “A”
# 80 - 89 should get a “B”
# 70 - 79 should get a “C”
# 65 - 69 should get a “D”
# Anything below a 65 should receive an “F”

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)

# --------------------------------------------------------------------------------

# Before thinking about sliding the window down Text, 
# let’s solve the simpler problem of determining whether Pattern matches a k-mer 
# of Text in a fixed window. In Python, the k-mer beginning at position i of Text 
# is denoted Text[i:i+k]. For example, if Text is "GACCATACTG", 
# then Text[4:7] is "ATA". Python uses 0-based indexing, in which the first symbol 
# of the string occurs at position 0 instead of 1; as a result, Text ends at position 
# len(Text)-1, where len(Text) is a built in function telling us the number of symbols 
# in Text.

# We can now use an if statement, shown below, to determine whether Pattern is the same as Text[i:i+k]; if it does, then we increment count.

if Text[i:i+len(Pattern)] == Pattern:
    count = count+1
# --------------------------------------------------------------------------------
# In Python, the indented block

# for i in range(n):
# iterates over all values of i between 0 and n-1, inclusively. (This is called a for loop, and Codecademy will spend more time on it later, but for now we note that the variable i can be anything you like.)

# For example, we could use the following code to print all even numbers between 0 and 100, inclusively.

for number in range(51):
    print(2*number)
# Note again that we used range(51) and not range(50) because range(n) runs from 0 to n - 1.

# --------------------------------------------------------------------------------

# In the window-sliding figure, reproduced below, we slide a 3-mer Pattern along a string Text of length 14. We start sliding the 3-nucleotide window at position 0 and stop sliding at position 11.

# Exercise Break (1 point): What is the final starting position of a substring of Text  that we would consider when sliding a 10-nucleotide window if Text has length 1000?
# 990

# In general, the final k-mer of a string of length n begins at position n-k; for example, the final 3-mer of "GACCATACTG", which has length 10, begins at position 10 - 3 = 7. This observation implies that the window should slide between position 0 and position len(Text)-len(Pattern).

# Thus, to slide our window from position 0 to len(Text)-len(Pattern), we will need a for loop of the form

for i in range(len(Text)-len(Pattern)+1):
    
# We are now ready to use this for loop along with our previous if statement to expand our code for PatternCount().

count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1 
            
# To put everything together, we will put all this code into a function, 
# called PatternCount() (see below). We will see soon that this function 
# will help us return to finding frequent words in the replication origin.

# Roughly stated, a function takes an input and returns an output. 
# Placing code into a function is economical because we can later call 
# this function by name any time we want to find the number of times one 
# string occurs as a substring within another, instead of having to 
# repeat all of the lines of code contained within the function. 
# The keyword def at the beginning of a function signals that we are 
# “defining” a function.

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
# --------------------------------------------------------------------------------

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

# ['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 
# 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 
# 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 
# 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 
# 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
# 'sqrt', 'tan', 'tanh', 'trunc']

# --------------------------------------------------------------------------------

# PatternCount() is just one of many functions that we will encounter in 
# this book. Sometimes, we will ask you to implement these functions in 
# "Code Challenges". We have already done the first exercise for you 
# (i.e., all you need to do is copy the function to the box below). 
# This step is designed to help get you used to the environment.

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

# --------------------------------------------------------------------------------

# Exercise Break (1 point): Copy over your PatternCount() function from the previous step. 
# 
# Then print  the number of times that the string Pattern equal to "TGATCA" occurs in 
# the string Text corresponding to the Vibrio cholerae ori, which is found here.

# Note:  You will need to reuse PatternCount() (and other functions) 
# throughout this chapter. To store these functions, first download 
# a text editor (such as Sublime or VSCode). Then, open your text 
# editor and copy PatternCount() into a file.  When you save the file as 
# "Replication.py", the text editor will detect that your code is 
# written in Python and color it accordingly.

# Copy your PatternCount function from the previous step below this line
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
# Now, we will set Text equal to the oriC of Vibrio cholerae and Pattern equal to "TGATCA"
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
Pattern = "TGATCA"

# Finally, let's print the result of calling PatternCount on Text and Pattern.
print(PatternCount(Text, Pattern))

# --------------------------------------------------------------------------------

# The Frequent Words Problem
# We say that Pattern is a most frequent k-mer in Text if it maximizes 
# PatternCount(Pattern, Text) among all k-mers. You can verify that "ACTAT" 
# is a most frequent 5-mer for Text equal to "ACAACTATGCATACTATCGGGAACTATCCT", 
# and "ATA" is a most frequent 3-mer for Text equal to "CGATATATCCATAG".

# Exercise Break (1 point): Find the most frequent 2-mer of "GATCCAGATCCCCATAC". 
# (You should solve this exercise by hand and type your answer into the field below.)

# CC

# --------------------------------------------------------------------------------

# We now have a rigorously defined computational problem for finding frequent words 
# in the replication origin. We define a computational problem as a specification 
# of input data in addition to a precise specification of output data that will 
# solve the problem.

# Frequent Words Problem: Find the most frequent k-mers in a string.

#  Input: A string Text and an integer k.
#  Output: All most frequent k-mers in Text.

# --------------------------------------------------------------------------------

# To find the most frequent k-mers in a string Text, we would like to create a 
# mapping like the example below for Text equal to "CGATATATCCATAG" and k equal to 3, 
# where we map each k-mer appearing in  Text to its number of occurrences in  Text.  
# We call this structure a frequency map; once we have constructed a frequency map 
# given  Text and k, we will be able to find the most frequent word  by finding 
# the k-mer whose number of occurrences achieves a maximum.

# ATA --> 3
# ATC --> 1
# CAT --> 1
# CCA --> 1
# CGA --> 1
# GAT --> 1
# TAT --> 2
# TCC --> 1
# TAG --> 1

# Fortunately, Python allows us to easily implement a frequency map by providing a 
# built-in data structure called a dictionary.  You can think of a dictionary as 
# a set of keys (first column in the figure above), where each key refers to a value 
# (second column in the figure above). You can learn about dictionaries 
# (and a related structure called a list) in the following exercises.

https://www.codecademy.com/courses/learn-python/lessons/python-lists-and-dictionaries/exercises/introduction-to-lists

my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]

# 1. In the example above, we created a dictionary that holds many types of values.

# 2. The key "fish" has a list, the key "cash" has an int, and the key "luck" has a string.

# 3. Finally, we print the letter "c". When we access a value in the dictionary like 
# my_dict["fish"], we have direct access to that value (which happens to be a list). 
# We can access the item at index 0 in the list stored by the key "fish".


# Add a key to inventory called 'pocket'

# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'

# .sort() the items in the list stored under the 'backpack' key

# Then .remove('dagger') from the list of items stored under the 'backpack' key

# Add 50 to the number stored under the 'gold' key

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

# --------------------------------------------------------------------------------

# Now that we can generate the beginning of a frequency map, it remains to range a 
# sliding window of length k through the text again. For each such k-mer Pattern, 
# we need to increase the current value of freq[Pattern] by 1.

# Code Challenge (Practice): Fill in the missing part of the FrequencyMap() function 
# below so that it computes the frequency map of a given string Text and integer k.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    # your code goes here!
    return freq

# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    # add another for loop here to range over each k-mer Pattern of text and increase freq[Pattern] by 1 each time
    for j in range(n-k+1):
        Pattern = Text[j:j+k]
        freq[Pattern] += 1
    return freq

# --------------------------------------------------------------------------------

# So let us start by generating an empty list, which will eventually hold the most frequent k-mers.

words = []

# Then, we will generate the frequency map for  Text and k.  We can use the FrequencyMap() 
# function that we have just written as a subroutine, or a function that is called within another function.

freq = FrequencyMap(Text, k)

# Speaking of subroutines, to identify the most frequent k-mers in Text, we need to find the maximum value 
# of the Count dictionary. Python has a built-in function called values() that returns a list containing 
# the values of a dictionary, and it also has a built in function max() for finding the maximum value in a list.  
# We can therefore find the maximum value in the frequency map freq as follows:

m = max(freq.values())

# --------------------------------------------------------------------------------
# Finally, it remains to find every key in the frequency map whose corresponding value is equal to the maximum m.  To do so, we will need to range over all keys in freq.  You learned about applying a for loop to a list in Unit 5 of Codecademy.  The same syntax,

# for key in freq:
# ranges over the keys of our dictionary (you don't have to use the word "key", you can use any variable name you like).

# We are now just about ready to solve the Frequent Words Problem.  All that remains is to append any keys to our list words if the key's corresponding value in freq is equal to m.  We leave this to you in the FrequentWords() function below.

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
    return words

Sample Input:

ACGTTGCATGTCGCATGATGCATGAGAGCT
4
Sample Output:

CATG GCAT

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    # your code here
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return words
# Copy your FrequencyMap() function here.
def FrequencyMap(Text, k):
    # your code here.
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for j in range(n-k+1):
        Pattern = Text[j:j+k]
        freq[Pattern] += 1
    return freq

# --------------------------------------------------------------------------------
# Exercise Break (1 point): Apply your solution to the Frequent Words Problem if Text is the ori of Vibrio cholerae (click here to download) and k = 10. What are the most frequent words?

Sample Input:

n/a
Sample Output:

['CTCTTGATCA', 'TCTTGATCAT']

# Copy your FrequentWords function from the previous step below this line

def FrequentWords(Text, k):
    # Initialize an empty list to store the most frequent k-mers
    freq_k_mers = []
    # Call FrequencyMap function to get the frequency of all k-mers in the Text
    freq = FrequencyMap(Text, k)
    # Find the maximum frequency value in the frequency dictionary
    max_value = max(freq.values())
    # Iterate through the dictionary to find k-mers with the highest frequency
    for key in freq:
        if freq[key] == max_value:
            # Add the most frequent k-mers to the list
            freq_k_mers.append(key)
    # Return the list of most frequent k-mers
    return freq_k_mers

# Function to create a frequency dictionary of k-mers in the given Text
def FrequencyMap(Text, k):
    # Initialize an empty dictionary to store k-mer frequencies code here.
    freq = {}
    # Get the length of the input Text
    n = len(Text)
    # First loop: Identify all k-mers and initialize their count to 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k] # Extract substring of length k
        freq[Pattern] = 0 # Initialize frequency count for the pattern
    # Second loop: Count occurrences of each k-mer in the Text
    for j in range(n-k+1):
        Pattern = Text[j:j+k] # Extract substring of length k
        freq[Pattern] += 1 # Increment its frequency count
    # Return the dictionary containing k-mer counts
    return freq

# Now, we will set Text equal to the oriC of Vibrio cholerae and Pattern equal to "TGATCA"
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10

# Finally, let's print the result of calling FrequentWords on Text and Pattern.
print(FrequentWords(Text, k))

# --------------------------------------------------------------------------------
# Frequent words in Vibrio cholerae
# The figure below reveals the most frequent k-mers in the ori region from Vibrio cholerae.

# STOP and Think: Do any of the counts in the figure seem surprisingly large?


# k           |   3   |   4   |   5   |   6    |   7     |   8      |   9       |
# -------------------------------------------------------------------------------
# occurrences |  25   |  11   |   8   |   8    |   5     |   4      |   3       |
# -------------------------------------------------------------------------------
# k-mers      |  tga  | atga  | gatca | tgatca | atgatca | atgatcaa | atgatcaag |
#             |       | tgat  | tgatc |        |         |          | cttgatcat |
#             |       |       |       |        |         |          | tcttgatca |
#             |       |       |       |        |         |          | ctcttgatc |

# For example, the 9-mer "ATGATCAAG" appears three times in the ori region of Vibrio cholerae — is it surprising?

# atcaatgatcaacgtaagcttctaagcATGATCAAGgtgctcacacagtttatccacaac
# ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca
# cggaaagATGATCAAGagaggatgatttcttggccatatcgcaatgaatacttgtgactt
# gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt
# acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga
# tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat
# tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag
# atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt
# tccttaaccctctattttttacggaagaATGATCAAGctgctgctcttgatcatcgtttc

# We highlight a most frequent 9-mer instead of using some other value of k because experiments have revealed that bacterial DnaA boxes are usually 9 nucleotides long. Furthermore, it is very unlikely that a 9-mer would appear three or more times in a randomly generated DNA string of length 500 due to random chance. In fact, there are four different 9-mers repeated three or more times in this region: "ATGATCAAG", "CTTGATCAT", "TCTTGATCA", and "CTCTTGATC".

# The low likelihood of witnessing even one repeated 9-mer in the ori region of Vibrio cholerae leads us to the working hypothesis that one of these four 9-mers may represent a potential DnaA box that, when appearing multiple times in a short region, jump-starts replication. But which one?

# STOP and Think: Is any one of the four most frequent 9-mers in the ori of Vibrio cholerae “more surprising” than the others?





# _______________________________________________________________________________

# 1.4 Some Hidden Messages are more surprising than others

# The reverse complement of a DNA string Pattern is the string formed by taking the complementary nucleotide of each nucleotide in Pattern, then reversing the resulting string. For example, the reverse complement of "AGTCGCATAGT" is "ACTATGCGACT". This leads us to the following computational problem.

# Reverse Complement Problem: Find the reverse complement of a DNA string.

#  Input: A DNA string Pattern.
#  Output: The reverse complement of Pattern.

# --------------------------------------------------------------------------------
# It is easy to find a problem like this daunting, because we need to juggle two separate tasks in our head.  One is reversing the letters of a given string; the other is taking the complementary nucleotide (A to T, C to G , G to C, T to A) at every position of a string.

# To keep multiple tasks separate and allow us to work on one task at a time, we will employ top-down programming, in which we start at the highest level of our program and divide the work into subsequently smaller pieces.  For example, we would love for our "highest-level" function to look like this.

# def ReverseComplement(Pattern):
#     Pattern = Reverse(Pattern) # reverse all letters in a string
#     Pattern = Complement(Pattern) # complement each letter in a string
#     return Pattern
# Now that we have designed our program top-down, we can focus our energy on two separate, simpler tasks: writing Reverse() and Complement().

# (Note: You may be hesitant about the notation x = f(x).  When we pass x to a function f, a copy of x is produced and used as the parameter of f.  So even if the function changes this copy, it won't change the original copy of x.)

# --------------------------------------------------------------------------------
# First, we will tackle Reverse().  We can range over each character char of a string Pattern (from beginning to end) using the notation

# for char in Pattern:
# Code Challenge (2 Points): Write a function Reverse() that takes a string Pattern and returns a string formed by reversing all the letters of Pattern.  Recall that for strings x, y, and z, the notation z=x+y concatenates x and y together and stores the result in the variable z.

# Hint: We can begin with an empty string rev and then successively place each character of Pattern at the beginning of this string.  For example, if we were taking the reverse of ACGT, then rev would grow as follows.

# A
# CA
# GCA
# TGCA
# Sample Input:

# AAAACCCGGT
# Sample Output:

# TGGCCCAAAA

# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev

# --------------------------------------------------------------------------------

# Next, we will handle Complement().  We can use the syntax introduced on the previous step for ranging through the characters in a string, and we can use the same approach to return a string by building it up from an empty string.

# This time, we simply need to check the value of the current character and add its complement to the growing string.

# Code Challenge (2 Points): Write a function Complement() that takes as input a DNA string Pattern and returns a string formed by taking the complement of each letter of Pattern (don't reverse the string yet).

# Sample Input:

# AAAACCCGGT
# Sample Output:

# TTTTGGGCCA

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    # Initialize an empty string to store the complementary DNA sequence
    string = ""
    # Create a dictionary mapping each nucleotide to its complement
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Iterate through each character in the input DNA sequence
    for char in Pattern:
        # Append the complementary nucleotide to the result string
        string += complement_dict[char]
    # Return the complementary DNA sequence
    return string

# --------------------------------------------------------------------------------
# Code Challenge (2 points): Write a function ReverseComplement() to solve the Reverse Complement Problem, which is reproduced below. (Remember that we have already given you this code at the beginning of the module.) Then add ReverseComplement() (and its needed subroutines) to Replication.py.

# Reverse Complement Problem: Find the reverse complement of a DNA string.

#  Input: A DNA string Pattern.
#  Output: The reverse complement of Pattern.
# Click here for this problem's test datasets.

# Sample Input:

# AAAACCCGGT
# Sample Output:

# ACCGGGTTTT

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    rev = ""
    for char in Pattern:
        rev = char + rev
    # print (rev)
    return rev

# Copy your Complement() function here.
def Complement(Pattern):
    # your code here
    # Initialize an empty string to store the complementary DNA sequence
    string = ""
    # Create a dictionary mapping each nucleotide to its complement
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Iterate through each character in the input DNA sequence
    for char in Pattern:
        # Append the complementary nucleotide to the result string
        string += complement_dict[char]
    # Return the complementary DNA sequence
    return string

ReverseComplement("AAAACCCGGT")

# --------------------------------------------------------------------------------
# Interestingly, among the four most frequent 9-mers in the ori region of Vibrio cholerae, 
# "ATGATCAAG" and "CTTGATCAT" are reverse complements of each other, 
# resulting in the following six occurrences of these strings.

# atcaatgatcaacgtaagcttctaagcATGATCAAGgtgctcacacagtttatccacaac 
# ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca 
# cggaaagATGATCAAGagaggatgatttcttggccatatcgcaatgaatacttgtgactt 
# gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt 
# acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga 
# tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat 
# tgataatgaatttacatgcttccgcgacgatttacctCTTGATCATcgatccgattgaag 
# atcttcaattgttaattctcttgcctcgactcatagccatgatgagctCTTGATCATgtt 
# tccttaaccctctattttttacggaagaATGATCAAGctgctgctCTTGATCATcgtttc

# Finding a 9-mer that appears six or more times 
# (either as itself or as its reverse complement) in a DNA string of length 500 
# is far more surprising than finding a 9-mer that appears three or more times alone. 
# This statistical evidence leads us to the working hypothesis that "ATGATCAAG" and 
# its reverse complement "CTTGATCAT" indeed represent DnaA boxes in Vibrio cholerae. 
# Our computational conclusion makes sense biologically because the DnaA protein that 
# binds to DnaA boxes and initiates replication does not care which of the two strands 
# it binds to. For our purposes, both "ATGATCAAG" and "CTTGATCAT" represent DnaA boxes.

# --------------------------------------------------------------------------------

# Function to find all starting positions where Pattern occurs in Genome
def PatternMatching(Pattern, Genome):
    positions = [] # empty list to store the starting positions of matches
    
    # append each starting position of the pattern to it when we encounter a match
    
    # loop through Genome with a sliding window of length equal to Pattern
    # range goes from 0 up to (len(Genome) - len(Pattern) + 1)
    # so we don’t run past the end of the Genome
    for i in range(len(Genome)-len(Pattern)+1):
        
        # extract the substring of Genome starting at i with length of Pattern
        window = Genome[i:i+len(Pattern)]
        
        # if this substring matches Pattern exactly
        if window == Pattern:
            
            # save the starting position (i) in the list
            positions.append(i)

    # return the list of all positions where Pattern was found            
    return positions

# Example input
Genome = "GATATATGCATATACTT"
Pattern = "ATAT"

# Finally, let's print the result of calling PatternMatching on Genome and Pattern.
print (PatternMatching(Pattern, Genome))

# --------------------------------------------------------------------------------

# Exercise Break (1 point): 
# 
# Apply your solution to the Pattern Matching Problem to find all starting positions of "CTTGATCAT" 
# in the Vibrio cholerae genome. (Give the positions in increasing order.)

# The genome will be automatically read below, but in the event that you want to play with 
# the Vibrio cholerae genome on your own computer, you can download the genome here.

# Copy your PatternMatching function below this line.
# Function to find all starting positions where Pattern occurs in Genome
def PatternMatching(Pattern, Genome):
    positions = [] # empty list to store the starting positions of matches
    
    # append each starting position of the pattern to it when we encounter a match
    
    # loop through Genome with a sliding window of length equal to Pattern
    # range goes from 0 up to (len(Genome) - len(Pattern) + 1)
    # so we don’t run past the end of the Genome
    for i in range(len(Genome)-len(Pattern)+1):
        
        # extract the substring of Genome starting at i with length of Pattern
        window = Genome[i:i+len(Pattern)]
        
        # if this substring matches Pattern exactly
        if window == Pattern:
            
            # save the starting position (i) in the list
            positions.append(i)

    # return the list of all positions where Pattern was found            
    return positions

# Behind the scenes, we read in Genome equal to the genome of V. cholerae.

# Set Pattern equal to "CTTGATCAT"
Pattern = "CTTGATCAT"

with open("Vibrio_cholerae.txt", "r") as file:
    Genome = file.read().replace("\n", "")

# Call PatternMatching on Pattern and Genome, and store the output as a variable called positions

# print the positions variable
result = PatternMatching(Pattern, Genome)
print (result)

print (len(result))
# --------------------------------------------------------------------------------

# After solving the Pattern Matching Problem, we discover that "ATGATCAAG" 
# appears 17 times in the following positions of the Vibrio cholerae genome:

# 116556, 149355, 151913, 152013, 152394, 186189, 194276, 200076, 224527,
# 307692, 479770, 610980, 653338, 679985, 768828, 878903, 985368

# With the exception of the three occurrences of "ATGATCAAG" in ori at starting 
# positions 151913, 152013, and 152394, no other instances of "ATGATCAAG" 
# form “clumps”, i.e., appear close to each other in a small region of the genome. 
# The preceding exercise verifies that the same conclusion is reached when 
# searching for "CTTGATCAT". We now have strong statistical evidence that 
# "ATGATCAAG"/"CTTGATCAT" may represent the hidden message to DnaA to start replication.

# STOP and Think: Is it safe to conclude that "ATGATCAAG"/"CTTGATCAT" also 
# represents a DnaA box in other bacterial genomes?

# _______________________________________________________________________________



# 1.5 An Explosion of Hidden Messages
# Looking for hidden messages in multiple genomes
# We should not jump to the conclusion that "ATGATCAAG"/"CTTGATCAT" is a hidden message 
# for all bacterial genomes without first checking whether it even appears in known 
# ori regions from other bacteria. After all, maybe the clumping effect of 
# "ATGATCAAG"/"CTTGATCAT" in the ori region of Vibrio cholerae is simply a 
# statistical fluke that has nothing to do with replication. Or maybe different 
# bacteria have different DnaA boxes . . .

# --------------------------------------------------------------------------------

# Let’s check the proposed ori region of Thermotoga petrophila, a bacterium that 
# thrives in extremely hot environments; its name derives from its discovery 
# in the water beneath oil reservoirs, where temperatures can exceed 80℃ Celsius.


# Exercise Break (1 point): How many combined occurrences of "ATGATCAAG" and "CTTGATCAT" 
# can you find in this region? (Click here to download the region.)

# Copy your PatternCount function below here
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# On the following line, let's create a variable called Text that is equal to the oriC region from T petrophila
Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"


# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.
count_1 = PatternCount(Text, "ATGATCAAG")


# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text. 
count_2 = PatternCount(Text, "CTTGATCAT")

# Finally, print the sum of count_1 and count_2
print (count_1 + count_2)

# Passed test #3. Correct! "ATGATCAAG" occurs 0 times, and "CTTGATCAT" occurs 0 times

# --------------------------------------------------------------------------------

# This region does not contain a single occurrence of "ATGATCAAG" or "CTTGATCAT"! Thus, different bacteria may use different DnaA boxes as “hidden messages” to the DnaA protein.

# Application of the Frequent Words Problem to the ori region above:

# Function to create a dictionary with counts of all k-mers in the given Text
def FrequencyMap(Text, k):
    """Create a dictionary with counts of all k-mers in Text."""
    # Initialize empty dictionary to store k-mer counts
    freq = {}
    # Get the length of the input Text
    n = len(Text)
    # Slide a window of length k over the text
    for i in range(n - k + 1):
        Pattern = Text[i:i+k] # Extract the current k-mer
        if Pattern in freq: # If k-mer already in dictionary
            freq[Pattern] += 1 # Increment its count
        else: # If k-mer is new
            freq[Pattern] = 1 # Initialize its count to 1
    # Return the dictionary containing k-mer counts
    return freq

# Function to return all k-mers that occur at least a certain number of times
def FrequentWords(Text, k, min_count):
    """Return all k-mers that occur the min number of times."""
    freq = FrequencyMap(Text, k) # Get the dictionary of k-mer counts
    # Filter k-mers meeting min_count
    frequent_kmers = [] # initialize empty list
    for key, count in freq.items(): # iterate over all k-mers and their counts
        if count >= min_count: # check if k-mer occurs at least min_count times
            frequent_kmers.append(key) # Add k-mer to the list if it meets the threshold
    return frequent_kmers # Return the filtered list of k-mers

# Load the ori sequence from a text file and remove newline characters
Text = open("Thermotoga_petrophila_ori.txt", "r").read().replace("\n", "")
k = 9 # Set the length of k-mers we want to analyze
min_count = 3 # Set the minimum count threshold

# Print the list of all k-mers that appear at least min_count times
print(FrequentWords(Text, k))


# reveals that the following six 9-mers appear in this region three or more 
# times:

# "AACCTACCA"  "AAACCTACC"  "ACCTACCAC"
# "CCTACCACC"  "GGTAGGTTT"  "TGGTAGGTT"

# Something peculiar must be happening because it is extremely unlikely that 
# six different 9-mers will occur so frequently within the same short region 
# in a random string. We will cheat a little and consult with Ori-Finder, 
# a software tool for finding replication origins in DNA sequences. 
# This software chooses "CCTACCACC" (along with its reverse complement "GGTGGTAGG") 
# as a working hypothesis for the DnaA box in Thermotoga petrophila. Together, 
# these two complementary 9-mers appear five times in the replication origin:

def ReverseComplement(Pattern):
    # Reverse the sequence first, then take its complement
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

def Reverse(Pattern):
    # Create a reversed version of the string
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev

def Complement(Pattern):
    # Initialize an empty string to store the complementary DNA sequence
    string = ""
    # Create a dictionary mapping each nucleotide to its complement
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Iterate through each character in the input DNA sequence
    for char in Pattern:
        # Append the complementary nucleotide to the result string
        string += complement_dict[char]
    # Return the complementary DNA sequence
    return string

def FrequencyMap(Text, k):
    """Create a dictionary with counts of all k-mers in Text."""
    # Initialize empty dictionary to store k-mer counts
    freq = {}
    # Slide a window of length k over the text
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k] # Extract the current k-mer
        if Pattern in freq:
            freq[Pattern] += 1  # increment count if k-mer already exists
        else:
            freq[Pattern] = 1   # initialize count to 1
    return freq

def OriFinder(Text, k, min_count=3):
    # Find k-mers that appear at least min_count times and their reverse complements
    freq = FrequencyMap(Text, k)
    candidates = []
    
    for kmer, count in freq.items():
        if count >= min_count: # Only keep k-mers that appear enough times
            rev_comp = ReverseComplement(kmer) # Get reverse complement
            rev_count = freq.get(rev_comp, 0) # Count of reverse complement
            combined = count + rev_count # Total occurrences
            # define canonical orientation
            candidates.append([kmer, rev_comp, count, rev_count, combined])
    return candidates

# Read the DNA sequence from a file and remove line breaks
Text = open("Thermotoga_petrophila_ori.txt", "r").read()
k = 9

# Get all candidate DnaA boxes and print counts
candidates = OriFinder(Text, k)
for kmer, rev_comp, count, rev_count, combined in candidates:
    print(f"{kmer} ({count}) - {rev_comp} ({rev_count}) > combined: {combined}")
    
    
# ----------------------------------------------------------------------------------
# The Clump Finding Problem
# Now imagine that you are trying to find ori in a newly sequenced bacterial genome. 
# Searching for “clumps” of "ATGATCAAG"/"CTTGATCAT" or "CCTACCACC"/"GGTGGTAGG" is 
# unlikely to help, since this new genome may use a completely different hidden 
# message! Before we lose all hope, let’s change our computational focus: instead 
# of finding clumps of a specific k-mer, let’s try to find every k-mer that forms 
# a clump in the genome. Hopefully, the locations of these clumps will shed light 
# on the location of ori.

# Our plan is to slide a window of fixed length L along the genome, looking for a 
# region where a k-mer appears several times in short succession. The parameter 
# value L = 500 reflects the typical length of ori in bacterial genomes.

# We think of a k-mer as a “clump” if it appears many times within a short interval 
# of the genome. More formally, given integers L and t, a k-mer Pattern forms an 
# (L, t)-clump inside a (longer) string Genome if there is a substring of Genome 
# of length L in which this k-mer appears at least t times. (This definition 
# assumes that the k-mer completely fits within the interval.) For example, 
# "TGCA" forms a (25, 3)-clump in the following Genome:

# "gatcagcataagggtccCTGCAATGCATGACAAGCCTGCAGTtgttttac"

# ----------------------------------------------------------------------------------

# From our previous examples of ori regions, "ATGATCAAG" forms a (500, 3)-clump in 
# the Vibrio cholerae genome, and "CCTACCACC" forms a (500, 3)-clump in the 
# Thermotoga petrophila genome. We are now ready to formulate the following problem.

# Clump Finding Problem: Find patterns forming clumps in a string.

#  Input: A string Genome, and integers k, L, and t.
#  Output: All distinct k-mers forming (L, t)-clumps in Genome.
# Don’t worry about writing an algorithm to solve the Clump Finding Problem; 
# we have done it for you. When we used this algorithm to look for clumps in 
# the Escherichia coli (E. coli) genome, the workhorse of bacterial genomics, 
# we found hundreds of different 9-mers forming (500, 3)-clumps in this genome. 
# It is absolutely unclear which of these 9-mers might represent a DnaA box in 
# the bacterium’s ori region.

# STOP and Think: Should we give up? If not, what would you do now?

# At this point, an unseasoned researcher might give up, since it appears that we 
# do not have enough information to locate ori in E. coli. But a fearless veteran 
# bioinformatician would try to learn more about the details of replication in the 
# hope that they provide new algorithmic insights into finding ori.

# _______________________________________________________________________________
# 1.6 Detour: The Most Beautiful Experiment in Biology

# The Meselson-Stahl experiment, conducted in 1958 by Matthew Meselson and 
# Franklin Stahl, is sometimes called "the most beautiful experiment in biology". 
# In the late 1950s, biologists debated three conflicting models of DNA replication, 
# illustrated in the figure below. The semiconservative hypothesis suggested that 
# each parent strand acts as a template for the synthesis of a daughter strand. 
# As a result, each of the two daughter molecules contains one parent strand and 
# one newly synthesized strand. The conservative hypothesis proposed that the 
# entire double-stranded parent DNA molecule serves as a template for the synthesis 
# of a new daughter molecule, resulting in one molecule with two parent strands 
# and another with two newly synthesized strands. The dispersive hypothesis 
# proposed that some mechanism breaks the DNA backbone into pieces and splices 
# intervals of synthesized DNA, so that each of the daughter molecules is a 
# patchwork of old and new double-stranded DNA.

# The three models are illustrated below, with parent DNA colored yellow and 
# newly synthesized DNA colored black.

# see image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "replication_models_one_round_1.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# --------------------------------------------------------------------------------
# Meselson and Stahl's insight relied on the fact that one isotope of nitrogen, 
# Nitrogen-14 (14N), is lighter and more abundant than Nitrogen-15 (15N). 
# Knowing that the DNA molecular structure naturally contains 14N , Meselson 
# and Stahl grew E. coli for many rounds of replication in a 15N medium, 
# which caused the bacteria to gain weight as they absorbed the heavier isotope 
# into their DNA.

# When they were confident that the bacterial DNA was saturated with 15N, 
# they transferred these heavy E. coli cells to a less dense 14N medium.

# STOP and Think: What do you think happened when the “heavy” E. coli replicated 
# in the “light” 14N medium?

# ---------------------------------------------------------------------------------
# The brilliance of the Meselson-Stahl experiment is that all newly synthesized 
# DNA would contain exclusively 14N, and the three existing hypotheses for DNA 
# replication predicted different outcomes for how this 14N isotope would be 
# incorporated into DNA. Specifically, after one round of replication, the 
# conservative model predicted that half the E. coli DNA would still have only 
# 15N and therefore be heavier, whereas the other half would have only 14N and 
# be lighter. Yet when they attempted to separate the E. coli DNA according to 
# weight by using a centrifuge after one round of replication, all of the DNA had 
# the same density! Just like that, they had refuted the conservative hypothesis 
# once and for all.

# Figure
# see image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "replication_models_one_round_1.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()
 

# Unfortunately, this experiment was not able to eliminate either of the other two 
# models, as you can see that both the dispersive and semiconservative hypotheses 
# predicted that all of the DNA after one round of replication would have the 
# same density.

# STOP and Think: What would the dispersive and semiconservative models predict 
# about the density of E. coli DNA after two rounds of replication?

# ---------------------------------------------------------------------------------
# Let’s first consider the dispersive model, which says that each daughter strand 
# of DNA is formed by half mashed up pieces of the parent strand, and half new DNA. 
# If this hypothesis were true, then after two replication cycles, any daughter 
# strand of DNA should contain about 25% 15N and about 75% 14N. In other words, 
# all the DNA should still have the same density. And yet when Meselson and Stahl 
# spun the centrifuge after two rounds of E. coli replication, this is not what 
# they observed!

# Instead, they found that the DNA divided into two different densities. 
# This is exactly what the semiconservative model predicted: after one cycle, 
# every cell should possess one 14N strand and one 15N strand; after two cycles, 
# half of the DNA molecules should have one 14N strand and one 15N strand, 
# while the other half should have two 14N strands, producing the two different 
# densities they noticed.

# Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "replication_models_2.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# STOP and Think: 
# What does the semi-conservative model predict about the density of E. coli DNA 
# after three rounds of replication?

# ---------------------------------------------------------------------------------
# Meselson and Stahl had rejected the conservative and dispersive hypotheses of 
# replication, and yet they wanted to make sure that the semiconservative 
# hypothesis was confirmed by further E. coli replication. This model predicted 
# that after three rounds of replication, one-quarter of the DNA molecules 
# should still have a 15N strand, causing 25% of the DNA to have an intermediate 
# density, whereas the remaining 75% should be lighter, having only 14N. 
# This is indeed what Meselson and Stahl witnessed in the lab, and the 
# semiconservative hypothesis has stood strong to this day.

# And if you don't want to take our word for it, why not hear about this beautiful 
# experiment from Meselson and Stahl themselves!

# https://www.youtube.com/watch?v=7-tnuAqEp9g

# _______________________________________________________________________________
# 1.7 Detour: Directionality of DNA Strands

# The sugar component of a nucleotide has a ring of five carbon atoms, 
# which are labeled as 1’, 2’, 3’, 4’, and 5’ in the figure on the right. 
# The 5’ atom is joined onto the phosphate group in the nucleotide and 
# eventually to the 3’ end of the neighboring nucleotide. The 3’ atom is 
# joined onto another neighboring nucleotide in the nucleic acid chain. 
# As a result, we call the two ends of the nucleotide the 5’-end and the 
# 3’-end (pronounced “five prime end” and ”three prime end”, respectively).

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "nucleotide_4.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()

# When we zoom out to the level of the double helix, we can see in the figure 
# below that any DNA fragment is oriented with a 3’ atom on one end and a 5’ 
# atom on the other end. As a standard, a DNA strand is always read in the 5' → 3' 
# direction. Note that the orientations run opposite to each other in 
# complementary strands.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_path = "directionality_4.png"
image = mpimg.imread(image_path)
plt.imshow(image)
plt.axis("off")  # hides x and y axes
plt.show()