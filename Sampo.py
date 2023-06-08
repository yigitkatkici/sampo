# ver1.0
# before running
# pip install librosa, shutil

import os
import librosa
#import shutil
import re

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
        tempo = 0
        fullpath = os.path.join(subdir, file)
        ##print(fullpath)
        numbers = re.findall(r'\d+', file)
        if(len(numbers) >0):
            print("tempo listed")
            print (numbers[0])
            for x in numbers:
                if int(x) > 40:
                    tempo = x
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
            elif("perc" in file.lower()):
                print ("percussion")
                category = "percussion"
            elif("vocal" in file.lower()):
                print ("vocal")
                category = "vocal"
            elif("synth" in file.lower() or "syn" in file.lower()):
                print ("synth")
                category = "synth"
            elif("pad" in file.lower()):
                print ("pad")
                category = "pad"
            elif("lead" in file.lower()):
                print ("lead")
                category = "lead"
            elif("arp" in file.lower()):
                print ("arp")
                category = "arp"
            elif ("chord" in file.lower()):
                print ("chord")
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
            elif ("stab" in file.lower()):
                print ("stab")
                category = "stab"
            elif ("strum" in file.lower()):
                print ("strum")
                category = "stab"
            elif ("piano" in file.lower() or "rhodes" in file.lower()  or "clav" in file.lower()):
                print ("piano")
                category = "piano"
            elif ("horn" in file.lower()):
                print ("horn")
                category = "horn"
            elif ("flute" in file.lower()):
                print ("flute")
                category = "flute"
            elif ("violin" in file.lower()):
                print ("violin")
                category = "violin"
            elif ("choir" in file.lower()):
                print ("choir")
                category = "choir"
            elif ("gtr" in file.lower() or "lick" in file.lower() or "elec" in file.lower() or "pluck" in file.lower() or "strum" in file.lower()):
                print ("gtr")
                category = "guitar"
            elif ("tom" in file.lower()):
                print ("tom")
                category = "tom"
            elif ("shaker" in file.lower()):
                print ("shaker")
                category = "shaker"
            elif ("vox" in file.lower() or "voc" in file.lower()):
                print ("voc")
                category = "voc"
            elif ("bong" in file.lower()):
                print ("bong")
                category = "bong"
            elif ("foley" in file.lower()):
                print ("foley")
                category = "foley"
            elif ("cello" in file.lower()):
                print ("cello")
                category = "cello"
            elif ("viola" in file.lower()):
                print ("viola")
                category = "viola"
            elif ("chorus" in file.lower()):
                print ("chorus")
                category = "chorus"
            elif ("melod" in file.lower()):
                print ("melody")
                category = "melody"
            elif ("SUB" in file.lower()):
                print ("SUB")
                category = "BASS"
            elif ("fx" in file.lower()):
                print ("fx")
                category = "fx"
            elif ("bell" in file.lower()):
                print ("bell")
                category = "bell"
            elif ("combi" in file.lower() or "combo" in file.lower()):
                print ("combo")
                category = "combo"
            elif ("downshifter" in file.lower()):
                print ("downshifter")
                category = "downshifter"
            elif ("tambourine" in file.lower()):
                print ("tambourine")
                category = "tambourine"
            elif ("mallet" in file.lower()):
                print ("mallet")
                category = "mallet"
            elif ("strings" in file.lower()):
                print ("strings")
                category = "strings"
            elif ("sitar" in file.lower()):
                print ("sitar")
                category = "sitar"
            elif ("hook" in file.lower()):
                print ("hook")
                category = "hook"
            elif ("crash" in file.lower()):
                print ("crash")
                category = "crash"
            elif ("bleep" in file.lower()):
                print ("bleep")
                category = "bleep"
            elif ("ambiance" in file.lower()):
                print ("ambiance")
                category = "ambiance"
            else:
                print("uncategorized")
                category = "uncategorized"
            worksheet.write(cola, fullpath)
            worksheet.write(colb, category) 
            worksheet.write(colc, type)
            worksheet.write(cold, dur)
            worksheet.write(cole, tempo)
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
