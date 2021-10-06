# alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

def encrypt (text,s):

 result = ""

 for i in range (len(text)):
     char=text[i]

     if (char.isupper()):
         result += char((ord(char) +s - 65)%26 + 65)
     else:
         result += char((ord(char) + s-97)%26 + 97)
     return result   


word= str(input("Enter a word to encrypt: "))
s = int(input("Enter the key: "))
print("Cipher text is :" + encrypt(word, s))

