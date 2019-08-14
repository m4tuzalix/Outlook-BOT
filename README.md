# Outlook-BOT
Bot to send emails and reminders

I have created this bot to automatize daily, monotonous process of sending emails and reminders to users (I'm working on 2nd support line).


1. Bot sends email to given user (email address, name, id, other things associated with particular person - data is taken straight from exchange)
2. Bot creates own database where all information regarding emails/reminders are stored. INCIDENT NUMBER is UNIQUE and works as a second PK
3. Bot checks if:
  - User has already been contacted (If incident ID is already in DB, then bot throws an info message)
  - At least two days between reminders have passed (if not, then reminder won't be send and bot will throw a message)
  - User has answered on reminder (Basing on unread mails with INCIDENT number in it. If user answers, then reminders are reset to 0)

As a second line engineer, I'm documenting resolved incidents in excel file and also included this part in my bot. At the first use
bot asks for path to folder where excel files are stored.

4. According to above, bot always picks the latest created file (sorted by date) and iterates thru all available rows/columns.
  If particular incident number present in DB is deteced in excel file, then DB deletes it.
  

BOT is fully automatized - checks everything and cleans DB itself. This program has decently improved performance of my work as I've started
to save a lot of time which before I had to spent to send dosens of emails/reminders.

To give the real facts.. To send first email or reminder it was taking me aprox 15-20 seconds, to fill the neccesary data and send it. 

BOT TAKES aprox. 3-4 seconds to send the email and 2 seconds to send the reminder. The difference is huge :)
