# https://cogniterra.org/lesson/30256/step/7?unit=22332

# Before looking for frequent words, 
# we would like to compute PatternCount(Pattern, Text). 
# Because this is your first biological algorithm, 
# we will walk you through the details. 
# To do so, we first create an integer variable count that we set equal to zero:
# count = 0

# As illustrated in the figure below, our plan is to “slide a window” down Text, 
# checking whether each k-mer substring of Text matches Pattern. 
# If it does, then we add 1 to count (adding 1 to a variable is called incrementing it). 
# The value of count after we have slid the window to the end of Text will be equal 
# to PatternCount(Pattern, Text). The question, then, is how to convert the idea in 
# the figure into a working program. Doing so will require a little more knowledge of Python.


#We can now use an if statement, shown below, to determine whether Pattern is the same as Text[i:i+k]; 
# if it does, then we increment count.

# if Text[i:i+len(Pattern)] == Pattern:
#     count = count+1

# In Python, the indented block

# for i in range(n):

# iterates over all values of i between 0 and n-1, inclusively. 
# (This is called a for loop, and Codecademy will spend more time on it later, 
# but for now we note that the variable i can be anything you like.)

# For example, we could use the following code to print all even numbers between 0 and 100, inclusively.

# for number in range(51):
#     print(2*number)
    
# Note again that we used range(51) and not range(50) because range(n) runs from 0 to n - 1.

# In general, the final k-mer of a string of length n begins at position n-k; for example, 
# the final 3-mer of "GACCATACTG", which has length 10, begins at position 10 - 3 = 7. 
# This observation implies that the window should slide between position 0 and 
# position len(Text)-len(Pattern).

# Thus, to slide our window from position 0 to len(Text)-len(Pattern), 
# we will need a for loop of the form

# for i in range(len(Text)-len(Pattern)+1):
    
# We are now ready to use this for loop along with our previous if statement to 
# expand our code for PatternCount().

# for i in range(len(Text)-len(Pattern)+1):
#     if Text[i:i+len(Pattern)] == Pattern:
#         count = count+1
        
# To put everything together, we will put all this code into a function, 
# called PatternCount() (see below). 
# We will see soon that this function will help us return to finding 
# frequent words in the replication origin.

# Roughly stated, a function takes an input and returns an output. 
# Placing code into a function is economical because we can later call 
# this function by name any time we want to find the number of times 
# one string occurs as a substring within another, instead of having 
# to repeat all of the lines of code contained within the function. 
# The keyword def at the beginning of a function signals that we are “defining” a function.

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print(PatternCount("GCGCG", "GCG"))

