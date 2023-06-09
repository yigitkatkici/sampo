import os
import librosa
import shutil
import re

import xlsxwriter
 
workbook = xlsxwriter.Workbook('Sampo.xlsx')

worksheet = workbook.add_worksheet()
cwd = os.getcwd()
#dire = r"C:\users\gambi\sampo\sampo"
dire = cwd

oneshot = cwd+"\oneshot\\"
loop = cwd+"\loop\\"
directory = os.fsencode(dire)
count = 0
for subdir, dirs, files in os.walk(dire):
    for file in files:
        fullpath = os.path.join(subdir, file)
        destination = loop+file
        if ("wav" in file):
            shutil.move(fullpath, destination)
            print(fullpath)
            print (destination)