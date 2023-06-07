# ver1.0
# before running
# pip install librosa, shutil

import os
import librosa
#import shutil

import xlsxwriter
 
workbook = xlsxwriter.Workbook('Sampo.xlsx')

worksheet = workbook.add_worksheet()

dire = r"C:\users\gambi\sampo\sampo"

#oneshot = "W:\Samples\MoveThemTunes\oneshot"
#loop = "W:\Samples\MoveThemTunes\loop"
directory = os.fsencode(dire)
count = 0

for subdir, dirs, files in os.walk(dire):
    for file in files:
        fullpath = os.path.join(subdir, file)
        ##print(fullpath)
        if file.endswith(".wav"):
            dur = librosa.get_duration(path = fullpath)
            print(dur)
            count = count+1
            cola = "A"+str(count)
            colb = "B"+str(count)
            colc = "C"+str(count)
            cold = "D"+str(count)
            cole = "E"+str(count)
            if (dur < 1):
                ##shutil.move(fullpath, os.path.join(oneshot,file))
                if("snare" in fullpath.lower()):
                    print ("snare")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'snare') 
                    worksheet.write(colc, 'one-shot')
                    worksheet.write(cold, dur)
                elif("hat" in fullpath.lower()):
                    print ("hat")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'hat') 
                    worksheet.write(colc, 'one-shot')
                    worksheet.write(cold, dur)
                elif("bass" in fullpath or "synth" in fullpath.lower()):
                    print ("bass")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'bass') 
                    worksheet.write(colc, 'one-shot')
                    worksheet.write(cold, dur)
                elif("vocal" in fullpath.lower()):
                    print ("vocal")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'vocal') 
                    worksheet.write(colc, 'one-shot')
                    worksheet.write(cold, dur)
                else: 
                    print("uncategorized")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'uncategorized') 
                    worksheet.write(colc, 'one-shot')
                    worksheet.write(cold, dur)
            else:
                ##shutil.move(fullpath, os.path.join(oneshot,file))
                if("drum" in fullpath.lower()):
                    print ("drum")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'drum') 
                    worksheet.write(colc, 'loop')
                    worksheet.write(cold, dur)
                elif("vocal" in fullpath.lower()):
                    print ("vocal")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'vocal') 
                    worksheet.write(colc, 'loop')
                    worksheet.write(cold, dur)
                elif("bass" in fullpath or "synth" in fullpath.lower()):
                    print ("bass")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'bass') 
                    worksheet.write(colc, 'loop')
                    worksheet.write(cold, dur)
                elif("arp" in fullpath.lower()):
                    print ("arp")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'arp') 
                    worksheet.write(colc, 'loop')
                    worksheet.write(cold, dur)
                else:
                    print("uncategorized")
                    worksheet.write(cola, fullpath)
                    worksheet.write(colb, 'uncategorized') 
                    worksheet.write(colc, 'loop')
                    worksheet.write(cold, dur)
            print('totals: ', count)
workbook.close()
#for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     if filename.endswith(".wav"): 
#         fullpath = os.path.join(dire, filename)
#         dur = librosa.get_duration(path = fullpath)
#         print (dur)
#         continue
#     else:
#         continue
#drum
#synth, arpeggio, melody, rhode, arp
#bass
#vocal
