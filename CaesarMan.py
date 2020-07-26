#!/usr/bin/python3

encdec = input("(E)ncrypt/(D)ecrypt?: ")
if encdec.lower() == "e":
	text = input("Enter text to Encrypt: ")
	try:
		shift = int(input("Please enter the shifting number (between - 25 and 25): "))
	except ValueError:
		print("Error: Expected an integer")
		exit(-1)
	if shift < -25 or shift > 25:
		print("Error: Shifting Number not in Range")
		exit(-2)
	output = ""
	for char in text:
		if char.islower() == False and char.isupper() == False:
			output += char
		else:
			compensate = 96 if char.islower() == True else 64
			acc = ord(char) + shift
			if acc > (compensate + 26):
				compchar = chr(acc - 26)
			elif acc < (compensate + 1):
				compchar = chr(acc + 26)
			else:
				compchar = chr(acc)
			output += compchar
	print("The Encrypted Text:", output)
elif encdec.lower() == "d":
	text = input("Enter text to Decrypt: ")
	shift = input("Please enter the shifting number (between - 25 and 25) or B for Brute Force: ")
	try:
		shift = int(shift)
	except ValueError:
		if shift.lower() != "b":
			print("Error: Expected an integer or 'B'")
			exit(-1)
	if (shift != "b" and shift != "B") and (shift < -25 or shift > 25):
		print("Error: Shifting Number not in Range")
		exit(-2)	
	if shift != "b" and shift != "B":
		output = ""
		for char in text:
			if char.islower() == False and char.isupper() == False:
				output += char
			else:
				compensate = 96 if char.islower() == True else 64
				acc = ord(char) - shift
				if acc > (compensate + 26):
					compchar = chr(acc - 26)
				elif acc < (compensate + 1):
					compchar = chr(acc + 26)
				else:
					compchar = chr(acc)
				output += compchar
		print("The Decrypted Text:", output)
	else:
		intelligent = True if input("Enter 'Y' if you want intelligent bruteforcing: ").lower() == "y" else False
		if intelligent:
			try:
				buff = open("exceptions.nhx", "r")
			except FileNotFoundError:
				print("Error: exceptions.nhx file missing. Cannot Continue")
				exit(1)
			wordslist = buff.read()
			buff.close()
			wordslist = wordslist.split("\n")
			for i in range(51):
				shift = i - 25
				output = ""
				for char in text:
					if char.islower() == False and char.isupper() == False:
						output += char
					else:
						compensate = 96 if char.islower() == True else 64
						acc = ord(char) - shift
						if acc > (compensate + 26):
							compchar = chr(acc - 26)
						elif acc < (compensate + 1):
							compchar = chr(acc + 26)
						else:
							compchar = chr(acc)
						output += compchar
				words = output.split(" ")
				flagged = 0
				for word in words:
					if word.lower() == word and word.upper() == word:
						continue
					if "a" not in word and "e" not in word and "i" not in word and "o" not in word and "u" not in word and word.lower() not in wordslist:
						flagged = 1
				if flagged:
					pass
				else:
					print("\nPossible Decrypted Text:", output)
		else:
			for i in range(51):
				shift = i - 25
				output = ""
				for char in text:
					if char.islower() == False and char.isupper() == False:
						output += char
					else:
						compensate = 96 if char.islower() == True else 64
						acc = ord(char) - shift
						if acc > (compensate + 26):
							compchar = chr(acc - 26)
						elif acc < (compensate + 1):
							compchar = chr(acc + 26)
						else:
							compchar = chr(acc)
						output += compchar
				print("\nPossible Decrypted Text:", output)
else:
	print("Exitting..")
	exit(0)
