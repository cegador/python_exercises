# Ask the user for a string and print  out whether this string is a  palindrome or not. A palindrome is  a string that reads the same forwards and backwards.

# print('Write a word and find out if it is a palindrome')
word = input('Write a word and find out if it is a palindrome ')

l_word = []

for i in word:
  l_word.append(i)

back_word = l_word[::-1]
palindrome = ''.join(back_word)

if(word == palindrome):
  print('{} is a palindrome'.format(word))
else:
  print('{} is  not a palindrome'.format(word))