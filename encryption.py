import os

filename = input("Enter file name to Encrypt - ")
enc ={"A":"T","a":"t","B":"D","b":"d","C":"L","c":"l","D":"O","d":"o","E":"F","e":"f","F":"A","f":"a","G":"G","g":"g","H":"J","h":"j","I":"K","i":"k","J":"R","j":"r","K":"I","k":"i","L":"C","l":"c","M":"V","m":"v","N":"P","n":"p","O":"W","o":"w","P":"U","p":"u","Q":"X","q":"x","R":"Y","r":"y","S":"B","s":"b","T":"E","t":"e","U":"Z","u":"z","V":"Q","v":"q","W":"S","w":"s","X":"N","x":"n","Y":"M","y":"m","Z":"H","z":"h"," ": " ", ":":":","-":"-",".":".","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","0":"0","\n":"\n"}

try:
	with open('ReportData/'+filename) as f:
		with open("Encryption/enc.txt", "w") as f1:
			for line in f:
				for ch in line:
					if ch in enc:
						f1.write(enc[ch])

except EnvironmentError:
    print("File Not Found")
    exit()

print("Encrypted Successfully")
os.remove('ReportData/'+filename)