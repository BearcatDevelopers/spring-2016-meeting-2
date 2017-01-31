from secret import gmailPassword
import smtplib

# Static variables
myEmail = 'bearcatdevelopers@gmail.com'
myPassword = gmailPassword # or put password as a string here

# Static inputs for python 3
sendToEmail = 'rhyneav@gmail.com'
msg = """

Hey, how's it going?!

"""

# sign in to gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myEmail, myPassword)

# send the email
server.sendmail(myEmail, sendToEmail, msg)

# exit
server.quit()

print('\nEmail Sent!\n')