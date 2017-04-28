### Main Program ###
word = input("Enter a string: ")
shift = input("Enter a digit for the amount to shift the string: ")

from caesar.py import caesar_shift
print(("Shifted string is: {}".format(caesar_shift(word,shift))))