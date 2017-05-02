
def caesar_shift(word,shift):
	"""Takes in a string and a shift amount and shifts the word that many ascii characters"""

	asciimin = 32
	asciimax = 126
	# Terminating case
	if len(word) == 0:
		return word
	# Takes the first letter of the word
	letter = word[:1]
	# If it will shift above the ascii numbers for letters
	if ord(letter) + shift >= asciimax:
		wrap =  asciimax - ord(letter)
		wrap = shift - wrap
		wrap += asciimin - 1
		
	# If it won't shift above
	else:
		wrap = ord(letter) + shift
	return chr(wrap) + caesar_shift(word[1:],shift)



