def caesar_shift(word,shift):
	output = ""
	if len(output) == len(word):
		return output
	first=word[0]
	ascii=ord(first)
	asciishift = chr(ascii + shift)
	output = asciishift + caesar_shift(str(word[1:]),shift)
	
print (caesar_shift("hi",1))