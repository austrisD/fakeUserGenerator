import random
# import maleNames
# import femaleNames
import json
from datetime import date
import bcrypt
import os.path


nameData = json.load(open('database/nameData.json'))
surnameData = json.load(open('database/surnamesData.json'))

countryList = list(nameData.keys()) #make country list from dict

startMessage = "Script Started Successful !!!"


FakeUserList = []
# prompt how many users need to generate?
FakeUserCount = int(input('How many fake users need to generate? number:'))


"""
User generation loop.
"""


print(f'starting to generate list with: {FakeUserCount} users')


loopCount = 1

while FakeUserCount != len(FakeUserList):
    # print(f'    loop times: {loopCount}')
    # print(f'user generated: {len(FakeUserList)}')

#Give random EU country adjust by population.
    countryListLength = len(countryList)
    countryListNumber = random.randrange(0,countryListLength)
    countryFrom = countryList[countryListNumber]

# give random name based on gender reduce probability for if have that name ,include name popularity
    CheckNameLocation = nameData[countryFrom][0].index("Forename")
    randomNameFromCountry = random.randrange(1,len(nameData[countryFrom]))  #its a random number based on length of list inside country!!! 
    name = nameData[countryFrom][randomNameFromCountry][CheckNameLocation]

    if name.isdigit(): #test if name string is numbers
        print(f'name contains digits:  {name} from this country :{countryFrom} number:{randomNameFromCountry}')        
# give gender based on name if specified if no search  #has to by fixed  "Male: 97%"   "Female: 98%"
    checkIfGenderIncluded = nameData[countryFrom][0][1] == "Gender"
    Gender = "no data"   # fix data or create a search function in other country
   
    if checkIfGenderIncluded:
        Gender = nameData[countryFrom][randomNameFromCountry][1]
        if not Gender.isalpha(): # check if gender contains %
            genderPercentage = Gender.rsplit(":")
            Gender = genderPercentage[0]
#give last name based on country, adjust by last name popularity + and foreign population from count include.    
    randomSurname = random.randrange(0, len(surnameData[countryFrom])) #number generated from list length
    lastName = surnameData[countryFrom][randomSurname][1]

#give random age [create birth rate cone] include age displace by gender
    BirthYear = random.randrange(1945, 2005)

#give random date.Take in count short months
    birthDate = [random.randrange(1, 30),random.randrange(1, 12)]

#calculate birth date
    today = date.today()
    ageCurrent = today.year - BirthYear - ((today.month, today.day) < (birthDate[1], birthDate[0]))

#password hasher
    password = f'cln:{countryListNumber}CF:{countryFrom}rnfc:{randomNameFromCountry}CIGI:{checkIfGenderIncluded}G:{Gender}RS:{randomSurname}LN:{lastName}'
    print(f'pass: {password}')
    salt = bcrypt.gensalt(6)
    print(f'salt: {salt}')
    hashPassword = bcrypt.hashpw(bytes(4), salt)
    

    # print(f'gender:{gender} name: {name} surname:{lastName} age:{ageCurrent} birthDate:{birthDate} from: {countryFrom} CREATED!!!')

    
    FakeUserList.append({
    "userId":loopCount,
    "password":password,
    "salt":str(salt),
    "hashPassword":str(hashPassword),
    "name":name,   #sometimes name is number !!!
    "lastName":lastName,
    "gender":Gender,
    "race":"caucasian",
    "religion":"atheist",
    "politicalAffiliation":(0,0),  #political axis XY  from -2 to 2+
    "countryFrom":countryFrom,
    "cityLiveIn":'Riga',
    "profilePhotoLocation":'c/photos/a/7856',
    "ageCurrent":ageCurrent,
    "BirthYear": BirthYear ,
    "birthDate":birthDate,
    "relationStatus": 'single' if random.choice([True, False]) else 'Taken',
    "friendList":[7895,2254,1254]
    })

    loopCount +=1

    if FakeUserCount == loopCount:
        break    
    if loopCount > 1000:
        break



print(f'generator stops finished generating list. List length:{len(FakeUserList)}')

femaleCount = 0
maleCount = 0
nationalityCount = 0
ageRange18_25 = 0
ageRange25_35 = 0
ageRange35_45 = 0
ageRange45_55 = 0
ageRange55_70 = 0
# nationalityCount = {{"Latvia":1}}


for x in FakeUserList:

#get gender counts
    if x["gender"] == "female":
         femaleCount +=1
    elif True:
        maleCount +=1
        
#create age range statistic
    age = x["ageCurrent"]
    if age < 25:
        ageRange18_25 +=1
    elif age > 25 and age < 35:
        ageRange25_35 +=1
    elif age > 35 and age < 45:
        ageRange35_45 +=1
    elif age > 45 and age < 55:
        ageRange45_55 +=1
    elif True:
        ageRange55_70 +=1

print(f'statistic: females{femaleCount} males:{maleCount}  ')
print(f'18>25: {ageRange18_25}')
print(f'25>35: {ageRange25_35}')
print(f'35>45: {ageRange35_45}')
print(f'45>55: {ageRange45_55}')
print(f'55>70: {ageRange55_70}')
print('Creating json file with Users')





#file writing handler

fileName = f'FakeUserFile'
folderPath = 'FakeUsers'
filenames = [file for file in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, file))]

if os.path.isfile(f'{folderPath}/{fileName}.json'):
    fileName = f'{fileName}{len(filenames)}' 



f = open(f'FakeUsers/{fileName}.json','x')
f.write(f'{json.dumps(FakeUserList)}')
f.close
