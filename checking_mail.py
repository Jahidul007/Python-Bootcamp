import imaplib

from imapclient import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('your email', 'your password')
conn.select_folder('INBOX', readonly=True)
UID = conn.search(['FROM', 'receiver email'])
print(UID)

rawMessage = conn.fetch([848],['BODY[]', 'FLAGS'])
print(rawMessage)



