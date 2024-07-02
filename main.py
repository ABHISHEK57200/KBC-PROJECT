from tkinter import * #tkinter is package(class) which include all gui functions
from tkinter.ttk import Progressbar#this package contains the progressbar class for the audience pole
from pygame import mixer # play the music
import pyttsx3  # text read and convert in voice
from twilio.rest import Client
# from time import strftime




engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

mixer.init()

mixer.music.load("KBC starting music.mp3")
mixer.music.play()



def phoneLine():
    mixer.music.load("outging ring1.mp3")  # this is load for the loading music
    mixer.music.play()  # this is play the loaded music
    callImageButton.place(x=70,y=240)
    lifelinePhonebutton.config(image=imagePhonex,state=DISABLED)

def clickPhone():
    for i in range(15):
        if questionarea.get(1.0,'end-1c')==questions[i]:
            # engine.say(f'the   answer    is the {questionAnswer[i]}')
            # engine.runAndWait()

            account_sid = "AC4ec0afdcebe05ae95280f51dc36dd310"
            auth_token = "e4bfff4d3b6148570100a8dbc1110c5e"
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                twiml=f'<Response><Say>the answer is {questionAnswer[i]}</Say></Response>',
                to="+919140311274",
                from_="+12058318938"
            )
            print(call.sid)

            mixer.music.load("kbc.mp3")
            mixer.music.play(-1)

def delete1():
    # for j in range(15):
        if questionarea.get(1.0,'end-1c')==questions[0]:
            optionButton2.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x,state=DISABLED)
            # lifelineAudiPolebutton.config(image=imageAudioPolex)
            # lifelinePhonebutton.config(image=imagePhonex)
        elif questionarea.get(1.0,'end-1c')==questions[1]:
            optionButton1.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
            # lifelineEnd.config(image=end50lifeline)
        elif questionarea.get(1.0,'end-1c')==questions[2]:
            optionButton1.config(text=' ')
            optionButton2.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[3]:
            optionButton1.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[4]:
            optionButton1.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[5]:
            optionButton2.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[6]:
            optionButton1.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[7]:
            optionButton1.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[8]:
            optionButton1.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[9]:
            optionButton2.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[10]:
            optionButton1.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[11]:
            optionButton1.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[12]:
            optionButton3.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[13]:
            optionButton1.config(text=' ')
            optionButton4.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[14]:
            optionButton1.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
        elif questionarea.get(1.0,'end-1c')==questions[15]:
            optionButton1.config(text=' ')
            optionButton3.config(text=' ')
            lifeline50button.config(image=image50x, state=DISABLED)
def audiencepolelifeline():
    mixer.music.load("new-effect-quiz-green-screen-no-copyright-effects-green-screen-kbc-quiz-contest-frame.mp3")
    mixer.music.play()
    lifelineAudiPolebutton.config(image=imageAudioPolex,state=DISABLED)
    progressbarA.place(x=555,y=190)
    progressbarB.place(x=595,y=190)
    progressbarC.place(x=635, y=190)
    progressbarD.place(x=675, y=190)

    optionNumber1.place(x=300,y=120)


    labelprogressbarA.place(x=580,y=190)
    labelprogressbarB.place(x=620, y=190)
    labelprogressbarC.place(x=660, y=190)
    labelprogressbarD.place(x=700, y=190)

    if questionarea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=20)
        progressbarC.config(value=40)
        progressbarD.config(value=50)
    elif questionarea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=65)
        progressbarD.config(value=70)
    elif questionarea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=40)
        progressbarD.config(value=80)
    elif questionarea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=40)
        progressbarB.config(value=55)
        progressbarC.config(value=40)
        progressbarD.config(value=60)
    elif questionarea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=55)
        progressbarB.config(value=60)
        progressbarC.config(value=40)
        progressbarD.config(value=20)
    elif questionarea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=45)
        progressbarB.config(value=20)
        progressbarC.config(value=55)
        progressbarD.config(value=50)
    elif questionarea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=60)
        progressbarB.config(value=20)
        progressbarC.config(value=40)
        progressbarD.config(value=50)
    elif questionarea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=35)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=30)
    elif questionarea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=40)
    elif questionarea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=40)
        progressbarC.config(value=60)
        progressbarD.config(value=50)
    elif questionarea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=50)
        progressbarB.config(value=45)
        progressbarC.config(value=60)
        progressbarD.config(value=20)
    elif questionarea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=40)
        progressbarD.config(value=60)
    elif questionarea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=40)
        progressbarB.config(value=55)
        progressbarC.config(value=50)
        progressbarD.config(value=30)
    elif questionarea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=45)
        progressbarB.config(value=20)
        progressbarC.config(value=60)
        progressbarD.config(value=40)
    elif questionarea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=20)
        progressbarB.config(value=50)
        progressbarC.config(value=45)
        progressbarD.config(value=60)





def select(event):

    callImageButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    labelprogressbarA.place_forget()
    labelprogressbarB.place_forget()
    labelprogressbarC.place_forget()
    labelprogressbarD.place_forget()


    b=event.widget
    # print(b)
    value=b['text']
    # print(b)
    # print(value)
    # if value==questionAnswer[0]:
    #     #mixer.music.load("kbc.mp3")
    #     #mixer.music.play(-1)
    for i in range(15):
        if value==questionAnswer[i]:
            if value==questionAnswer[14]:
                def close():
                    root2.destroy()  # root1 is the name of current window which call the destroy method.
                    # the destroy method is predefined which is use to clse the curent window.
                    roots.destroy()

                def playagain():
                    lifeline50button.config(state=NORMAL, image=image50)
                    lifeline50button.config(state=NORMAL, image=imageAudiPole)
                    lifeline50button.config(state=NORMAL, image=callImage)

                    root2.destroy()
                    questionarea.delete(1.0, END)
                    questionarea.insert(END, questions[0])
                    questionarea.delete(1.0, END)
                    questionarea.insert(END, questions[0])
                    optionButton1.config(text=option1[0])
                    optionButton2.config(text=option2[0])
                    optionButton3.config(text=option3[0])
                    optionButton4.config(text=option4[0])
                    logolabel1.config(image=amount)


                root2 = Toplevel()  # this class is use to create a new window
                root2.overrideredirect(True)

                mixer.music.load("Kbcwon.mp3")
                mixer.music.play(-1)

                root2.geometry('500x400+140+20')
                root2.maxsize(width=500, height=400)
                root2.config(bg='black', bd=0)
                root2.title('you won 0 paunds')
                gamelosswindow = Label(root2, image=imageCenter, bd=0)
                gamelosswindow.pack(pady=30)
                winlable = Label(root2, text='You won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlable.pack()
                playAgainbutton = Button(root2, text='Play again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                   activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                   command=playagain)
                playAgainbutton.pack()
                closeButton = Button(root2, text='Close', bg='black', font=('arial', 20, 'bold'), fg='white',
                                     activebackground='black', activeforeground='white', bd=0, command=close)
                closeButton.pack()
                happyimage = PhotoImage(file='happy.png')
                happylable = Label(root2, image=happyimage, bg='black')

                happylable.place(anchor=NW, y=300, x=30)
                happyimage2 = PhotoImage(file='happy.png')
                happylbel1 = Label(root2, image=happyimage2, bg='black')
                happylbel1.place(x=400, y=300)
                root2.mainloop()
                break;
            mixer.music.load("kbc-timer-music_2_second-level-music-for-kbc.mp3")
            mixer.music.play()









            # logolabel1.remove(1.0, END)
            questionarea.delete(1.0,END)

            questionarea.insert(END,questions[i+1])
            optionButton1.config(text=option1[i+1])
            optionButton2.config(text=option2[i+1])
            optionButton3.config(text=option3[i+1])
            optionButton4.config(text=option4[i+1])
            logolabel1.config(image=Amountlist[i])

            # timeFun()


        if value not in questionAnswer:
            def close():
                root1.destroy()# root1 is the name of current window which call the destroy method.
                # the destroy method is predefined which is use to clse the curent window.
                roots.destroy()

            def tryagain():
                lifeline50button.config(state=NORMAL, image=image50)
                lifelineAudiPolebutton.config(state=NORMAL, image=imageAudiPole)
                callImageButton.config(state=NORMAL, image=callImage)
                root1.destroy()
                questionarea.delete(1.0,END)
                questionarea.insert(END, questions[0])
                questionarea.delete(1.0, END)
                questionarea.insert(END, questions[0])
                optionButton1.config(text=option1[0])
                optionButton2.config(text=option2[0])
                optionButton3.config(text=option3[0])
                optionButton4.config(text=option4[0])
                logolabel1.config(image=amount)



            root1=Toplevel()#this class is use to create a new window
            root1.overrideredirect(True)
            root1.geometry('500x400+140+20')
            root1.maxsize(width=500,height=400)
            root1.config(bg='black',bd=0)
            root1.title('you won 0 paunds')
            gamelosswindow=Label(root1,image=imageCenter,bd=0)
            gamelosswindow.pack(pady=30)
            loselable=Label(root1,text='You lose',font=('arial',40,'bold'),bg='black',fg='white')
            loselable.pack()
            trybutton=Button(root1,text='Try again',font=('arial',20,'bold'),bg='black',fg='white',
                             activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=tryagain)
            trybutton.pack()
            closeButton=Button(root1,text='Close',bg='black',font=('arial',20,'bold'),fg='white',
                               activebackground='black',activeforeground='white',bd=0,command=close)
            closeButton.pack()
            sadimage = PhotoImage(file='sad.png')
            sadlable=Label(root1, image=sadimage,bg='black')

            sadlable.place(anchor=NW,y=300,x=30)
            sadimage2=PhotoImage(file='sad.png')
            sadlbel1=Label(root1,image=sadimage2,bg='black')
            sadlbel1.place(x=400,y=300)
            root1.mainloop()
            break
# def tryagain():
#     lifeline50button.config(state=NORMAL,image=image50)
#     lifeline50button.config(state=NORMAL, image=imageAudiPole)
#     lifeline50button.config(state=NORMAL, image=callImage)
#     roots.destroy()
#     questionarea.insert(END,questions[0])
#     questionarea.delete(1.0,END)
#     questionarea.insert(END,questions[0])
#     optionButton1.config(text=option1[0])
#     optionButton2.config(text=option2[0])
#     optionButton3.config(text=option3[0])
#     optionButton4.config(text=option4[0])
#     logolabel1.config(image=amount)













# wrongOption=["Managing function calls"]

questionAnswer=["all of the above","select empid where empid = 1009 and Lastname = 'GELLER';"
    ,"Merge Sort","n","1.44log nAssume base of log is 2","Schema"
    ,"It is a type of system software","2","Data Warehouse","Cardinality","JDK","JAVA_HOME",
    "Floating-point value assigned to an integer type","Object class","ServerSocket"]


questions=["Which one of the following is an application of Stack Data Structure?",
           "Which one of the following given statements possibly contains the error?",
           "Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity",
           "In the worst case, the number of comparisons needed to search a singly linked list of length n for a given element is",
           "What is the worst case possible height of AVL tree?",
            "Which one of the following is commonly used to define the overall design of the database?",
         " A Database Management System is a type of _________software.",
          " The minimum number of stacks needed to implement a queue is",
           " A huge collection of the information or data accumulated form several different sources is known as ________:",
           "Which of the following refers to the number of tuples in a relation?",
           "Which component is used to compile, debug and execute the java programs?",
           "Which environment variable is used to set the java path?",
           " What is Truncation in Java?",
           "Which of the following is a superclass of every class in Java?",
           "Which class provides system independent server side implementation?"]
option1=["Managing function calls","select * from emp where empid = 10003;",
         "Insertion Sort","log(2*n)",
         "2LognAssume base of log is 2","Application program",
         "It is a type of system software","3",
         "Data Management","Entity"," JRE"
         ,"MAVEN_Path","Floating-point value assigned to a Floating type",
         "ArrayList","Server",
         ]

option2=["The stock span problem","select empid from emp where empid = 10006;",
         "Quick Sort","n/2",
         "1.44log nAssume base of log is 2","Data definition language",
         "It is a kind of application software","1",
         "Data Mining","Column","JIT"
         ,"JavaPATH","Floating-point value assigned to an integer type",
         "Abstract class","ServerReader",
]

option3=["Arithmetic expression evaluation","select empid from emp;",
         "Heap Sort","log(2*n) -1",
         "Depends upon implementation","Schema",
         "It is a kind of general software","2",
         "Data Warehouse","Cardinality","JDK"
         ,"JAVA","Integer value assigned to floating type",
         "Object class","Socket",]

option4=["all of the above","select empid where empid = 1009 and Lastname = 'GELLER';",
         "Merge Sort","n",
         "Theta(n)","Source code",
         "Both A and C","4",
         "Both B and C","None of the above","JVM"
         ,"JAVA_HOME","Integer value assigned to floating type",
         "String","ServerSocket",]


roots=Tk() #it is function of tkinter class which is use to create window
roots.geometry('1270x652+0+0')# it is set size of the window
roots.title("KBC QUIZE GAME")# this function is use to create title of the window
roots.config(bg='black')

leftFrame=Frame(roots,bg='black',padx=90)
leftFrame.grid(row=0,column=0)

topFrame=Frame(leftFrame,bg='black',pady=25)
topFrame.grid()

centerFrame=Frame(leftFrame,bg='black',pady=30)
centerFrame.grid(row=1,column=0)

bottomFrame=Frame(leftFrame)
bottomFrame.grid(row=2,column=0)


rightFrame=Frame(roots, padx=50,pady=25,bg='black')
rightFrame.grid(row=0,column=1)

image50=PhotoImage(file="50-50.png")
image50x=PhotoImage(file="50-50-X.png")
lifeline50button=Button(topFrame,image=image50,bg='black',bd=0,activebackground='black',height=80,width=180,command=delete1)
lifeline50button.grid(row=0,column=0)


# lifelineEnd=Label(topFrame,image=end50lifeline)
# lifelineEnd.grid(row=0,column=0)

imageAudiPole=PhotoImage(file="audiencePole.png")
imageAudioPolex=PhotoImage(file="audiencePoleX.png")
lifelineAudiPolebutton=Button(topFrame,image=imageAudiPole,bg='black',bd=0,activebackground='black'
                              ,height=80,width=180,command=audiencepolelifeline)
lifelineAudiPolebutton.grid(row=0,column=1)

imagePhone=PhotoImage(file="PhoneAFriend.png")
imagePhonex=PhotoImage(file="phoneAFriendX.png")
lifelinePhonebutton=Button(topFrame,image=imagePhone,bg='black',bd=0,activebackground='black',height=80,width=180,command=phoneLine)
lifelinePhonebutton.grid(row=0,column=2)
callImage=PhotoImage(file="phone.png")

callImageButton=Button(roots,image=callImage,bg='black',bd=0,activebackground='black',command=clickPhone)


imageCenter=PhotoImage(file='center.png')
logolabel=Label(centerFrame,image=imageCenter,bg='black',activebackground='black',height=200,width=300)
logolabel.grid(row=1,column=0)
# imageCenter.grid(row=1,column=0)
# def timeFun():
#     time_string = strftime('%H:%M:%S')
#     timelable.config(text=time_string)
#     timelable = Label(centerFrame, font=('times', 53, 'white'), bg='yellow')
#     timelable.grid(row=1, column=0)


layImage=PhotoImage(file='lay.png')
logoLay=Label(bottomFrame,image=layImage,bg='black')
logoLay.grid(row=0,column=0)

amount=PhotoImage(file='Picture0.png')
amount2=PhotoImage(file='Picture1.png')
amount3=PhotoImage(file='Picture2.png')
amount4=PhotoImage(file='Picture3.png')
amount5=PhotoImage(file='Picture4.png')
amount6=PhotoImage(file='Picture5.png')
amount7=PhotoImage(file='Picture6.png')
amount8=PhotoImage(file='Picture7.png')
amount9=PhotoImage(file='Picture8.png')
amount10=PhotoImage(file='Picture9.png')
amount11=PhotoImage(file='Picture10.png')
amount12=PhotoImage(file='Picture11.png')
amount13=PhotoImage(file='Picture12.png')
amount14=PhotoImage(file='Picture13.png')
amount15=PhotoImage(file='Picture14.png')
amount16=PhotoImage(file='Picture15.png')
# amount17=PhotoImage(file='Picture15.png')

Amountlist=[amount2,amount3,amount4,amount5,amount6,amount7,amount8,
            amount9,amount10,amount11,amount12,amount13,amount14,amount15,amount16]

logolabel1=Label(rightFrame,image=amount,bd=0,bg='black')
logolabel1.grid(row=0,column=0)

questionarea=Text(bottomFrame,font=('arial',14,'bold'),width=40,height=3,wrap='word',bg='black',fg='white',bd=0)
questionarea.place(x=70,y=9)
questionarea.insert(END,questions[0])

optionNumberA=Label(bottomFrame,text='A:',font=('arial',14),bg='black',fg='white',bd=0)
optionNumberA.place(x=40,y=100)
optionButton1=Button(bottomFrame,text=option1[0],font=('arial',13,'bold'),bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2',wraplength=230, justify=LEFT)
optionButton1.place(x=60,y=95)

optionNumberB=Label(bottomFrame,text='B:',font=('arial',14),bg='black',fg='white',bd=0)
optionNumberB.place(x=320,y=100)
optionButton2=Button(bottomFrame,text=option2[0],font=('arial',13,'bold'),bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2',wraplength=230, justify=LEFT  )
optionButton2.place(x=340,y=95)

optionNumberC=Label(bottomFrame,text='C:',font=('arial',14),bg='black',fg='white',bd=0)
optionNumberC.place(x=40,y=180)
optionButton3=Button(bottomFrame,text=option3[0],font=('arial',13,'bold'),bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2',wraplength=230, justify=LEFT)
optionButton3.place(x=60,y=175)

optionNumberD=Label(bottomFrame,text='D:',font=('arial',14),bg='black',fg='white',bd=0)
optionNumberD.place(x=320,y=180)
optionButton4=Button(bottomFrame,text=option4[0],font=('arial',13,'bold'),bg='black',fg='white',bd=0,activebackground='black',
                     activeforeground='white',cursor='hand2',wraplength=230, justify=LEFT)
optionButton4.place(x=340,y=175)

optionNumber1=Label(centerFrame,text='A',font=('arial',14,'bold'),bg='black',fg='white',bd=0)

progressbarA=Progressbar(roots,orient=VERTICAL,length=120)
progressbarB=Progressbar(roots,orient=VERTICAL,length=120)
progressbarC=Progressbar(roots,orient=VERTICAL,length=120)
progressbarD=Progressbar(roots,orient=VERTICAL,length=120)

labelprogressbarA=Label(roots,font=('arial',20,'bold'),bg='black',fg='white')
labelprogressbarB=Label(roots,font=('arial',20,'bold'),bg='black',fg='white')
labelprogressbarC=Label(roots,font=('arial',20,'bold'),bg='black',fg='white')
labelprogressbarD=Label(roots,font=('arial',20,'bold'),bg='black',fg='white')
 # //this function is use to n=bind the all buttons when clicking left button

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)
lifeline50button.bind('<Button-1>',delete1)


roots.mainloop()# this function is use to hold the window on the screen