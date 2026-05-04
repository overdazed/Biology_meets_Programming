# Copy over your PatternCount() function from the previous step.  
# Then print  the number of times that the string Pattern equal to 
# "TGATCA" occurs in the string Text corresponding to 
# the Vibrio cholerae ori, which is found here.

# Note:  You will need to reuse PatternCount() (and other functions) throughout this chapter. 
# To store these functions, first download a text editor (such as Sublime or VSCode). 
# Then, open your text editor and copy PatternCount() into a file.  
# When you save the file as "Replication.py", the text editor will detect that your code is written in Python and color it accordingly.

# Copy your PatternCount function from the previous step below this line
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Now, we will set Text equal to the oriC of Vibrio cholerae and Pattern equal to "TGATCA"
with open("../vibrio_cholerae.txt", "r") as file:
    Text = file.read().upper()

Pattern = "TGATCA"

print(PatternCount(Text, Pattern))