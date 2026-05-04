def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

# Now that we have designed our program top-down, we can focus our energy on two separate, simpler tasks: 
# writing Reverse() and Complement().

# (Note: You may be hesitant about the notation x = f(x).  
# When we pass x to a function f, a copy of x is produced and used as the parameter of f.  
# So even if the function changes this copy, it won't change the original copy of x.)

# First, we will tackle Reverse().
# We can range over each character char of a string Pattern (from beginning to end) using the notation

for char in Pattern:
    
# Code Challenge (2 Points): 
# Write a function Reverse() that takes a string Pattern and returns a 
# string formed by reversing all the letters of Pattern.  Recall that for strings x, y, and z, 
# the notation z=x+y concatenates x and y together and stores the result in the variable z.

# Hint: We can begin with an empty string rev and then successively place each character 
# of Pattern at the beginning of this string.
# For example, if we were taking the reverse of ACGT, then rev would grow as follows.

# rev = ""
# rev = "A"
# rev = "CA"
# rev = "GCA"
# rev = "TGCA"

# Input:  A string Pattern
# Output: The reverse of Pattern

def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev

print(Reverse("ACGT"))

# Another way
# def Reverse(Pattern):
#     return Pattern[::-1]

# print(Reverse("ACGT"))

# Next, we will handle Complement().
# We can use the syntax introduced on the previous step for ranging through 
# the characters in a string, and we can use the same approach to return 
# a string by building it up from an empty string.

# This time, we simply need to check the value of the current character and add its complement to the growing string.

# Code Challenge (2 Points): 
# Write a function Complement() that takes as input a DNA string Pattern and 
# returns a string formed by taking the complement of each letter of Pattern 
# (don't reverse the string yet).

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).

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

print(Complement("AAAACCCGGT"))


# Code Challenge (2 points): 
# Write a function ReverseComplement() to solve the Reverse Complement Problem, 
# which is reproduced below. 
# (Remember that we have already given you this code at the beginning of the module.) 
# Then add ReverseComplement() (and its needed subroutines) to Replication.py.

# Reverse Complement Problem: Find the reverse complement of a DNA string.

# Input: A DNA string Pattern.
# Output: The reverse complement of Pattern.
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

print(ReverseComplement("AAAACCCGGT"))