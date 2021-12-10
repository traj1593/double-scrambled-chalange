'''
Program: Double Scramble challenge
Filename: doubleScrambleChallenge-tRaj-00.py
Author: Tushar Raj
Revisions: No revisions made
Description:
    Double Scrambled Words
    The variable z contains four encoded common English words.
    Each word is 5 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions where possible.
    *** Note that unlike the previous problem, each item in z is a list.
        Each list has an integer that encodes the position in a different
        location in the list.  The characters are in the correct order but
        you will need to rotate each list so the integers are in the same
        location in each list.  The most convenient location would be at
        index zero because then, you would not need to provide a sort key.
    Example: rotate z[0] so it looks like this: [3, 't', 'n','s', 'a']
'''
print("Double Scramble challenge\n\n")

z = [['s', 'a', 3, 't', 'n'],['h', 'b', 'c', 1, 'p'],
     ['h', 'y', 'c', 'k', 5],[4, 'c', 'e', 'i', 'l'],
     ['o', 'a', 'h', 2, 'i']]

# Step 1:   Rotate each list in z so the integer is in the zero position
#           without changing the order of the characters.

def rotate(lst):
    if(type(lst[0])==int): #checking if the first letter in nested list is int type or not
        return lst
    l=[i for i in lst if(isinstance(i,int))] #find the int type data in list
    n=lst.index(l[0]) #find the index of the int type
    return lst[n:] + lst[:n] #roate the list by index position
t=[rotate(i) for i in z]

# Step 2:   Sort the lists based on the integer value in each.

t.sort(key=lambda a:a[0])

# Step 3:   Use a list comprehension to create a list of characters
#           for each word.

a=[[j[i] for j in t] for i in range(len(t[1])) if(i !=0)]

# Stpe 4:   Use the join() method to create a string for each of the
#           four words and print them.

v=list(map("".join,a))
[print(i,end=" ") for i in v]


print("\n\n\n***Double Scramble challenge Ended***")
