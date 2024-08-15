import subprocess
import re

def get_password():
	x = 3
	while x > 1:
		x-= 1
		print(f"You have {x} Attempts left")
		password = input("--------Please, Enter Your Password------- \n")
		confirm_password = input("-------Kindly Confirm Your Password------- \n")
		if password == confirm_password:
			return password
		else:
			#print("_"*50)
			print(" ----> Passwords do not match. Please try again!")
			#print("-"*50)
				
				
def check_password_strength(password):
	if len(password) <= 8:
		return False
	if not re.search (r'[A-Z]', password):
		return False
	if not re.search (r'[a-z]', password):
		return False
	if not re.search (r'[0-9]', password):
		return False
	if not re.search (r'[!@#$%^&*()-_=+{};:<>,.?]', password):
		return False
	return True

def password_feedback(password):
	if check_password_strength(password) == True:
		#print("_"*50)
		print(" ----> You have a STRONG password right there!")
		#print("-"*50)
	else:
		#print("_"*50)
		print(" ----> Your password is too WEAK, Make sure it is longer than 8 Characters and has numbers and special characters")
		#print("-"*50)

def simulate_hashcat(password):
	try:
		with open("password_hash.txt", "w") as file:
			file.write(password)
		result = subprocess.run(['hashcat', '-a', '0', '-m', '0', 'password_hash.txt', 'rockyou.txt'], capture_output=True, text=True)
		#Check if crack is successfu or not
		if "Cracked" in result.stdout:
			#print("_"*50)
			print("----> Oops! Your password is not as safe as we'd thought!")
			#print("-"*50)
		else:
			#print("_"*50)
			print(" ----> Wooo! Your password is as STRONG as we'd thought")
			#print("-"*50)
	except Exception as e:
		#print("_"*50)
		print(f" ----> An error occurred while attempting to crack passwor: {e}")
		#print("-"*50)
