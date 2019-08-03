from tkinter import *
from email import send_email
from tkinter import messagebox
class Switcher(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.resizable(width=False, height=False)

        Global = Frame(self, bd=1, bg='yellow')
        Global.grid()

        Header = Frame(Global, bg='yellow', bd=1, padx=5, pady=1, relief=RIDGE) #////// title space
        Header.pack(side=TOP)

        self.Header_text = Label(Header, font=('times new roman', 40, 'bold'), text="Outlook-Bot", bg='yellow')
        self.Header_text.grid()
        self._frame = None
        self.switch_frame(main)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

class main(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.configure(bg='yellow')
        

        ClickFrame = Frame(self, bd=1, width=330, height=50, padx=1, pady=1, bg='yellow', relief=RIDGE) #//// buttons space
        ClickFrame.pack(side=BOTTOM)

        Data = Frame(self, bd=1, width=300, height=400, padx=5, pady=5, relief=RIDGE, bg='yellow') #////// content space
        Data.pack(side=BOTTOM)
        
        DataLeft = LabelFrame(Data, bd=1, width=200, height=300, padx=5, pady=5, relief=RIDGE, bg='yellow', font=('arial', 20, 'bold'))
        DataLeft.pack(side=LEFT)

        

        self.user = Label(DataLeft, text='User')
        self.user.grid(row=1, column=0, sticky=W)
        self.entry_user = Entry(DataLeft, width=39)
        self.entry_user.grid(row=1, column=1)

        self.issue = Label(DataLeft, text='Issue')
        self.issue.grid(row=3, column=0, sticky=W)
        self.entry_issue = Entry(DataLeft, width=39)
        self.entry_issue.grid(row=3, column=1)

        self.Ticket = Label(DataLeft, text='Ticket')
        self.Ticket.grid(row=5, column=0, sticky=W)
        self.entry_Ticket = Entry(DataLeft, width=39)
        self.entry_Ticket.grid(row=5, column=1)


        self.labels = {self.Ticket, self.issue, self.user}
        for label in self.labels:
            label.configure(bg='red', font=('times new roman', 10, 'bold'))
        
        a = 2
        for row in range(3):
            self.space = Label(DataLeft, text="", bg='yellow')
            self.space.grid(row=a, column=1)
            a = a + 2

        #//// buttons
        self.send = Button(ClickFrame, text='Send', bg='red', width=30, command=self.mechanism)
        self.send.pack(anchor=CENTER)

        self.send2 = Button(ClickFrame, text='STRIKES', bg='green', width=30, command=lambda: master.switch_frame(Strikes))
        self.send2.pack(anchor=CENTER)


    def mechanism(self):
        user = self.entry_user.get()
        issue = self.entry_issue.get()
        body = self.entry_Ticket.get()
        entries = {self.entry_user,self.entry_Ticket,self.entry_issue}
        if user == "" or issue == "" or body == "":
            messagebox.showerror("error","fields cannot be empty")
        else:
            choice = messagebox.askyesno("Send",'Send the message?') #/// ask if user wants to send
            if choice:
                if len(body) == 10: #/// ticket length is always the same and it has 10 characters
                    try:
                        send_email().mechanism_bot(user,issue,body)
                    except: #/// if integrity error is returned (ticket appears as unique and cannot be doubled)
                        messagebox.showerror("exists",f'{body} already in database, you can strike it')
                else:
                    messagebox.showerror('error','wrong ticket provided')
            else:
                pass
        
        for item in entries:
            item.delete(0,END)
        self.entry_user.focus() #/// cursor comes back to user entry



class Strikes(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(bg='yellow')

        ClickFrame = Frame(self, bd=1, width=330, height=50, padx=1, pady=1, bg='yellow', relief=RIDGE) #//// buttons space
        ClickFrame.pack(side=BOTTOM)

        Data = Frame(self, bd=1, width=300, height=400, padx=5, pady=5, relief=RIDGE, bg='yellow') #////// content space
        Data.pack(side=BOTTOM)
        
        DataLeft = LabelFrame(Data, bd=1, width=200, height=300, padx=5, pady=5, relief=RIDGE, bg='yellow', font=('arial', 20, 'bold'))
        DataLeft.pack(side=LEFT)

        

        self.issue = Label(DataLeft, text='Ticket')
        self.issue.grid(row=1, column=0, sticky=W)
        self.entry_issue = Entry(DataLeft, width=39)
        self.entry_issue.grid(row=1, column=1)




        self.labels = {self.issue}
        for label in self.labels:
            label.configure(bg='red', font=('times new roman', 10, 'bold'))
        
        a = 2
        for row in range(3):
            self.space = Label(DataLeft, text="", bg='yellow')
            self.space.grid(row=a, column=1)
            a = a + 2

        #//// buttons
        self.send3 = Button(ClickFrame, text='GIVE STRIKE', bg='red', width=30, command=self.send_strike)
        self.send3.pack(anchor=CENTER)
        self.send2 = Button(ClickFrame, text='BACK', bg='green', width=30, command=lambda: master.switch_frame(main))
        self.send2.pack(anchor=CENTER)
        
    def send_strike(self):
        ticket = self.entry_issue.get()
        if ticket == "":
            messagebox.showerror('empty','box cannot be empty')
        
        else:
            if len(ticket) == 10:
                if ticket[:3] == "INC":
                    send_email().reply(ticket)
                else:
                    messagebox.showerror('INC','TICKET should start from INC')
            else:
                messagebox.showerror('error',f'TICKET length should be 10 not {len(ticket)}')

