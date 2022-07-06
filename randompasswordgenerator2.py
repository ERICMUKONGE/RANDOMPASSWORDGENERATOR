import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+?><|/"

while 1:
    password_len = int(input("Please the any please length of your choice:\n"))
    password_count = int(input("Please enter any number of passwords you want to generate:\n"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password : ",password)    
