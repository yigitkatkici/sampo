import os
import librosa
#import shutil
import csv

dire = "W:\Samples\MoveThemTunes\Splice\Samples\packs"
oneshot = "W:\Samples\MoveThemTunes\oneshot"
loop = "W:\Samples\MoveThemTunes\loop"
directory = os.fsencode(dire)
count = 0

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for subdir, dirs, files in os.walk(dire):
         for file in files:
            fullpath = os.path.join(subdir, file)
            print(fullpath)
            if file.endswith(".wav"):
                dur = librosa.get_duration(path = fullpath)
                print(dur)
                count = count+1
                if (dur < 1):
                    ##shutil.move(fullpath, os.path.join(oneshot,file))
                    if("snare" in fullpath.lower()):
                        print ("snare")
                    if("hat" in fullpath.lower()):
                        print ("hat")
                    if("bass" in fullpath or "synth" in fullpath.lower()):
                        print ("bass")
                    if("vocal" in fullpath.lower()):
                        print ("vocal")
                else:
                    ##shutil.move(fullpath, os.path.join(oneshot,file))
                    if("drum" in fullpath.lower()):
                        print ("drum")
                    if("vocal" in fullpath.lower()):
                        print ("vocal")
                    if("bass" in fullpath or "synth" in fullpath.lower()):
                        print ("drum")
                    if("arp" in fullpath.lower()):
                        print ("arp")
            print('totals: ', count)

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
