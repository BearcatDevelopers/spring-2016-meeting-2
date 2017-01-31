from secret import gmailPassword
import smtplib

# Static variables
myEmail = 'bearcatdevelopers@gmail.com'
myPassword = gmailPassword # or put password as a string here

# Dynamic inputs for python 3
sendToEmail = input('Who do you want to send an email to? \n')
msg = input('What do you want to say? \n')

# sign in to gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, myPassword)

# send the email
server.sendmail(myEmail, sendToEmail, msg)

# exit
server.quit()

print('\nEmail Sent!\n')