import requests
import random
# import maleNames
# import femaleNames
import SmallTuples
import json


maleDataBase = open('maleList.json','r')
femaleDateBase = open('femaleList.json','r')


femaleNames = list(json.loads(femaleDateBase.read()).keys())
maleNames =  list(json.loads(maleDataBase.read()).keys())




startMessage = "Script Started Successful !!!"


FakeUserList = [{
    "userId":7856,
    "hashPassword":'asdasfasdfsadfdsdasd65as53v4a5sdvas15df5a3sdcSAd3f63',
    "name":'Austris',
    "lastName":'Daugulis',
    "gender":'male',
    "countryFrom":'Latvia',
    "profilePhotoLocation":'c/photos/a/7856',
    "ageCurrent":33,
    "BirthYear":1991,
    "birthDate":[3,18],
    "relationStatus":'single',
    "friendList":[7895,2254,1254]
    }]
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

# give random gender include gender imbalance 
    gender = "male" if genderBoolean else "female"
#Give random EU country adjust by population.
    countryFrom = SmallTuples.country[random.randrange(0, len(SmallTuples.country))]
# give random name based on gender reduce probability for if have that name ,include name popularity
    name = maleNames[random.randrange(0, len(maleNames))] if genderBoolean else femaleNames[random.randrange(0, len(femaleNames))]
#give last name based on country, adjust by last name popularity + and foreign population from count include.
    lengthOfTuple = len(SmallTuples.countrySurnames[countryFrom])
    lastName = SmallTuples.countrySurnames[countryFrom][random.randrange(0, lengthOfTuple)]
#give random age [create birth rate cone] include age displace by gender
    ageCurrent = random.randrange(18, 70)
#give random date
    birthDate = [random.randrange(1, 30),random.randrange(1, 12)]
#password hasher

    print(f'gender:{gender} name: {name} surname:{lastName} age:{ageCurrent} birthDate:{birthDate} from: {countryFrom} CREATED!!!')

    
    FakeUserList.append({
    "userId":loopCount,
    "hashPassword":'asdasfasdfsadfdsdasd65as53v4a5sdvas15df5a3sdcSAd3f63',
    "name":name,
    "lastName":lastName,
    "gender":gender,
    "countryFrom":countryFrom,
    "profilePhotoLocation":'c/photos/a/7856',
    "ageCurrent":ageCurrent,
    "BirthYear":1991,
    "birthDate":birthDate,
    "relationStatus":'single',
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
