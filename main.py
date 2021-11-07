import keyboard

#Not finished and still WIP
def setKeys():
    print("Press all 5 keys for you flasks and press space when u finished")
    flaskKeys=keyboard.record(until='space')
    playKeys(flaskKeys)
    

def playKeys(*flaskKeys):
    flaskKeys=list(flaskKeys)
    for i in range(len(flaskKeys)):
        temp = flaskKeys[i]
        print(temp)
        temp = temp[14:15]
        print(temp)
        flaskKeys[i]=temp
    for i in range(len(flaskKeys)):
        #keyboard.press_and_release(flaskKeys[i])
        print('Key')
        print(flaskKeys[i])


setKeys()
