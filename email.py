import win32com.client
from database import main,add,get_user_data,give_strike
from datetime import datetime



class send_email():
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
            name_final.append(final[-1])
        
        
        Msg = outlook.CreateItem(0)


        Msg.To = f'{email_address}'
        Msg.Subject = f'{self.mes} - {self.sub}'
        Msg.HTMLBody = f'<div>Hello {name_final[0].title()},<br></br> <br></br> I got your ticket <span style="text-transform: uppercase; font-style: italic; "><strong>{self.mes}.</strong></span>, please let me know when you are available to let me fix this issue<div style="padding: 15px; margin: 5px;"><h1 style="color: red;">Engineer</h1><h2 style="color: green; font-size: 10px;">CTS TEAM</h2></div></div>'

        add(email_address, self.mes, self.time)

        Msg.Send()
    
    def reply(self,sub):
        self.sub = sub
        outlook =win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") # to trigger outlook application
        inbox = outlook.GetDefaultFolder(5) # send items
        messages = inbox.Items  
        message = messages.GetFirst()# message is treated as each mail in for loop 
        founded = False
        for message in messages:
            for rows in get_user_data(self.sub):                                       
                if rows[2] in message.Subject: # based on the subject replying to email 
                    reply = message.Reply() 
                    reply.To = rows[1]
                    reply.Body = "tak"
                    founded = True #///// iterates over all messages and checks the subject. If found, then returns True. 
                    break
                
            if founded: #///// if founded at least one match, then breaks the loop
                a = give_strike(self.sub,self.time) #//// this function returns variable SEND which value by default is NONE
                if a is not None:
                    try:
                        strikes = ['1st','2nd','3rd'] #/// if SEND variable returns any strike, then the returned strike is given
                        for strike in strikes:
                            if a == strike:
                                reply.HTMLBody = f'{strike} strike <br></br> Today, we have tried to contact you, concerning your ticket <span style="text-transform: uppercase; font-style: italic; "><strong>{self.sub}.</strong></span> <br></br> Please contact us to make an appointment to solve the issue.'
                                reply.Send()
                    except ValueError as e: 
                        print("Something went wrong "+str(e))
                        break
                    else:
                        break
                break
                    
                
            else: #///// if not then continues the itteration
                continue
                    


            
            
                
                    
               
        
       