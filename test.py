import os 

import json

final_string=""

list_of_files=os.listdir('./new_sprites')
for file in list_of_files:
    final_string+="""{
        "name": """+'"'+file.split("_")[1].split(".")[0]+"""",
        "tags": [
            "eduCOBOT",
            "educobot"
        ],
        "isStage": false,
        "variables": {},
        "costumes": [
            {
                "assetId": "60f720956ab1840431dcf0616ce98f14",
                "name": "amon",
                "bitmapResolution": 2,
                "md5ext": "https://nehanaikdhure-educobot.github.io/open-editor/new_sprites/"""+file+"""",
                "dataFormat": "png",
                "rotationCenterX": 174,
                "rotationCenterY": 162
            }
        ],
        "sounds": [
            {
                "assetId": "83a9787d4cb6f3b7632b4ddfebf74367",
                "name": "pop",
                "dataFormat": "wav",
                "format": "",
                "rate": 44100,
                "sampleCount": 1032,
                "md5ext": "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ],
        "blocks": {}
    },
"""
final_string+="]"
print(final_string)

with open("new_sprites.json", "w") as outfile:
    outfile.write(final_string)
