# Now that we have a function to generate a frequency map from a given string and integer, 
# we need to find the maximum value in this map and return all keys that achieve the maximum; 
# this will represent a function FrequentWords(Text, k) to solve the Frequent Words Problem.

# For example, given Text equal to "CGATATATCGAT" and k equal to 3, 
# we have the following frequency map, and we would like to return a list containing all keys 
# of this dictionary achieving the maximum value of 2 
# (lists were introduced in the preceding Python Practice).

with open("../vibrio_cholerae.txt", "r") as file:
    Text = file.read().upper()

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for j in range(n-k+1):
        Pattern = Text[j:j+k]
        freq[Pattern] += 1
    return freq

# print(FrequencyMap(Text, 8))
print(FrequencyMap("CGATATATCGAT", 3))


# return a list containing all keys of this dictionary achieving the maximum value of 2
# So, let us start by generating an empty list, which will eventually hold the most frequent k-mers.
freq_k_mers = []

# Then, we will generate the frequency map for  Text and k.  We can use the FrequencyMap() function that we have just written as a subroutine, or a function that is called within another function.
freq = FrequencyMap("CGATATATCGAT", 3)

# Speaking of subroutines, to identify the most frequent k-mers in Text, 
# we need to find the maximum value of the Count dictionary. 
# Python has a built-in function called values() that returns a 
# list containing the values of a dictionary, 
# and it also has a built in function max() for finding the maximum value in a list.  
# We can therefore find the maximum value in the frequency map freq as follows:
max_value = max(freq.values())

# Finally, it remains to find every key in the frequency map whose corresponding value 
# is equal to the maximum max_value.  To do so, we will need to range over all keys in freq.

# ranges over the keys of our dictionary.
for key in freq:
    
# We are now just about ready to solve the Frequent Words Problem.  
# All that remains is to append any keys to our list freq_k_mers 
# if the key's corresponding value in freq is equal to max_value.

# Input: A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
# Function to find the most frequent k-mers (substrings of length k) in a given text

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

# Call the function with a sample DNA sequence and k=4
# print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))

# Exercise Break (1 point): 
# Apply your solution to the Frequent Words Problem if Text is the ori of Vibrio cholerae 
# (click here to download) and k = 10. What are the most frequent words?

with open("../vibrio_cholerae.txt", "r") as file:
    Text = file.read().upper()

print(FrequentWords(Text, 9))