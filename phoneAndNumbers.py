#!/user/bin/python

#phoneAndEmail.py-Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)?         #separator
    (\d{3})            #first 3 digit
    (\s|-|\.)          #seperator
    (\d{4})            #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
    )''',re.VERBOSE)

emailRegex=re.compile(r'''(
      [a-zA-Z0-9._%+-]+ #username
      @                 #@symbol
      [a-zA-Z0-9.-]+    #domain name
      (\.[a-zA-Z]{2,4}) #dot-something
      )''',re.VERBOSE)


      
#Find matches in clipboard text
#text =str(pyperclip.paste())
file=input("Enter the name of File:")
fd=open(file)
lines=str(fd.readlines())
matches=[]
for groups in phoneRegex.findall(lines):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(lines):
    matches.append(groups)

for i in range(len(matches)):
    print(matches[i])
#if len(matches) > 0:
    #pyperclip.copy('\n'.join(matches))
   # pyperclip.copy(matches)
   # print('Copied to clipboard:')
   # print(matches)

else:
    print('No phone numbers or email address found.')

                      
