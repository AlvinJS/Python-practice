def encrypt (text,key):
 result = ""

 for i in range (len(text)):
     char=text[i]

     if (char.isupper()):
         result += chr((ord(char) + key - 65) %26 + 65)
     else:
         result += chr((ord(char) + key - 97) %26 + 97)
 return result            

text = "Lionel"
key = 2

print(encrypt(text, key))
