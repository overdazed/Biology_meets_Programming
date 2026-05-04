# empty dictionary
freq = {}

# Next, we will range through the text and assign every pattern a value of 0.  
# We already know how to range through every k-mer in a string from our work 
# with  PatternCount() in a previous module.  

n = len(Text)
for i in range(n-k+1):
    Pattern = Text[i:i+k]
    freq[Pattern] = 0
    
#(Note that this code may assign the same key more than once, which is fine.)  
# The code below is therefore the start of our FrequencyMap() function.

def FrequencyMap(Text, k):
    # Initialize an empty dictionary to store substring frequencies
    freq = {}
    
    # Get the length of the given text
    n = len(Text)
    
    # Loop through the text, extracting substrings of length k
    for i in range(n-k+1):
        # Get the substring (pattern) starting at index i with length k
        Pattern = Text[i:i+k]
        
        # Add the pattern as a key to the dictionary and initialize its value to 0
        # However, this code does not actually count occurrences, just initializes them
        freq[Pattern] = 0
    # Return the dictionary containing the initialized substring frequencies
    return freq

# Now that we can generate the beginning of a frequency map, 
# it remains to range a sliding window of length k through the text again. 
# For each such k-mer Pattern, we need to increase the current value of freq[Pattern] by 1.

# Code Challenge (Practice): 
# Fill in the missing part of the FrequencyMap() function below so that it computes 
# the frequency map of a given string Text and integer k.

with open("../vibrio_cholerae.txt", "r") as file:
    Text = file.read().upper()

# This function takes a string (Text) and an integer (k), 
# where k represents the length of substrings (patterns) that will be analyzed.
def FrequencyMap(Text, k):
    # Initialize an empty dictionary freq to store substrings of length k and their frequency counts.
    freq = {}
    # Determines the length of Text.
    n = len(Text)
    
    # First Loop (Initializes Dictionary Keys):
    for i in range(n-k+1):
        # Iterates through Text and extracts all possible substrings (Pattern) of length k.
        Pattern = Text[i:i+k]
        # Each substring is added as a key in freq, and its value is initialized to 0.
        #This ensures all patterns appear in the dictionary before counting occurs.
        freq[Pattern] = 0
    # Second Loop (Counts Occurrences):
    for j in range(n-k+1):
        # Iterates through Text again, extracting the same substrings.
        Pattern = Text[j:j+k]
        # Instead of initializing them, it increments their count in freq, 
        # effectively counting how many times each substring appears in Text.
        freq[Pattern] += 1
    # Return the dictionary containing the frequency of each substring.
    return freq

# print(FrequencyMap(Text, 8))

# The function processes "CGATATATCCATAG" to extract all substrings of length 3 and 
# count their occurrences.
print(FrequencyMap("CGATATATCCATAG", 3))
# The result is a dictionary where keys represent 3-letter substrings from Text, 
# and values indicate how many times each substring appears.