#! python 3
#renameDates.py
#to European

import shutil,os,re

datePattern=re.compile(r"""^(.*?) # all text before the date
     ((0|1)?\d)-       #one or two digits for the month
     ((0|1|2|3)?\d)-   # one or two digits for the day
     ((19|20)\d\d)    #four digits for the year
     (.*?)$            #att text after the date
     """,re.VERBOSE)

#loop over the files in the working directory     
for amerFilename in os.listdir ('E:\\Python Material\\Practice'):
    mo=datePattern.search(amerFilename)

#Skip files without a date
    if mo==None:
        continue

#Get the different parts of the filename
    print(mo.groups())
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)

#Form the European-Style filename.
    euroFilename= beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

#Get the full ,absoulte file paths.
    absWorkingDir=os.path.abspath('E:\\Python Material\\Practice')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)

    print('Renaming "%s" to "%s"...'%(amerFilename,euroFilename))
    shutil.move(amerFilename,euroFilename)
    
