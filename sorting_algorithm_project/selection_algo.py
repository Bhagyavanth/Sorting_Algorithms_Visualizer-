import time

def selectionSort(data,drawData,timetick):
    time.sleep(timetick)
    for i in range(len(data)):
        sel=i
        for j in range(i+1,len(data)):
            if data[sel]>data[j]:
                sel=j
            drawData(data, getColorArray(len(data), i, j, sel))
            time.sleep(timetick)
        data[i],data[sel]=data[sel],data[i]
    drawData(data, ['green' for x in range(len(data))])

def getColorArray(length,i,j,sel):
    colorArray=[]

    for x in range(length):
        if x==i:
            colorArray.append('yellow')
        elif x==j:
            colorArray.append('red')
        elif x==sel:
            colorArray.append('pink')
        elif x<i:
            colorArray.append('green')

        else:
            colorArray.append('white')

    return colorArray
