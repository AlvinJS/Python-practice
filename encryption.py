def encrypt(text,s):
 result = ""
 for i in range(len(text)):
    char = text[i]
      
    if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
    else:
         result += chr((ord(char) + s - 97) % 26 + 97)
 return result


def decrypt(text,s):
 result = ""
 for i in range(len(text)):
    char = text[i]
      
    if (char.isupper()):
         result += chr((ord(char) - s-65) % 26 + 65)
    else:
         result += chr((ord(char) - s - 97) % 26 + 97)
 return result

i=2

while i!=0:
    text= str(input("Enter text: "))
    s = int(input("Enter key: "))
    choice= int(input("choose 1 to encrypt or choose 2 to decrypt: "))
    if choice == 1:
        print ("Plain Text : " + text)
        print ("Shift pattern : " + str(s))
        print ("Cipher: " + encrypt(text,s))
    elif choice == 2:
        print ("Plain Text : " + text)
        print ("Shift pattern : " + str(s))
        print ("Cipher: " + decrypt(text,s))        
    else:
        print("choice not found")