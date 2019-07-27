import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.ehlo()

conn.login('your_email', 'your_password')

conn.sendmail('your maiil', 'receiver_mail', 'type your message')

conn.quit()