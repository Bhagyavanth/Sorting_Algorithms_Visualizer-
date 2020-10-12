import time

def bubbleSort(data,drawData,speed):
    time.sleep(speed)
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data,['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(speed)

    drawData(data, ['green' for x in range(len(data))])


