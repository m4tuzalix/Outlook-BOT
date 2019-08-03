# Outlook-BOT


This is the outlook bot to send messages thru outlook, to particular receiver, with particulat subject and message. 
The main reason it has been created is automatization of work where a lot of emails or reminders must be send.

Receiver entry field checks the outlook AddressBook, so you can provide either name, email or id of user - It will compare 
with existing data in AB and then assign the message to concrete user.

As mentioned above, program is to automatizate the taska so the message template is up-given. Anyway it can be rebuild if neccessary.


Reminder function is on of the most functional in my opinion. Bot sends reminders according to provided ticket ID (In my particular case).
There are 3 possible reminders to give with 2 days break after each, so for instance from Monday to Friday. Third reminder means
ticket can be closed as user has not respond.

According to provided ticket, script checks if any reminder has already been given or if at least 2 days have passed before giving another reminder.


Some features still need to be improved, but bot is usable and works as intended.

