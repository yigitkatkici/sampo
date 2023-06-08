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
        key = "none"
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
            colf = "F"+str(count)

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
            ##KEY
            if("_f_" in file.lower() or "f_major" in file.lower() or "f_maj" in file.lower()):
                print ("F major")
                key = "_F_major"
            elif("_g_" in file.lower() or "g_major" in file.lower() or "g_maj" in file.lower()):
                print ("G major")
                key = "_G_major"
            elif("_a_" in file.lower() or "a_major" in file.lower() or "a_maj" in file.lower()):
                print ("A major")
                key = "_A_major"
            elif("_b_" in file.lower() or "b_major" in file.lower() or "b_maj" in file.lower()):
                print ("B major")
                key = "_B_major"
            elif("_c_" in file.lower() or"c_major" in file.lower() or "c_maj" in file.lower()):
                print ("C major")
                key = "_C_major"
            elif("_d_" in file.lower() or"d_major" in file.lower() or "d_maj" in file.lower()):
                print ("D major")
                key = "_D_major"
            elif("_e_" in file.lower() or "e_major" in file.lower() or "e_maj" in file.lower()):
                print ("E major")
                key = "_E_major"
            #minors
            elif("fm" in file.lower() or "f_minor" in file.lower() or "f_min" in file.lower() or "fmin" in file.lower()):
                print ("F minor")
                key = "_F_minor"
            elif("gm" in file.lower() or "g_minor" in file.lower() or "g_min" in file.lower() or "gmin" in file.lower()):
                print ("G minor")
                key = "_G_minor"
            elif("am" in file.lower() or "a_minor" in file.lower() or "a_min" in file.lower() or "amin" in file.lower()):
                print ("A minor")
                key = "_A_minor"
            elif("bm" in file.lower() or "b_minor" in file.lower() or "b_min" in file.lower()) or "bmin" in file.lower():
                print ("B minor")
                key = "_B_minor"
            elif("cm" in file.lower() or "c_minor" in file.lower() or "c_min" in file.lower() or "cmin" in file.lower()):
                print ("C minor")
                key = "_C_minor"
            elif("dm" in file.lower() or "d_minor" in file.lower() or "d_min" in file.lower() or "dmin" in file.lower()):
                print ("D minor")
                key = "_D_major"
            elif("em" in file.lower() or "e_minor" in file.lower() or "e_min" in file.lower()) or "emin" in file.lower():
                print ("E minor")
                key = "_E_minor"
            #sharps
            elif("f#" in file.lower()):
                print ("F sharp")
                key = "_F_sharp"
            elif("g#" in file.lower()):
                print ("G sharp")
                key = "_G_sharp"
            elif("a#" in file.lower()):
                print ("A sharp")
                key = "_A_sharp"
            elif("b#" in file.lower()):
                print ("B sharp")
                key = "_B_sharp"
            elif("c#" in file.lower()):
                print ("C sharp")
                key = "_C_sharp"
            elif("d#" in file.lower()):
                print ("D sharp")
                key = "_D_sharp"
            elif("e#" in file.lower()):
                print ("E sharp")
                key = "_E_sharp"

            elif("f#m" in file.lower()):
                print ("F sharp minor")
                key = "_F_sharp_minor"
            elif("g#m" in file.lower()):
                print ("G sharp minor")
                key = "_G_sharp_minor"
            elif("a#m" in file.lower()):
                print ("A sharp minor")
                key = "_A_sharp_minor"
            elif("b#m" in file.lower()):
                print ("B sharp minor")
                key = "_B_sharp_minor"
            elif("c#m" in file.lower()):
                print ("C sharp minor")
                key = "_C_sharp_minor"
            elif("d#m" in file.lower()):
                print ("D sharp minor")
                key = "_D_sharp_minor"
            elif("e#m" in file.lower()):
                print ("E sharp minor")
                key = "_E_sharp_minor"
            elif("f#" in file.lower()):
                print ("F sharp")
                key = "_F_sharp"
            elif("g#" in file.lower()):
                print ("G sharp")
                key = "_G_sharp"
            elif("a#" in file.lower()):
                print ("A sharp")
                key = "_A_sharp"
            elif("b#" in file.lower()):
                print ("B sharp")
                key = "_B_sharp"
            elif("c#" in file.lower()):
                print ("C sharp")
                key = "_C_sharp"
            elif("d#" in file.lower()):
                print ("D sharp")
                key = "_D_sharp"
            elif("e#" in file.lower()):
                print ("E sharp")
                key = "_E_sharp"
            #Flats
            elif("fb" in file.lower()):
                print ("F flat minor")
                key = "_F_flat_minor"
            elif("gb" in file.lower()):
                print ("G flat minor")
                key = "_G_flat_minor"
            elif("ab" in file.lower()):
                print ("A flat minor")
                key = "_A_flat_minor"
            elif("bb" in file.lower()):
                print ("B flat minor")
                key = "_B_flat_minor"
            elif("cb" in file.lower()):
                print ("C flat minor")
                key = "_C_flat_minor"
            elif("db" in file.lower()):
                print ("D flat minor")
                key = "_D_flat_minor"
            elif("eb" in file.lower()):
                print ("E flat minor")
                key = "_E_flat_minor"

            elif("fbm" in file.lower()):
                print ("F flat minor")
                key = "_F_flat_minor"
            elif("gbm" in file.lower()):
                print ("G f;at minor")
                key = "_G_flat_minor"
            elif("abm" in file.lower()):
                print ("A flat minor")
                key = "_A_flat_minor"
            elif("bbm" in file.lower()):
                print ("B flat minor")
                key = "_B_flat_minor"
            elif("cbm" in file.lower()):
                print ("C flat minor")
                key = "_C_flat_minor"
            elif("dbm" in file.lower()):
                print ("D flat minor")
                key = "_D_flat_minor"
            elif("ebm" in file.lower()):
                print ("E flat minor")
                key = "_E_flat_minor"
            
            else:
                print ("Key not found")
                key = "uncategorized"
            worksheet.write(cola, fullpath)
            worksheet.write(colb, category) 
            worksheet.write(colc, type)
            worksheet.write(cold, dur)
            worksheet.write(cole, tempo)
            worksheet.write(colf, key)
            print('totals: ', count)
workbook.close()
"""
Exclusive            
_F_
_G_
_A_
_B_
_C_
_D_
_E_

_F
_G
_A
_B
_C
_D
_E

f_major
g_major
a_major
b_major
c_major
d_major
e_major

Fmaj
Gmaj
Amaj
Bmaj
Cmaj
Dmaj
Emaj

minors
Fm
Gm
Am
Bm
Cm
Dm
Em

f_minor
g_minor
a_minor
b_minor
c_minor
d_minor
e_minor

Fmin
Gmin
Amin
Bmin
Cmin
Dmin
Emin

Sharps
F#m
G#m
A#m
B#m
C#m
D#m
E#m

F#
G#
A#
B#
C#
D#
E#

flat minors
fbm
gbm
abm
bbm
cbm
dbm
ebm

flat majors
fb
gb
ab
bb
cb
db
eb
"""


            
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
