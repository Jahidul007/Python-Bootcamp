import re
def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
message = 'call me 415-555-1234 tomorrow, or at 415-555-9999 for my office line'

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could no find any phone number')
#print(isPhoneNumber('415-555-1234'))


phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumber.findall(message)
#mo = phoneNumber.search(message)
#print(mo.group())
print(mo)
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneNumber.search(message).group(2))

batRegex = re.compile(r'Bat(mobile|man|copter|bat)')

mo = batRegex.search('Batmobile lost a wheel')
#mo = batRegex.search('Batmotor lost a wheel')
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('the adventures of Batman')

print(mo.group())

# exactly repeating

haRegex = re.compile(r'(Ha){3}')

ha = haRegex.search('jakjhg  jdfhjh HaHaHa')
print(ha.group())


phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phn = phoneRegex.findall('aksdflkjslkdf 444-444-4444 444-444-6666 lksdflkjlsakdf 444-444-6666')
print(phn)


# vowel regex

vowelRegex = re.compile(r'[aeiouAEIOU]')
vr = vowelRegex.findall('Hamid hasan is a good boy but not talent.')

print(vr)





