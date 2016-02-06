from tkinter import *
import datetime
import time

tk = Tk()

canvas = Canvas(tk, width=240,height=160)

#display the canvas
canvas.pack()

#black background
canvas.create_rectangle (0,0, 240,160,fill="black")

#coordinates of the hour boxes
hbox5=10, 10+80, 30, 30+80
hbox4=10, 10+120, 30, 30+120
hbox3=10+40, 10, 30+40, 30
hbox2=10+40, 10+40, 30+40, 30+40
hbox1=10+40, 10+80, 30+40, 30+80
hbox0=10+40, 10+120, 30+40, 30+120

#coordinates of the minute boxes
mbox6=10+80, 10+40, 30+80, 30+40
mbox5=10+80, 10+80, 30+80, 30+80
mbox4=10+80, 10+120, 30+80, 30+120
mbox3=10+120, 10, 30+120, 30
mbox2=10+120, 10+40, 30+120, 30+40
mbox1=10+120, 10+80, 30+120, 30+80
mbox0=10+120, 10+120, 30+120, 30+120

#coordinates of the seconds boxes
sbox6=10+160, 10+40, 30+160, 30+40
sbox5=10+160, 10+80, 30+160, 30+80
sbox4=10+160, 10+120, 30+160, 30+120
sbox3=10+200, 10, 30+200, 30
sbox2=10+200, 10+40, 30+200, 30+40
sbox1=10+200, 10+80, 30+200, 30+80
sbox0=10+200, 10+120, 30+200, 30+120

def create_boxes():
    #These box coordinates should be set as tuple variables and referenced throughout
    #instead of being hard-coded in each and every time

    #Draw the hours block
    canvas.create_rectangle (hbox0,fill="dimgray")
    canvas.create_rectangle (hbox1,fill="dimgray")
    canvas.create_rectangle (hbox2,fill="dimgray")
    canvas.create_rectangle (hbox3,fill="dimgray")
    canvas.create_rectangle (hbox4,fill="dimgray")
    canvas.create_rectangle (hbox5,fill="dimgray")

    #Draw the minutes block
    canvas.create_rectangle (mbox0,fill="dimgray")
    canvas.create_rectangle (mbox1,fill="dimgray")
    canvas.create_rectangle (mbox2,fill="dimgray")
    canvas.create_rectangle (mbox3,fill="dimgray")
    canvas.create_rectangle (mbox4,fill="dimgray")
    canvas.create_rectangle (mbox5,fill="dimgray")
    canvas.create_rectangle (mbox6,fill="dimgray") 

    #Draw the seconds block
    canvas.create_rectangle (sbox6,fill="dimgray")
    canvas.create_rectangle (sbox5,fill="dimgray")
    canvas.create_rectangle (sbox4,fill="dimgray")
    canvas.create_rectangle (sbox3,fill="dimgray")
    canvas.create_rectangle (sbox2,fill="dimgray")
    canvas.create_rectangle (sbox1,fill="dimgray")
    canvas.create_rectangle (sbox0,fill="dimgray")


def fill_boxes_seconds(binseconds):
    #fills in boxes for the seconds block
    #seconds, ones column
    bintens=binseconds[0]
    binones=binseconds[1]
    #ones column
    if binones[7]=="1": 
        canvas.create_rectangle(sbox0,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox0,fill="dimgray")
    if binones[6]=="1": 
        canvas.create_rectangle(sbox1,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox1,fill="dimgray")
    if binones[5]=="1": 
        canvas.create_rectangle(sbox2,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox2,fill="dimgray")
    if binones[4]=="1": 
        canvas.create_rectangle(sbox3,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox3,fill="dimgray")
    #tens column
    if bintens[7]=="1": 
        canvas.create_rectangle(sbox4,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox4,fill="dimgray")
    if bintens[6]=="1": 
        canvas.create_rectangle(sbox5,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox5,fill="dimgray")
    if bintens[5]=="1": 
        canvas.create_rectangle(sbox6,fill="turquoise3")
    else:
        canvas.create_rectangle(sbox6,fill="dimgray")

def fill_boxes_minutes(binminutes):
    #fills in boxes for the seconds block
    #seconds, ones column
    bintens=binminutes[0]
    binones=binminutes[1]
    #ones column
    if binones[7]=="1": 
        canvas.create_rectangle(mbox0,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox0,fill="dimgray")
    if binones[6]=="1": 
        canvas.create_rectangle(mbox1,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox1,fill="dimgray")
    if binones[5]=="1": 
        canvas.create_rectangle(mbox2,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox2,fill="dimgray")
    if binones[4]=="1": 
        canvas.create_rectangle(mbox3,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox3,fill="dimgray")
    #tens column
    if bintens[7]=="1": 
        canvas.create_rectangle(mbox4,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox4,fill="dimgray")
    if bintens[6]=="1": 
        canvas.create_rectangle(mbox5,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox5,fill="dimgray")
    if bintens[5]=="1": 
        canvas.create_rectangle(mbox6,fill="turquoise3")
    else:
        canvas.create_rectangle(mbox6,fill="dimgray")

def fill_boxes_hours(binhours):
    #fills in boxes for the seconds block
    #seconds, ones column
    bintens=binhours[0]
    binones=binhours[1]
    #ones column
    if binones[7]=="1": 
        canvas.create_rectangle(hbox0,fill="turquoise3")
    else:
        canvas.create_rectangle(hbox0,fill="dimgray")
    if binones[6]=="1": 
        canvas.create_rectangle(hbox1,fill="turquoise3")
    else:
        canvas.create_rectangle(hbox1,fill="dimgray")
    if binones[5]=="1": 
        canvas.create_rectangle(hbox2,fill="turquoise3")
    else:
        canvas.create_rectangle(hbox2,fill="dimgray")
    if binones[4]=="1": 
        canvas.create_rectangle(hbox3,fill="turquoise3")
    else:
        canvas.create_rectangle(hbox3,fill="dimgray")
    #tens column
    if bintens[7]=="1": 
        canvas.create_rectangle(hbox4,fill="turquoise3")
    else:
        canvas.create_rectangle(hbox4,fill="dimgray")
    if bintens[6]=="1": 
        canvas.create_rectangle(hbox5,fill="turquoise3")
    else:
        canvas.create_rectangle(hbox5,fill="dimgray")

def int_to_bin(integer):
#converts an integer into a formatted binary
    binary = '{0:08b}'.format(integer)
    return binary

def convert_to_clock_binary(number):
#returns a list with the binary for the tens place,
#and binary for the ones place
    tens = number/10
    tens = int(tens)
    bintens=int_to_bin(tens)
    ones = number%10
    binones=int_to_bin(ones)
    output = bintens,binones
    return output

def draw_time():
    #fill in the boxes based on current time
    now=datetime.datetime.now()
    time=now.hour
    binhours=convert_to_clock_binary(time)
    fill_boxes_hours(binhours)
    time=now.minute
    binminutes=convert_to_clock_binary(time)
    fill_boxes_minutes(binminutes)
    time=now.second
    binseconds=convert_to_clock_binary(time)
    fill_boxes_seconds(binseconds)
    
create_boxes()


x=1
while x==1:
    draw_time()
    tk.update()
    time.sleep(1)
    

###########
#tests#####
###########


#time is number of hours and minutes and seconds
#using function convert_to_clock_binary
#and function fill_boxes_minutes
#test that binary clock is working properly





#test- assign a seconds/minutes/hour number to variable time
#call convert_to_clock_binary
#should get a list back with the tens, in binary, and ones, in binary
#time=59
#bintime=convert_to_clock_binary(time)
#print(bintime)

#insert a box variable to have it display
#fill_a_box(hbox0)
