import json
import os


outdata = {}


### 1
files = os.listdir('file')              # make list of files in the folder 'file'

for fileName in files:                   
    if not fileName.endswith(".json"): continue
    if fileName.endswith(("_sapling.json","seeditem.json")): continue               # excludes "_sapling.json","seeditem.json" files 

    filePath = 'file/'+fileName

    with open(filePath, encoding='utf-8', errors='ignore', newline='\n') as f:
        data = json.load(f)

        quantity = 1
        if "result" in data:
            if "count" in data['result']:
                quantity = data['result']['count']

        if "ingredients" in data:
            material = data['ingredients']

        else: continue

    outdata[fileName] = []
    outdata[fileName].append(quantity)
    for i in range(0, len(material)):
        if "ore" in material[i]:
            outdata[fileName].append(material[i]['ore'])
        if "item" in material[i]:
            outdata[fileName].append(material[i]['item'])

with open('output/foodlist.json', 'w') as outfile:
    json.dump(outdata, outfile, indent=4)
            
        



### 2

sampleTable={
    "수량": [
        1,
        2
        ],
    "도구": [
        "toolA",
        "toolB",
        "toolC",
        ],
    "농작물": [
        "cropA",
        "cropB",
        "cropC",
        "cropD",
        ],
    "물/소금": [
        "listAllwater",
        "listAllSalt"
        ],
    "설탕": [
        "listAllsugar"
        ],
    "밀가루": [
        "Flour"
        ],
    "식용유": [
        "Oliveoil"
        ],
    "우유": [
        "Milk"
        ],
    "고기": [
        "listAllmeat"
        ],
    "물고기": [
        "listAllfish"
        ],
    "광물": [
        "coal",
        "diamond",
        "iron",
        "gold"
        ]
    }


with open('output/foodlist.json', encoding='utf-8', errors='ignore') as ff:
    data_ = json.load(ff)

    outdata_ = {}

    for i in data_:
        outdata_[i] = [0]*11
        for j in data_[i]:
            isHas = False
            k_number = 0
            for k in sampleTable:
                for value in sampleTable[k]:
                    if j==value:
                        if k_number == 0 :
                            outdata_[i][k_number] = j
                        elif k_number == 10:
                            if outdata_[i][k_number] == 0:
                                temp = [j]
                                outdata_[i][k_number] = temp
                            else: outdata_[i][k_number].append(j)
                        else: outdata_[i][k_number] = outdata_[i][k_number] + 1
                        isHas = True
                k_number = k_number + 1
            if not isHas:
                outdata_[i].append(j)



with open('output/result.txt', 'w') as tf:
    for i in outdata_:
        string = str(i)
        for j in outdata_[i]:
            string = string + ':' + str(j)
        string = string + '\n'
        tf.write(string)
                            
            
    
    
    

