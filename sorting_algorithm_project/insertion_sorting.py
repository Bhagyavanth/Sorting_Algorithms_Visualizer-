import time

def insertionSort(data,drawData,speed):
    time.sleep(speed)
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        while j>=0 and key<data[j]:
            data[j+1] =data[j]
            data[j]=key
            drawData(data, getColorArray(len(data),j))
            time.sleep(speed)
            j-=1
        data[j+1]=key
    drawData(data, ['green' for x in range(len(data))])

def getColorArray(length,j):
    colorArray=[]

    for i in range(length):
        if i==j:
            colorArray.append('green')
        elif i==j-1:
            colorArray.append('red')
        else:
            colorArray.append('grey')

    return colorArray