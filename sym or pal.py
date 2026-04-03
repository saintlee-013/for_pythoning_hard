#A string is symmetrical if its first half matches the second half, considering the middle character for odd-length strings.
#A string is palindrome if it reads the same forward and backward.
print("Enter word to check if the word is symmetrical or a palindrome")
word = input()
i = 0
chars = []
print(f"word is {word}")
for x in word:
 print(x, end = ' ')
 chars = chars + [x]
 i = i+1
print()
print(f"The number of letter in the word is {i}")
for char in chars:
 print(char)
""" for the symmetrical part first, we must have two cases, one where there is an odd number of letters in the word and one where there is an even
a word can be symmetrical even with an even number of letters, but can't be a palindorme and it is my duty to mention why it is or isn't """
""" murmur = 012345 -> 0 == 3, 1==4, 2==5 and there are 6 letters, so it splits at half = 3 but 3-1 so half-1=2  """
half = i//2 
j = 1
while j < (half +1):
 if(chars[(half - j)] == chars[(i-j)]):
  j = j + 1
 else:
  print("Word is not symmetrical!")
  break
if (j == (half+1)):
 print("word is symmetrical!")
"""now for palindrome! 0==5, 1==4, 2==3 for hannah"""
k = 0
l = 1
while (k<=(half-1)):
 if(chars[k]==chars[i-l]):
  k = k+1
  l = l+1
 else:
  print("Word is not a palindrome!")
  break
if((k+l)>(i-1)):
 print("Word is a palindrome!")
