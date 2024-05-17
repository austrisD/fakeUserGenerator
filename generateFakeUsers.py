import random
# import maleNames
# import femaleNames
import json
from datetime import date


namesFile = open('database/nameData.json')
surnameFile = open('database/surnamesData.json')

nameData = json.load(namesFile)
surnameData = json.load(surnameFile)

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

    genderBoolean = random.choice([True, False])


#Give random EU country adjust by population.
    countryListLength = len(countryList)
    countryFrom = countryList[random.randrange(0, countryListLength)]

# give random name based on gender reduce probability for if have that name ,include name popularity
    randomNameFromCountry = random.randrange(1,len(nameData[countryFrom]))  #its a random number based on length of list inside country!!! 
    print(f'test1: {countryFrom}:{randomNameFromCountry}')
    name = nameData[countryFrom][randomNameFromCountry][2]
# give gender based on name if specified if no search
    checkIfGenderIncluded = nameData[countryFrom][randomNameFromCountry][0] == "Gender"
    if checkIfGenderIncluded:
        gender = nameData[countryFrom][randomNameFromCountry][randomNameFromCountry][1] # make it random if gender natural Name
    else:
        gender= "LGBT+"
#give last name based on country, adjust by last name popularity + and foreign population from count include.    
    randomSurname = random.randrange(0, len(surnameData[countryFrom])) #number generated from list length
    print(f'test2: {randomSurname}')  #akrotiri-and-dhekelia troble
    print(f'test3: {surnameData[countryFrom][randomSurname]}')
    lastName = surnameData[countryFrom][randomSurname][1]
#give random age [create birth rate cone] include age displace by gender
    BirthYear = random.randrange(1945, 2005)
#give random date.Take in count short months
    birthDate = [random.randrange(1, 30),random.randrange(1, 12)]
#calculate birth date
    today = date.today()
    ageCurrent = today.year - BirthYear - ((today.month, today.day) < (birthDate[1], birthDate[0]))
#password hasher



    # print(f'gender:{gender} name: {name} surname:{lastName} age:{ageCurrent} birthDate:{birthDate} from: {countryFrom} CREATED!!!')

    
    FakeUserList.append({
    "userId":loopCount,
    "password":'safePassword#1234',
    "hashPassword":'asdasfasdfsadfdsdasd65as53v4a5sdvas15df5a3sdcSAd3f63',
    "name":name,   #sometimes name is number !!!
    "lastName":lastName,
    "gender":gender,
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
f = open('UserFile.json','x')
f.write(f'{json.dumps(FakeUserList)}')
f.close
