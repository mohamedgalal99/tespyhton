from getpass import getpass

count = 0
password= "lol"
print('Enter your')
while count < 3:
    input_password = getpass()
    if input_password == password:
        print("Authorized ya prince")
        break
    else :
        print("denied")
        count += 1
