#  Problem 1
# 10.0 points possible (graded)

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

vowels=['a', 'e', 'i', 'o', 'u']
holder=0
for i in s:
    if i in vowels:
        holder+=1
print('Number of vowels: %d'%(holder))
