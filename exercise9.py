import math

suggestedFile=input("Type the absolute path of your file\n")
file=open(suggestedFile,"r")

dictionary={}
for i in range(1,127,2):
    dictionary[chr(i)]=0

totalCharCount=0
for line in file:
    for charachter in line:
        x=ord(charachter)
        if x%2==1:
            totalCharCount+=1
            y=dictionary[charachter]+1
            dictionary.update({charachter:y})

for dictKey, dictValue in dictionary.items():
    percentage = math.ceil((dictValue / totalCharCount) * 100)
    strg = ''
    for i in range(percentage):
        strg= strg + '*'
    print("%s: %s" %(dictKey, strg))

file.close()
