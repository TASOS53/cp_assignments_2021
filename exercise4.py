import random
suggestedFile=input("Type the absolute path of your file\n")
file=open(suggestedFile,"r")


lista=[]
for line in file:
    for word in line.split():
        lista.append(word)
newLista=[]
for i in range(len(lista)-2):
    newLista.append(lista[i:i+3])

position=newLista.index((random.choice(newLista)))
print(newLista[position][0],end =' ')
print(newLista[position][1],end =' ')
print(newLista[position][2],end =' ')
wordCounter=3
word2 = newLista[position][1]
word3 = newLista[position][2]

while wordCounter<200:
    found=0
    for miniList in newLista:
        if miniList[0]==word2 and miniList[1]==word3:
            print(miniList[2],end=' ')
            wordCounter=wordCounter+1
            word2=miniList[1]
            word3=miniList[2]
            found=1
            break
    if found==0:
        break
print('')

file.close()
