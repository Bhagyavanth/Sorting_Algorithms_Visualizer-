from tkinter import *
from tkinter import ttk
from random import *
from BubbleSort import bubbleSort
from mergeSort_algo import *
from insertion_sorting import *
from selection_algo import *
from quicksort_algo import *

root=Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900,700)
root.config(bg='black')

selected_alg=StringVar()
data=[]

def drawData(data,colorArray):
    canvas.delete('all')
    c_height=380
    c_width=670
    x_width=c_width/(len(data)+1)
    offset=30
    normalizedata=[i/max(data) for i in data]
    for i, height in enumerate(normalizedata):
        x0=i*x_width + offset
        y0=c_height-height*340

        x1=(i+1)*x_width+offset
        y1=c_height

        canvas.create_rectangle(x0,y0,x1,y1,fil=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    root.update_idletasks()
def generate():
    global data
    min_val=int(minval_entry.get())
    max_val=int(maxval_entry.get())
    size=int(size_entry.get())
    data=[]
    for i in range(size):
        data.append(randrange(min_val,max_val+1))

    drawData(data,['red' for x in range(len(data))])

def startAlgo():
    global data
    if Menu.get()=='Bubble sort':
        bubbleSort(data,drawData,speed_scale.get())
    elif Menu.get()=='Merge sort':
        mergeSort(data, drawData, speed_scale.get())
    elif Menu.get()=='Insertion sort':
        insertionSort(data, drawData, speed_scale.get())
    elif Menu.get()=='Selection sort':
        selectionSort(data, drawData, speed_scale.get())
    elif Menu.get()=='Quick sort':
        quicksort(data,0,len(data)-1, drawData, speed_scale.get())
        drawData(data,['green' for x in range(len(data))])


# creating a frame
frame=Frame(root, width=700,height=200,bg='orange')
frame.grid(row=0,column=0, padx=10,pady=5)

# creating a canvas
canvas=Canvas(root, width=700,height=400,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

# creating a start button
start_bttn=Button(frame,text='   Start   ',bg='yellow',activebackground='red',command=startAlgo)
start_bttn.grid(row=0,column=2,padx=5,pady=5)

speed_scale=Scale(frame,from_=0.1, to=6.0,length=200,digits=2,resolution=0.1,orient=HORIZONTAL,label='Select delay')
speed_scale.grid(row=1,column=6,padx=5,pady=5)

# creating a combobox
Label(frame, text='Algorithm',bg='orange').grid(row=0,column=0,padx=5,pady=5,sticky=W)
Menu=ttk.Combobox(frame,textvariable=selected_alg,values=['Bubble sort','Quick sort','Merge sort','Insertion sort','Selection sort'])
Menu.grid(row=0,column=1,padx=5,pady=5)
Menu.set('Bubble sort')

size_entry=Scale(frame,from_=3, to=50,resolution=1,orient=HORIZONTAL,label='Size')
size_entry.grid(row=1,column=1,padx=5,pady=5)

minval_entry=Scale(frame,from_=1, to=10,resolution=1,orient=HORIZONTAL,label='Min value')
minval_entry.grid(row=1,column=2,padx=5,pady=5)

maxval_entry=Scale(frame,from_=11, to=100,resolution=1,orient=HORIZONTAL,label='Max value')
maxval_entry.grid(row=1,column=3,padx=5,pady=5)



# creating a generate button
generate_bttn=Button(frame,text='Generate',bg='green',fg='white',activebackground='red',command=generate)
generate_bttn.grid(row=0,column=3,padx=5,pady=5)

status_bar=Label(root,text='Created by: Bhagyawanth_Avantagi',
                 font=('arial',10,'bold'),bg='sky blue')
status_bar.grid(row=2,column=0)
root.mainloop()