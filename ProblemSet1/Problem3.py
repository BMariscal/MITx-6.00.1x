#  Problem 3
# 15.0 points possible (graded)

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.


longest=s[0]
new_longest=s[0]
for i in range(1,len(s),1):
    if (s[i] >= longest[-1]):
        longest += s[i]
        if len(longest) > len(new_longest):
            new_longest = longest
    else:
        longest = s[i]

print('Longest substring in alphabetical order is: {}'.format(new_longest))


        