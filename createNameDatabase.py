import os
import json

#from 1880 to 2023

script_dir = os.path.dirname(__file__)

namelistFemales = {}
namelistMales = {}


#loop files
year = 1880
while year < 2023:
    databasePath = f"database/names/yob{year}.txt"
    path = os.path.join(script_dir,databasePath)
    f = open(path,"r")
    yearList = f.readlines()

    for X in yearList:
        if X.find(',F,') > 0:
            clearedF = X.rstrip('\n')  # removes /n from end of string
            toListF = clearedF.split(',')  #convert to list
            toListF[2] = int(toListF[2])   #convert string to number
            if not toListF[0] in namelistFemales:
                namelistFemales[toListF[0]] = [toListF[1],toListF[2]]
            else:
                namelistFemales[toListF[0]][1] += toListF[2]

        elif  X.find(',M,') > 0 :
            clearedM = X.rstrip('\n')
            toListM = clearedM.split(',')
            toListM[2] = int(toListM[2])
            if not toListM[0] in namelistMales:
                namelistMales[toListM[0]] = [toListM[1],toListM[2]]
            else:
                namelistMales[toListM[0]][1] += toListM[2]         
    # if year == 1885:
    #     break

    f.close()    
    year+=1


print(len(namelistFemales))
print(len(namelistMales))

fileF = open('femaleList.json','x')
fileF.write(json.dumps(namelistFemales))
fileF.close

fileM = open('maleList.json','x')
fileM.write(json.dumps(namelistMales))
fileM.close


