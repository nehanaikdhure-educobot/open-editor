import os 

import json

final_string="["

list_of_files=os.listdir('./images')
for file in list_of_files:
    final_string+="""
    {"name": \""""+file.split("_")[1].split(".")[0]+"""\",
        "tags": [
            "background"
        ],
        "assetId": "67e0db3305b3c8bac3a363b1c428892e",
        "bitmapResolution": 2,
        "dataFormat": "png",
        "md5ext": "https://open-editor-assets.s3.ap-south-1.amazonaws.com/"""+file+"""",
        "rotationCenterX": 480,
        "rotationCenterY": 360
    },
"""
final_string+="]"
print(final_string)

with open("assets.json", "w") as outfile:
    outfile.write(final_string)