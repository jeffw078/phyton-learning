#LEARNED HOW TO READ AND WRITE FROM JSON FILE USING PUBLIC DATA COLLECTION
import json

## read data from json file
with open("database.json", "r") as file:
    dict = json.load(file)
    for key, data in dict.items():
        print(key + "" + str(data))

## write data from json file

    dict = {
    "000.000.000-00": ["Jefferson Willian Cardoso","07/08/1991", "SC"],
    "000.000.000-01": ["Raquel Machado Fragoso","25/04/1989", "SC"]
       }

with open("database2.json", "w") as file:
    json.dump(dict,file)


## read data from external file for big data pourpose
# database = []
# with open("iris.data", "r") as file:
#     for record in file.readlines():
#         database.append(record.split(","))
#
#     print(float(database[0][0]) + float(database[0][1]))


    ##JSON EXAMPLE

