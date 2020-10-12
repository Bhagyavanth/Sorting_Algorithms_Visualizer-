import time

def mergeSort(data,drawData,timetick):
    merge_Sort_Algo(data,0,len(data)-1,drawData,timetick)

def merge_Sort_Algo(data,left,right,drawData,timetick):
    if left<right:
        middle=(left+right)//2
        merge_Sort_Algo(data,left,middle,drawData,timetick)
        merge_Sort_Algo(data,middle+1,right,drawData,timetick)
        merge(data,left,middle,right,drawData,timetick)

def merge(data,left,middle,right,drawData,timetick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timetick)

    leftpart=data[left:middle+1]
    rightpart=data[middle+1:right+1]

    leftIdx = rightIdx=0

    for dataIdx in range(left,right+1):

        if leftIdx<len(leftpart) and rightIdx<len(rightpart):
            if leftpart[leftIdx] <= rightpart[rightIdx] :
                data[dataIdx]=leftpart[leftIdx]
                leftIdx+=1
            else:
                data[dataIdx] = rightpart[rightIdx]
                rightIdx += 1
        elif leftIdx<len(leftpart):
            data[dataIdx]=leftpart[leftIdx]
            leftIdx+=1

        else:
            data[dataIdx]=rightpart[rightIdx]
            rightIdx+=1


        drawData(data, ['red' if x==dataIdx else 'white' for x in range(len(data))])
        time.sleep(timetick)

    drawData(data, ['green' if x>=left and x<=right  else 'white' for x in range(len(data))])
    time.sleep(timetick)

def getColorArray(length,left,middle,right):
    colorArray=[]

    for i in range(length):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')
        else:
            colorArray.append('white')
    return colorArray