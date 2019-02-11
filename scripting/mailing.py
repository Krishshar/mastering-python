import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr = "soulking1623@gmail.com"
to_addr = "singhakku7700@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = from_addr

# storing the receivers email address
msg['To'] = to_addr

# storing the subject
msg['Subject'] = 'Bee I sent this message using code!'

# string to store the body of the mail
body = "This the body of the mail!!!!"

# attach to store the body of the mail
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "mailing.py"
attachment = open("C:\Users\Codeghoul\Desktop\Folders\Python\mastering-python\scripting", "r")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

#encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

#attach the instance 'p' instance 'msg'
msg.attach(p)

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(' soulking1623@gmail.com ', "p[l;,./']" )

smtp_obj.sendmail("soulking1623@gmail.com", "ashishekka329@gmail.com", msg)
smtp_obj.quit()