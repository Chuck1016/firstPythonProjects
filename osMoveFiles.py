import os
import fnmatch as fn
import shutil as su

path = '/home/chuck/Videos/UNSORTED/'
path18 = '/home/chuck/Videos/UNSORTED/2018/'
path19 = '/home/chuck/Videos/UNSORTED/2019/'

os.chdir(path)

for file in os.listdir(path):
    if fn.fnmatch(file, '*2018*.mp4') :
        su.move(path+file, path18+file)
    elif fn.fnmatch(file, '*2019*.mp4'):
        su.move(path+file, path19+file)
        
##      print(file)
##    It worked!!
##    Note: move() needs to be path+file to move the files. path will move the entire directory
