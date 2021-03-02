import json
import urllib.request
import datetime
import time

DrawIdList=[]
current_date=datetime.datetime.now()
current_day=current_date.strftime("%d")
for i in range (1, int(current_day)+1):
    if i<10:
        FromDate="2021-02-0" +  str(i)
    else:
        FromDate="2021-02-" + str(i)
    ToDate=FromDate
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/" + FromDate + "/" + ToDate +'/draw-id'
    response=urllib.request.urlopen(url)
    data=response.read()
    data=json.loads(data)
    DrawIdList.append(data[0])
    time.sleep(2)

winningNumbersList=[]
for i in DrawIdList:
    url="https://api.opap.gr/draws/v3.0/1100/" + str(i)
    response=urllib.request.urlopen(url)
    data=response.read()
    data=json.loads(data)
    winningNumbersList.append(data['winningNumbers']['list'])
    time.sleep(2)


array=[]
for i in range(80):
    array.append(0)


for i in range(int(current_day)):
    for j in range(20):
        array[winningNumbersList[i][j]-1]+=1
print(array)
print("\n")

for i in range(80):
    print("Νούμερο:%d Ποσοστό εμφάνισης:%d" %(i+1, (array[i]/int(current_day))*100))
