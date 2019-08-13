import win32com.client
from database import main,add,get_user_data,give_strike,strike_reset
from datetime import datetime
from tkinter import messagebox



class Send_email:
    def __init__(self):
        self.time = datetime.now().strftime('%Y-%m-%d')
        pass
    
    def mechanism_bot(self,user,sub,mes):
        self.user = user
        self.sub = sub
        self.mes = mes
        
        search_string = self.user

        outlook = win32com.client.gencache.EnsureDispatch('Outlook.Application')
        recipient = outlook.Session.CreateRecipient(search_string)
        recipient.Resolve()
        
        
        Address = recipient.AddressEntry
        email_address = None

        if 'EX' == Address.Type:
            eu = Address.GetExchangeUser()
            email_address = eu.PrimarySmtpAddress

        if 'SMTP' == Address.Type:
            email_address = Address.Address


        name_container = [f'{recipient.Name}']
        name_final = []
        for n in name_container:
            final = n.split()
            if final[-1] == "(IBM)" or final[-1] == "(TCS)":
                final[-1] = final[1]
            name_final.append(final[-1])

        
        
        Msg = outlook.CreateItem(0)
        Msg.To = f'{email_address}'
        Msg.Subject = f'{self.mes} - {self.sub}'
        Msg.GetInspector
        message = f'<div>Hello {name_final[0].title()},<br></br> <br></br> I got your ticket <span style="text-transform: uppercase; font-style: italic; "><strong>{self.mes}</strong></span>. Please let me know when you are available to let me fix this issue</div>'
        
        index = Msg.HTMLBody.find('>', Msg.HTMLBody.find('<body')) 
        Msg.HTMLBody = Msg.HTMLBody[:index + 1] + message + Msg.HTMLBody[index + 1:] 

   
        database = add(email_address, self.mes, self.time)
        if database is None:
            Msg.Send()
        else:
            messagebox.showerror("error","Ticket already in database!")
        
        
        
        
        
    
    def reply(self,sub): #//// sub is ticket
        if not get_user_data(sub):
            messagebox.showerror('Not found',"User has not been conntacted regarding this ticket, please send the email first")
        else:
            self.sub = sub
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") # to trigger outlook application
            inbox = outlook.GetDefaultFolder(5) # send items
            messages = inbox.Items  
            messages.Sort("[ReceivedTime]", True)
            message = messages.GetFirst()# message is treated as each mail in for loop 
            founded = False

            user_answer_check = outlook.GetDefaultFolder(6)
            checker = user_answer_check.Items
            checker.Sort("[ReceivedTime]", True)
            check = checker.GetFirst()

            for message, check in zip(messages,checker):
                if self.sub in check.Subject and check.UnRead == True:
                    messagebox.showerror('answered', "Found unread message regarding this ticket, reseting the strikes to 0")
                    strike_reset(self.sub)
                    break
                else:
                    for rows in get_user_data(self.sub):                                       
                        if rows[2] in message.Subject: # based on the subject replying to email 
                            reply = message.Reply() 
                            reply.To = rows[1]
                            founded = True #///// iterates over all messages and checks the subject. If found, then returns True. 
                            break
                        
                    if founded: #///// if founded at least one match, then breaks the loop
                        a = give_strike(self.sub,self.time) #//// this function returns variable SEND which value by default is NONE
                        if a is not None:
                            try:
                                strikes = ['1st','2nd','3rd'] #/// if SEND variable returns any strike, then the returned strike is given
                                for strike in strikes:
                                    if a == strike:
                                        msg = f'{strike} strike <br></br> Today, we have tried to contact you, concerning your ticket <span style="text-transform: uppercase; font-style: italic; "><strong>{self.sub}.</strong></span> <br></br> Please contact us to make an appointment to solve the issue.'
                                        index = reply.HTMLBody.find('>', reply.HTMLBody.find('<body')) 
                                        reply.HTMLBody = reply.HTMLBody[:index + 1] + msg + reply.HTMLBody[index + 1:] 
                                        reply.Send()
                            except ValueError as e: 
                                print("Something went wrong "+str(e))
                                break
                            else:
                                break
                        break
                            
                        
                    else: #///// if not then continues the itteration
                        continue
                    


            
            
                
                    
               
        
       