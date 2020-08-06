from tkinter import *
from datetime import datetime
import os
import random
from PIL import Image, ImageTk

sentence_list=[]
with open("sentences.txt","r") as file:
    sentence1 = file.read()

sentence_list = (sentence1.split("\n"))
sentenace_list = sentence_list.pop(len(sentence_list)-1)

root = Tk()
root.title("Typing Speed Test")
root.geometry("800x250")

photo = PhotoImage("C:/Users/deven/Python projects/Tkinter/img2.gif")

chosen_text = StringVar()
chosen_text.set("Wait a sec....")
l1 = Label(root,textvariable=chosen_text,font=("Helvetica", 18))
l1.pack(side=TOP,expand=True,fill=X, padx=40)

e1= Entry(root, fg='Red',font=("Helvetica", 15))
e1.pack(side=TOP,expand=True,fill=X)

result = StringVar()
l2 = Label(root, textvariable=result, font=("Helvetica", 16))
l2.pack(side=TOP, fill=X)

def main():
    e1.delete(0,END)
    result.set("Please wait.....")
    def sel_text():
        global sentence_list
        text = random.choice(sentence_list)
        return text

    #Starting the event of typing
    def s_time(event):
        global stime
        stime = datetime.now()
        print("start",stime)

    #End of typing stage and start of calculation stage
    def time_cal(event):
        global etime
        global stime
        global text
        etime = datetime.now()
        print("etime",etime)

        #time lapse in minutes
        duration = (etime - stime).seconds/60
        print("timelapse",duration)
        text_input = e1.get()
        text_select = chosen_text.get()

        if (text_input!=''):
            words_count = text_input.split(' ')
            wpm = len(words_count)/duration
            count = 0
            for i, char in enumerate(text_select):
                try:
                    if text_input[i]==char: count+=1
                except: pass
            accuracy = count/len(text_select)*100
            display="Duration: "+str(duration*60)+"secs | Accuracy: "+str(int(accuracy))+"% | WPM: "+str(int(wpm))+" words/min"   
        else:
            display="You haven't entered anything"
        result.set(display)
            
    def execution():
        e1.bind('<Button>',s_time)
        e1.bind('<Return>',time_cal)

    #assigning to label-l1
    chosen_text.set(sel_text())
    #calling execution function to start the calculation process
    execution()

b1=Button(root,text="Test restart",command=main, fg='black',font=("Helvetica", 15))
b1.pack(side=LEFT, expand=True, fill=X, padx=5, pady=10)

b2=Button(root,text="Quit test", command=root.destroy, fg='black',font=("Helvetica", 15))
b2.pack(side=LEFT, expand=True, fill=X, padx=5, pady=10)

if __name__ == "__main__":
    main()  


root.mainloop()
