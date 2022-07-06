import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+?><:}{]]\;/.,/"
length_password = int(input("Enter the length of the password:\n"))
a = "".join(random.sample(password,length_password))
print(f"Your new random generated password is {a} ")