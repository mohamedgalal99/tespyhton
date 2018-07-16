import sys

char1 = input("Enter first character: ")
char2 = input("Enter cipher of first character: ")
txt = input("Enter ur plain text:")

if ord(char2) > ord(char1):
    shift = ord(char2) - ord(char1)
elif ord(char2) < ord(char1):
    #shift = (ord(char2) + ord('z')) - ord(char1)
    shift = ord('z') - ((ord('z')-ord(char1))+(ord(char1)-ord(char2)))

for i in txt:
    #if ord(i) < ord('a') or ord(i) > ord('z') or ord(i) != " ":
     #   print('Unsupported char, no number or special char')
     #   sys.exit()
    if i == " ":
        print(" ", end=""),
        continue
    if ((ord(i) + shift) <= ord('z')):
        print(chr(ord(i) + shift), end=""),
    else:
        #encryption above ord('z') 
        print(chr(((ord(i) + shift) - ord('z')) -1 + ord('a')), end=""),
    
