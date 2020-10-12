import time

def partition(data,head,tail,drawData,timeTick):
    border = head
    pivot = data[tail]
    drawData(data,getArray(len(data),head,tail,border,border))
    time.sleep(timeTick)
    for j in range(head,tail):
        if data[j] < pivot:
            drawData(data, getArray(len(data), head, tail, border, j,True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getArray(len(data), head, tail, border, j, True))
        time.sleep(timeTick)

    drawData(data, getArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]

    return border

def quicksort(data,head,tail,drawData,timeTick):
    if head<tail:
        # partition index
        partitionIdx = partition(data,head,tail,drawData,timeTick)

        # left partition
        quicksort(data,head,partitionIdx-1,drawData,timeTick)

        # right partition
        quicksort(data,partitionIdx+1,tail,drawData,timeTick)


def getArray(datalen,head,tail,border,currIdx,isSwaping=False):
    colorArray=[]

    for i in range(datalen):

        if i>=head and i<=tail:
            colorArray.append('gray')
        elif i<border:
            colorArray.append('green')
        else:
            colorArray.append('white')

        if i== tail:
            colorArray[i]='blue'
        elif i==border:
            colorArray[i]='red'
        elif i==currIdx:
            colorArray[i]='yellow'

        if isSwaping:
            if  i==currIdx:
                colorArray[i]='green'
            elif i==border:
                colorArray[i]='red'

    return colorArray

