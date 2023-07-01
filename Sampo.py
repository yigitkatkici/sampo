# ver1.0
# before running
# pip install librosa, shutil

import os
import librosa
import shutil
import re
import xlsxwriter
#import sys


workbook = xlsxwriter.Workbook('Sampo.xlsx')
worksheet = workbook.add_worksheet()
cwd = os.getcwd()
#dire = r"C:\users\gambi\sampo\sampo"
dire = cwd
move = False
validprompt = 0
oneshot = cwd+"\oneshot"
loop = cwd+"\loop"
scan = False
moveType = False
moveCategory = False
moveTempo = False
moveNote = False
justScan = True

while move == False:
    print("Welcome to Sampo, no frills sample analizer.")
    type = input("would you like Sampo to arrange your samples as loop and one shot? YES OR NO ")
    tempo = input("would you like Sampo to arrange your samples by tempo? YES or NO ")
    note = input("would you like Sampo to arrange your samples by note? YES or NO ")
    category = input("would you like Sampo to arrange your samples by category? YES or NO ")
    invalid = False
    ##exitsentence = "your samples will be arranged by:"
    if type == "YES":
        print ("Your loops will be arranged as loop and one shot. ")
        validprompt = validprompt+1
        moveType = True
    elif type == "NO":
        print ("Your loops will not be arranged by loop one shot. ")
    else:
        print(type)
        print (" is not a valid prompt")
        invalid = True
    if tempo == "YES":
        print ("Your loops will be arranged by tempo. ")
        validprompt = validprompt+1
        moveTempo = True
    elif tempo == "NO":
        print ("Your loops will not be arranged by Tempo. ")
    else:
        print(tempo)
        print (" is not a valid prompt. ")
        invalid = True
    if note == "YES":
        print ("Your loops will be arranged by Note. ")
        validprompt = validprompt+1
        moveNote = True
    elif note == "NO":
        print ("Your loops will not be arranged by Note. ")
    else:
        print(note)
        print (" is not a valid prompt. ")
        invalid = True
    if category == "YES":
        print ("Your loops will be arranged by Category. ")
        validprompt = validprompt+1
        moveCategory = True
    elif category == "NO":
        print ("Your loops will not be arranged by Category. ")
    else:
        print(category)
        print (" is not a valid prompt")
        invalid = True
    
    if validprompt > 0 and invalid == False:
        goahead=  input("Are you sure you would like to move your files? YES to continue NO to Just SCAN, X to exit. ")
        if (goahead == "YES"):
            scan = True
            justScan = False
            move = True
            
        elif(goahead == "X"):
            print("Thanks for USING SAMPO")
            os._exit(os.EX_OK)
        else:
            scan = True
            move = True
    else:
        print("Thanks for USING SAMPO")
        os._exit(os.EX_OK)
if(scan):
    directory = os.fsencode(dire)
    count = 0
    print("SCAN INITIATED")
    for subdir, dirs, files in os.walk(dire):
        for file in files:
            type = "none"
            category = "none"
            key = "none"
            tempo = "NA"
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
                colf = "F"+str(count)
                colg = "G"+str(count)
                # Sample TYPE
                if("drum" in file.lower() or "break" in file.lower()):
                    print ("drum")
                    category = "Drum"
                elif("snare" in file.lower()):
                    print ("snare")
                    category = "Snare"
                elif("kick" in file.lower()):
                    print ("kick")
                    category = "Kick"
                elif("phrase" in file.lower()):
                    print ("phrase")
                    category = "Phrase"
                elif("clap" in file.lower()):
                    print ("clap")
                    category = "Clap"
                elif("hat" in file.lower()):
                    category = "Hat"
                elif("bass" in file.lower()):
                    category = "Bass"
                elif("perc" in file.lower()):
                    print ("percussion")
                    category = "Percussion"
                elif("vocal" in file.lower()):
                    print ("vocal")
                    category = "Vocal"
                elif("synth" in file.lower() or "syn" in file.lower()):
                    print ("synth")
                    category = "Synth"
                elif("pad" in file.lower()):
                    print ("pad")
                    category = "Pad"
                elif("lead" in file.lower()):
                    print ("lead")
                    category = "Lead"
                elif("arp" in file.lower()):
                    print ("arp")
                    category = "Arp"
                elif ("chord" in file.lower()):
                    print ("chord")
                    category = "Chord"
                elif ("adlib" in file.lower()):
                    print ("adlib")
                    category = "Adlib"
                elif ("riser" in file.lower() or "uplifter" in file.lower()):
                    print ("riser")
                    category = "Riser"
                elif ("downer" in file.lower() or "downlifter" in file.lower()):
                    print ("downlifter")
                    category = "Downlifter"
                elif ("sweep" in file.lower()):
                    print ("sweep")
                    category = "Sweep"
                elif ("stab" in file.lower()):
                    print ("stab")
                    category = "Stab"
                #elif ("strum" in file.lower()):
                #    print ("strum")
                #    category = "Strum"
                elif ("piano" in file.lower() or "rhodes" in file.lower()  or "clav" in file.lower()):
                    print ("Piano")
                    category = "piano"
                elif ("horn" in file.lower()):
                    print ("horn")
                    category = "Horn"
                elif ("flute" in file.lower()):
                    print ("flute")
                    category = "Flute"
                elif ("violin" in file.lower()):
                    print ("violin")
                    category = "Violin"
                elif ("choir" in file.lower()):
                    print ("choir")
                    category = "Choir"
                elif ("gtr" in file.lower() or "lick" in file.lower() or "elec" in file.lower() or "pluck" in file.lower() or "strum" in file.lower() or "guitar" in file.lower()):
                    print ("guitar")
                    category = "Guitar"
                elif ("tom" in file.lower()):
                    print ("tom")
                    category = "Tom"
                elif ("shaker" in file.lower()):
                    print ("shaker")
                    category = "Shaker"
                elif ("vox" in file.lower() or "voc" in file.lower()):
                    print ("voc")
                    category = "Vocal"
                elif ("bong" in file.lower()):
                    print ("bong")
                    category = "Bong"
                elif ("foley" in file.lower()):
                    print ("foley")
                    category = "Foley"
                elif ("cello" in file.lower()):
                    print ("cello")
                    category = "Cello"
                elif ("viola" in file.lower()):
                    print ("viola")
                    category = "Viola"
                elif ("chorus" in file.lower()):
                    print ("chorus")
                    category = "Chorus"
                elif ("melod" in file.lower()):
                    print ("melody")
                    category = "Melody"
                elif ("SUB" in file.lower()):
                    print ("SUB")
                    category = "BASS"
                elif ("fx" in file.lower()):
                    print ("fx")
                    category = "fx"
                elif ("bell" in file.lower()):
                    print ("bell")
                    category = "Bell"
                elif ("combi" in file.lower() or "combo" in file.lower()):
                    print ("combo")
                    category = "Vombo"
                elif ("downshifter" in file.lower()):
                    print ("downshifter")
                    category = "Downshifter"
                elif ("tambourine" in file.lower()):
                    print ("tambourine")
                    category = "Tambourine"
                elif ("mallet" in file.lower()):
                    print ("mallet")
                    category = "Mallet"
                elif ("strings" in file.lower()):
                    print ("strings")
                    category = "Strings"
                elif ("sitar" in file.lower()):
                    print ("sitar")
                    category = "Sitar"
                elif ("hook" in file.lower()):
                    print ("hook")
                    category = "Hook"
                elif ("crash" in file.lower()):
                    print ("crash")
                    category = "Crash"
                elif ("bleep" in file.lower()):
                    print ("bleep")
                    category = "Bleep"
                elif ("ambiance" in file.lower()):
                    print ("ambiance")
                    category = "Ambiance"
                else:
                    print("uncategorized")
                    category = "uncategorized"
                #Change below Drum to drum if you would like to check drums for KEYS    
                if(category != "Drum"):
                    # Sample KEY
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

                    #sharp
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

                    elif("f#min" in file.lower()):
                        print ("F sharp minor")
                        key = "_F_sharp_minor"
                    elif("g#min" in file.lower()):
                        print ("G sharp minor")
                        key = "_G_sharp_minor"
                    elif("a#min" in file.lower()):
                        print ("A sharp minor")
                        key = "_A_sharp_minor"
                    elif("b#min" in file.lower()):
                        print ("B sharp minor")
                        key = "_B_sharp_minor"
                    elif("c#min" in file.lower()):
                        print ("C sharp minor")
                        key = "_C_sharp_minor"
                    elif("d#min" in file.lower()):
                        print ("D sharp minor")
                        key = "_D_sharp_minor"
                    elif("e#min" in file.lower()):
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
                    elif("_f" in file.lower()):
                        print ("F major")
                        key = "_F_major"
                    elif("_g" in file.lower()):
                        print ("G major")
                        key = "_G_major"
                    elif("_a" in file.lower()):
                        print ("A major")
                        key = "_A_major"
                    elif("_b" in file.lower()):
                        print ("B major")
                        key = "_B_major"
                    elif("_c" in file.lower()):
                        print ("C major")
                        key = "_C_major"
                    elif("_d" in file.lower()):
                        print ("D major")
                        key = "_D_major"
                    elif("_e" in file.lower()):
                        print ("E major")
                        key = "_E_major"
                    else:
                        print ("Key not found")
                        key = "uncategorized"
                else:
                    key = "uncategorized"
                    print("Drum not checked for keys")
                    # Sample genre

                if("house" in subdir.lower() or "club" in subdir.lower() or "disco" in subdir.lower() or "edm" in subdir.lower()):
                    print ("house")
                    category = "house"
                if("tech" in subdir.lower() or "techno" in subdir.lower() or "trance" in subdir.lower() or "psy" in subdir.lower() or "acid" in subdir.lower() or "rave" in subdir.lower()):
                    print ("trance")
                    category = "trance" 
                elif("funk" in subdir.lower() or "blues" in subdir.lower() or "jazz" in subdir.lower()):
                    print ("funky")
                    category = "funky"
                elif("afro" in subdir.lower() or "reggae" in subdir.lower() or "moombahton" in subdir.lower()  or "groove" in subdir.lower()):
                    print ("groovy")
                    category = "groovy"
                elif("jungle" in subdir.lower() or "garage" in subdir.lower() or "grime" in subdir.lower() or "Drum and bass" in subdir.lower() or "dnb" in subdir.lower() or "drum&bass" in subdir.lower() or "drum & bass" in subdir.lower() or "drum_&_bass" in subdir.lower()):
                    print ("brit")
                    category = "brit"
                elif("downtempo" in subdir.lower() or "lofi" in subdir.lower() or "lo-fi" in subdir.lower() or "ambient" in subdir.lower()):
                    print ("lofi")
                    category = "lofi"
                elif("rnb" in subdir.lower() or "pop" in subdir.lower() or "soul" in subdir.lower() or "indie" in subdir.lower() or "urban" in subdir.lower()):
                    print ("pop")
                    category = "pop"
                elif("trapstep" in subdir.lower() or "dubstep" in subdir.lower() or "discostep" in subdir.lower() or "hardstep" in subdir.lower() or "chillstep" in subdir.lower()):
                    print ("dubstep")
                    category = "dubstep"
                elif("ethnic" in subdir.lower() or "greek" in subdir.lower() or "turk" in subdir.lower() or "spanish" in subdir.lower() or "asia" in subdir.lower() or "india" in subdir.lower() or "mantra" in subdir.lower()):
                    print ("ethnic")
                    category = "ethnic"
                elif("drill" in subdir.lower() or "trap" in subdir.lower() or "hip hop" in subdir.lower() or "hip-hop" in subdir.lower() or "chillhop" in subdir.lower()):
                    print ("trap")
                    category = "trap"
                elif("nu_wave" in subdir.lower() or "nu wave" in subdir.lower() or "nuwave" in subdir.lower() or "nudisco" in subdir.lower() or "nu disco" in subdir.lower() or "nu_disco" in subdir.lower() or "neofunk" in subdir.lower()):
                    print ("nu_wav")
                    category = "nu_wav"
                elif("synthwave" in subdir.lower() or "retro" in subdir.lower()):
                    print ("synthwave")
                    category = "synthwave"
                elif("cinematic" in subdir.lower() or "foley" in subdir.lower()):
                    print ("cinematic")
                    category = "cinematic"
                elif("rock" in subdir.lower() or "metal" in subdir.lower()):
                    print ("rock")
                    category = "rock"
                elif("glitch" in subdir.lower()):
                    category = "glitch"
                elif("bass" in subdir.lower()):
                    print ("bass")
                    category = "bass"
                elif("vocal" in subdir.lower() or "acapella" in subdir.lower()):
                    print ("vocal")
                    category = "vocal"
                if (dur < 2.2):
                    type = "oneshot"
                    tempo = "NA"
                else:
                    type = "loop"
                    numbers = re.findall(r'\d+', file)
                    if(len(numbers) >0):
                        #print("tempo candidate")
                        for x in numbers:
                            x = int(x)
                            if (x>40 and x<200):
                                if (x>int(tempo)):
                                    tempo=x
                ###DO EM ALL
                if (justScan == False):
                    destination = cwd
                    if (moveType):
                        destination = destination+"\\"+type
                    if (moveCategory):
                        destination = destination+"\\"+category
                    if (moveTempo):
                        if(type == "loop"):
                            destination = destination+"\\"+str(tempo)
                    if (moveNote):
                        if(type == "loop" and category !="Drum"):
                            destination = destination+"\\"+key
                    destination =  destination +"\\"
                    if(os.path.exists(destination)):
                        print("destination Path found")
                    else:
                        os.makedirs(destination)
                        print("destination Path created")
                    destination = os.path.join(destination + file) 
                    fullpath = os.path.join(subdir, file)
                    shutil.move(fullpath, destination)
                    print (fullpath)
                    print(destination)
                worksheet.write(cola, fullpath)
                worksheet.write(colb, category) 
                worksheet.write(colc, type)
                worksheet.write(cold, dur)
                worksheet.write(cole, tempo)
                worksheet.write(colf, key)
                ## worksheet.write(colg, key)
                print('totals: ', count)
    workbook.close()
else:
    print("Scan Skipped")