import os
from pathlib import Path
import shutil

z = os.path.join(os.getenv('USERPROFILE'), 'Desktop') # Gets the users desktop dir
os.chdir(z) # Changes dir to the users desktop
print(z)
Path("elden_mod").mkdir(exist_ok=True) # Creates a folder named elden_mod
z = os.path.abspath('elden_mod')
print('Created a folder named elden_mod at ', z)
try:
    x = input("Enter path of your elden ring game folder: ") # Grabs the path of the elden ring game folder
    os.chdir(x) # Changes into that directory
    for file in os.listdir(): # Loops through each file in the directory
        if file == 'dinput8.dll':
            shutil.move(file, z)
            print(f'moving... {file} to elden_mod')
            os.remove(os.path.abspath(file))

    ans = input('Would you like to return to the modded elden ring version? (Y/n) ')
    if ans.lower() == 'y':
        os.chdir(z)
        for file in os.listdir(): # brings back the dll file where it was orginally
            if file == 'dinput8.dll':
                shutil.copy(file, x)
                print(f'{ file } has returned into { x }')
    else:
        pass
except:
    pass