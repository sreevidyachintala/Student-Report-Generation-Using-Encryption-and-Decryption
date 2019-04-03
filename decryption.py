import os

filename = input("Enter file name to Decrypt - ")
dec ={'T': 'A', 't': 'a', 'D': 'B', 'd': 'b', 'L': 'C', 'l': 'c', 'O': 'D', 'o': 'd', 'F': 'E', 'f': 'e', 'A': 'F', 'a': 'f', 'G': 'G', 'g': 'g', 'J': 'H', 'j': 'h', 'K': 'I', 'k': 'i', 'R': 'J', 'r': 'j', 'I': 'K', 'i': 'k', 'C': 'L', 'c': 'l', 'V': 'M', 'v': 'm', 'P': 'N', 'p': 'n', 'W': 'O', 'w': 'o', 'U': 'P', 'u': 'p', 'X': 'Q', 'x': 'q', 'Y': 'R', 'y': 'r', 'B': 'S', 'b': 's', 'E': 'T', 'e': 't', 'Z': 'U', 'z': 'u', 'Q': 'V', 'q': 'v', 'S': 'W', 's': 'w', 'N': 'X', 'n': 'x', 'M': 'Y', 'm': 'y', 'H': 'Z', 'h': 'z', ' ': ' ', ':': ':', '-': '-', '.': '.', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '\n': '\n'}

try:
	with open('Encryption/'+filename) as f:
		with open("Decryption/dec.txt", "w") as f1:
			for line in f:
				for ch in line:
					if ch in dec:
						f1.write(dec[ch])

except EnvironmentError:
    print("File Not Found")
    exit()

print("Decrypted Successfully")
os.remove('Encryption/'+filename)