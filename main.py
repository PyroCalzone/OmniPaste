from system_hotkey import SystemHotkey
import keyboard
hk = SystemHotkey()

registered = False

clipboards = {
    "group1": "Welcome to omnipaste",
    "group2": "",
    "group3": "",
    "group4": "",
    "group5": "",
    "group6": "",
    "group7": "",
    "group8": "",
    "group9": "",
    "group10": "",
}

def getSelectedText(): #Grab selected text from whatever active window. Might have to modify clipboard history.
    #TODO: Find a method to do intended functionality.
    pass

def paste(text): #Paste text, or have the keyboard write it out.
    keyboard.release("control")
    keyboard.write(text)
    keyboard.press("control")

def copy(group): #Copy text
    clipboards[group] = getSelectedText()

def registerHotkeys(hotKey): #Register Hotkeys for togglable functionality.
    hotKey.register(('control', 'alt', '1'), callback=lambda x: copy("group1"))
    hotKey.register(('control', '1'), callback=lambda x: paste(clipboards["group1"]))
    hotKey.register(('control', 'alt', '2'), callback=lambda x: copy("group2"))
    hotKey.register(('control', '2'), callback=lambda x: paste(clipboards["group2"]))
    hotKey.register(('control', 'alt', '3'), callback=lambda x: copy("group3"))
    hotKey.register(('control', '3'), callback=lambda x: paste(clipboards["group3"]))
    hotKey.register(('control', 'alt', '4'), callback=lambda x: copy("group4"))
    hotKey.register(('control', '4'), callback=lambda x: paste(clipboards["group4"]))
    hotKey.register(('control', 'alt', '5'), callback=lambda x: copy("group5"))
    hotKey.register(('control', '5'), callback=lambda x: paste(clipboards["group5"]))
    hotKey.register(('control', 'alt', '6'), callback=lambda x: copy("group6"))
    hotKey.register(('control', '6'), callback=lambda x: paste(clipboards["group6"]))
    hotKey.register(('control', 'alt', '7'), callback=lambda x: copy("group7"))
    hotKey.register(('control', '7'), callback=lambda x: paste(clipboards["group7"]))
    hotKey.register(('control', 'alt', '8'), callback=lambda x: copy("group8"))
    hotKey.register(('control', '8'), callback=lambda x: paste(clipboards["group8"]))
    hotKey.register(('control', 'alt', '9'), callback=lambda x: copy("group9"))
    hotKey.register(('control', '9'), callback=lambda x: paste(clipboards["group9"]))
    hotKey.register(('control', 'alt', '0'), callback=lambda x: copy("group10"))
    hotKey.register(('control', '0'), callback=lambda x: paste(clipboards["group10"]))

def unregisterHotkeys(hotKey): # Unregister Hotkeys for togglable functionality.
    hotKey.unregister(('control', 'alt', '1'))
    hotKey.unregister(('control', '1'))
    hotKey.unregister(('control', 'alt', '2'))
    hotKey.unregister(('control', '2'))
    hotKey.unregister(('control', 'alt', '3'))
    hotKey.unregister(('control', '3'))
    hotKey.unregister(('control', 'alt', '4'))
    hotKey.unregister(('control', '4'))
    hotKey.unregister(('control', 'alt', '5'))
    hotKey.unregister(('control', '5'))
    hotKey.unregister(('control', 'alt', '6'))
    hotKey.unregister(('control', '6'))
    hotKey.unregister(('control', 'alt', '7'))
    hotKey.unregister(('control', '7'))
    hotKey.unregister(('control', 'alt', '8'))
    hotKey.unregister(('control', '8'))
    hotKey.unregister(('control', 'alt', '9'))
    hotKey.unregister(('control', '9'))
    hotKey.unregister(('control', 'alt', '0'))
    hotKey.unregister(('control', '0'))

def registerToggle(): #Toggle hotkeys
    global registered
    if registered:
        unregisterHotkeys(hk)
        registered = False
    else:
        registerHotkeys(hk)
        registered = True

#TODO: add notification that you've switched key-binds
#TODO: add GUI for identifying which binds holds which pastes 

if __name__ == '__main__':
    hk.register(('control', 'grave'), callback=lambda x: registerToggle()) #
    input()
    #Ensuring hotkeys are unregistered before exiting, not sure if required. 
    if registered:
        unregisterHotkeys(hk)
        registered = False
