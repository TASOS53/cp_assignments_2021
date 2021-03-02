suggestedFile=input("Type the absolute path of your file\n")
file=open(suggestedFile,"r")
newCharList=[]
for line in file:
    for charachter in line:
        newCharachter=128-ord(charachter)
        newCharList.append(chr(newCharachter))
for i in range(-1,-(len(newCharList)+1),-1):
    print(newCharList[i],end ='')
file.close()
