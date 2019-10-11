##  From the Corey Schafer YouTube video: Python Tutorial: Automate Parsing and Renaming of Multiple Files
##  Break down a file name into variables, then rearange them and rename the file.
##  original test files were in this format: 20190712_IMG073803545.jpg

import os 

os.chdir('/home/chuck/Python/TestFiles')

for f in os.listdir():
    fName, fExt = os.path.splitext(f)  # separate file name from extension
    
    fDate, fNum = fName.split('_')  # separate date from image number
    
    fNum = fNum.strip()[3:]   # remove 'IMG' from the number
    year = fDate[:4]        # break date into parts
    month = fDate[4:6]
    day = fDate[6:]
    
    newFileName = '{}_{}_{}_{}{}'.format(month, day, year, fNum, fExt)  # reorder variables using {place holders}
    print(newFileName)
##  os.rename(f, newFileName)
