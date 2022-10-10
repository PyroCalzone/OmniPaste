from system_hotkey import SystemHotkey
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

def paste(text): #Paste text, or have the keyboard write it out. TODO: find and integrate a method to write the text without having held modifiers affect the output.
    print(f"Pasting: {text}")


def registerHotkeys(hotKey): #Register Hotkeys for togglable functionality. TODO: Change copy callbacks to grab selected text and save in dictionary
    hotKey.register(('control', 'alt', '1'), callback=lambda x: print("Copy Group 1"))
    hotKey.register(('control', '1'), callback=lambda x: paste(clipboards["group1"]))
    hotKey.register(('control', 'alt', '2'), callback=lambda x: print("Copy Group 2"))
    hotKey.register(('control', '2'), callback=lambda x: print("Paste Group 2"))
    hotKey.register(('control', 'alt', '3'), callback=lambda x: print("Copy Group 3"))
    hotKey.register(('control', '3'), callback=lambda x: print("Paste Group 3"))
    hotKey.register(('control', 'alt', '4'), callback=lambda x: print("Copy Group 4"))
    hotKey.register(('control', '4'), callback=lambda x: print("Paste Group 4"))
    hotKey.register(('control', 'alt', '5'), callback=lambda x: print("Copy Group 5"))
    hotKey.register(('control', '5'), callback=lambda x: print("Paste Group 5"))
    hotKey.register(('control', 'alt', '6'), callback=lambda x: print("Copy Group 6"))
    hotKey.register(('control', '6'), callback=lambda x: print("Paste Group 6"))
    hotKey.register(('control', 'alt', '7'), callback=lambda x: print("Copy Group 7"))
    hotKey.register(('control', '7'), callback=lambda x: print("Paste Group 7"))
    hotKey.register(('control', 'alt', '8'), callback=lambda x: print("Copy Group 8"))
    hotKey.register(('control', '8'), callback=lambda x: print("Paste Group 8"))
    hotKey.register(('control', 'alt', '9'), callback=lambda x: print("Copy Group 9"))
    hotKey.register(('control', '9'), callback=lambda x: print("Paste Group 9"))
    hotKey.register(('control', 'alt', '0'), callback=lambda x: print("Copy Group 10"))
    hotKey.register(('control', '0'), callback=lambda x: print("Paste Group 10"))

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

#Todo, add code for finding selected text

hk.register(('control', 'grave'), callback=lambda x: registerToggle()) #
input()

#Ensuring hotkeys are unregistered before exiting, not sure if required. 
if registered:
        unregisterHotkeys(hk)
        registered = False