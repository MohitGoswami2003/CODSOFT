import random 
import array 

#length of password..... 
length =int(input("Enter the length of password :"))

# declare arrays of the character for password .....

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<'] 

# combines all the character  to form one array .....

password_generate= numbers + lower_case + upper_case + symbols

random_number = random.choice(numbers) 
random_lower = random.choice(lower_case) 
random_upper = random.choice(upper_case) 
random_symbols = random.choice(symbols) 

pwd = random_number + random_lower + random_upper + random_symbols


#loop the length of password that is greater than 4....
for x in range(length - 4): 
	pwd = pwd + random.choice(password_generate) 

	
	pwd_list = array.array('u', pwd) 
	random.shuffle(pwd_list) 

password = "" 
for x in pwd_list: 
		password = password + x 
		
# print out password
print("PASSWORD IS : ",password) 
