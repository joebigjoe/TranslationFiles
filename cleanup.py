# use the subtitles from the netflix movie - The Trial of the Chicago 7
# strip the subtitles info
# then only the strings needed left
# other languages are translated by google translate
# will back it up for future usage.

import os

fileToClean = os.getcwd() +"\\tw.txt"

lines = []
linesclean = []
with(open(file=fileToClean, encoding='utf-8', errors='ignore', mode='r')) as filehandle:
    lines = filehandle.readlines()

for i in range(len(lines)):
    try:
        temp = int(lines[i].strip())
        cleanstring  = lines[i + 2].strip()
        linesclean.append(cleanstring + "\n")
    except Exception as ex:
        pass

filetoSave = os.getcwd() +"\\zh-TW.txt"
with(open(file=filetoSave, encoding='utf-8', errors='ignore', mode='w')) as filehandle:
    lines = filehandle.writelines(linesclean)
