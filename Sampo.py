# ver1.0
# before running
# pip install librosa, shutil

import os
import librosa
#import shutil

import xlsxwriter
 
workbook = xlsxwriter.Workbook('Sampo.xlsx')

worksheet = workbook.add_worksheet()
cwd = os.getcwd()
#dire = r"C:\users\gambi\sampo\sampo"
dire = cwd

#oneshot = "W:\Samples\MoveThemTunes\oneshot"
#loop = "W:\Samples\MoveThemTunes\loop"
directory = os.fsencode(dire)
count = 0
for subdir, dirs, files in os.walk(dire):
    for file in files:
        type = "none"
        category = "none"
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
            if (dur < 2.2):
                type = "oneshot"
                ##shutil.move(fullpath, os.path.join(oneshot,file))
            else:
                type = "loop"
                ##shutil.move(fullpath, os.path.join(oneshot,file))
            if("drum" in file.lower()):
                    print ("drum")
                    category = "drum"
            elif("snare" in file.lower()):
                    print ("snare")
                    category = "snare"
            elif("kick" in file.lower()):
                    print ("kick")
                    category = "kick"
            elif("guitar" in file.lower()):
                    print ("kick")
                    category = "kick"
            elif("phrase" in file.lower()):
                    print ("phrase")
                    category = "phrase"
            elif("clap" in file.lower()):
                    print ("clap")
                    category = "clap"
            elif("hat" in file.lower()):
                    category = "hat"
            elif("bass" in file.lower()):
                    category = "bass"
            elif("percu" in file.lower()):
                    print ("percussion")
                    category = "percussion"
            elif("vocal" in file.lower()):
                    print ("vocal")
                    category = "vocal"
            elif("synth" in file.lower()):
                    print ("synth")
                    category = "synth"
            elif("pad" in file.lower()):
                    print ("pad")
                    category = "pad"
            elif("lead" in file.lower()):
                    print ("lead")
                    category = "lead"
            elif("arp" in file.lower()):
                    category = "arp"
            elif ("chord" in file.lower()):
                    category = "chord"
            elif ("riser" in file.lower() or "uplifter" in file.lower()):
                    print ("riser")
                    category = "riser"
            elif ("downer" in file.lower() or "downlifter" in file.lower()):
                    print ("downlifter")
                    category = "downlifter"
            elif ("sweep" in file.lower()):
                    print ("sweep")
                    category = "sweep"
            elif ("piano" in file.lower()):
                    print ("piano")
                    category = "piano"
            else: 
                    print("uncategorized")
            worksheet.write(cola, fullpath)
            worksheet.write(colb, category) 
            worksheet.write(colc, type)
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
