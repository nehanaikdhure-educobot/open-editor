import os
import shutil







list_of_folders=os.listdir('./assets')
print(list_of_folders)
for folder in list_of_folders:
    images=os.listdir(f'./assets/{folder}')
    for image in images:
        if image.lower().count('background')>0 or image.lower().count('bg')>0 or image.lower().count('bunny')>0:
            print(folder+" "+image)
            shutil.move(f'./assets/{folder}/{image}',f'./images/{folder+"_"+image}')
