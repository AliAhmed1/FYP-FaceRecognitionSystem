import yagmail
import getpass

pswd = getpass.getpass('Password:')

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='saliahmed11111@gmail.com', password=pswd)
    #sending the email
    yag.send(to='saadalam996@gmail.com', subject='Testing Yagmail', contents='Hurray, it worked!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")