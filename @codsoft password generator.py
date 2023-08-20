import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these :
		1. Letters
		2. Digits
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Choose a number :"))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList = characterList +string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList = characterList +string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList = characterList +string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a correct option!")

random_password = []

for i in range(length):

	# character list
	randomcharacter = random.choice(characterList)
	
	# appending a random character to password
	random_password.append(randomcharacter)

# print password as a string
print("The random password is " + "".join(random_password))
