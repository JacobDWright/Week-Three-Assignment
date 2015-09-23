#Jacob Wright
#Simple Pig Latin
#Week Three Assignment

#prompt the user to input an English word
word = input("Type in a word in English to be translated into Pig Latin ")

vowel = "aeiou"

#translate and print the word into Pig Latin
if word[0] in vowel:
  print(word+"yay")
else:
  print(word[1:]+word[0]+"ay")
  