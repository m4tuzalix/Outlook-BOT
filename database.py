import sqlite3
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta

def main():
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mails(id INTEGER PRIMARY KEY, user TEXT, ticket TEXT UNIQUE, date TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS strikes(id PRIMARY KEY, ticketID INTEGER, first TEXT, second TEXT, third TEXT, FOREIGN KEY (ticketID) REFERENCES mails(id))")
    con.commit()
    con.close

def add(user, ticket, date):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute("INSERT INTO mails VALUES (NULL,?,?,?)", (user,ticket,date))
    cur.execute("INSERT INTO strikes VALUES (NULL,(SELECT id FROM mails WHERE ticket=?),?,?,?)", (ticket,"0","0","0"))
    con.commit()
    con.close()

def get_user_data(ticket):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM mails WHERE ticket=?", (ticket,))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def give_strike(ticket,data):
    send = None
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM mails WHERE ticket=?", (ticket,))
    if cur.fetchone():
        cur.execute("SELECT * FROM strikes WHERE ticketID=(SELECT id FROM mails WHERE ticket=?)", (ticket,))
        for item in cur.fetchall(): #/// checks all rows for given user
            if item[2] == "0": #/// if first reminder value is 0 then reminds
                cur.execute("UPDATE strikes SET first=? WHERE ticketID=(SELECT id FROM mails WHERE ticket=?)",(data,ticket))
                send = "1st"
                break
                  
            else: #// if first reminder has been detected, then iterates further
                date_s1 = datetime.strptime(item[2], '%Y-%m-%d')
                if item[3] == "0" and datetime.now() >= date_s1 + timedelta(days=2): #// if second reminder value is 0 and at least 2 days have passed, then gives second remind
                    cur.execute("UPDATE strikes SET second=? WHERE ticketID=(SELECT id FROM mails WHERE ticket=?)",(data,ticket))
                    send = "2nd"
                    break
                    

                elif item[3] != "0" and item[4] == "0": #// if second reminder has been given and third one value is 0, then proceeding
                    date_s2 = datetime.strptime(item[3], '%Y-%m-%d')
                    if datetime.now() >= date_s2 + timedelta(days=2): #/// if at least two days have passed, then gives last reminder
                        cur.execute("UPDATE strikes SET third=? WHERE ticketID=(SELECT id FROM mails WHERE ticket=?)",(data,ticket))
                        send = "3rd"
                        messagebox.showinfo('3 strikes detected','Ticket has been stroke 3x, you can close it')
                        break
                
                    else:
                        messagebox.showerror('third','2 days have not passed yet') #/// two days haven't passed
                        break


                elif item[4] != "0":
                    messagebox.showinfo('3 strikes detected','Ticket has been stroke 3x, you can close it')
                    break

                else: #/// if 2 days haven't passed from first reminder, then second remind cannot be given
                    messagebox.showerror('second','2 days have not passed yet')
                    break
    
    con.commit()
    con.close()
    return send
main()
