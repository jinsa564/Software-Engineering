str1=input("enter the string:")
print("original string:",str1)
char=str1[0]
length=len(str1)
str1=str1.replace(char,'$')
str1=char+str1[1:]
print("repalced string:",str1)