from system_hotkey import SystemHotkey
import keyboard
import pyperclip
from time import sleep
from sysIcon import SysTrayIcon
from os import path
hk = SystemHotkey()
icon = path.abspath(path.join(path.dirname(__file__), 'assets/icon.ico'))
hover_text = "OmniPaste"

registered = False

clipboards = {
    "group1": "",
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

def prepCopy(keys, group): #Keys that are currently pressed down, clipboard to send the text to.
    for key in keys:
        keyboard.release(key) #Release all keys that are currently press down so they don't interfere with sending a copy command
    copy(group) # Send copy command
    for key in keys:
        if not key.isdigit(): # Press down all of our keys again except for one, the digit, so we don't accidentally read it as the key-bind being pressed again.
            keyboard.press(key)

def copy(group): # Clipboard to send the text to
    originalClipboard = pyperclip.paste() #Save our current clipboard so we can restore
    keyboard.press("control"); keyboard.press("c") #Press the buttons relating to copying text
    sleep(0.01) # The copy function built into the system may not be able to keep up with our code's speed
    keyboard.release("control"); keyboard.release("c") #Release the buttons relating to copying text
    newClipboard = pyperclip.paste() #Save our new clipboard, this should be our selected text.
    clipboards[group] = newClipboard #Set the group's clipboard to our selected text
    pyperclip.copy(originalClipboard) #Restore clipboard


def paste(text): #Paste text, or have the keyboard write it out.
    splitText = text.splitlines() #Split the text up by newline characters
    keyboard.release("control") #Release control button so we don't accidentally activate other hotkeys
    for index, line in enumerate(splitText, start = 1): #For every newline in text
        keyboard.write(line) #Write the line out
        if index != len(splitText): #If the line isn't the last line
            keyboard.press_and_release("shift+enter") #Add a soft line break (Won't send messages on messaging platforms)
    keyboard.press("control") #Press the control button so you can spam paste if you want.

def registerHotkeys(hotKey): #Register Hotkeys for togglable functionality.
    hotKey.register(('control', 'alt', '1'), callback=lambda x: prepCopy(('control', 'alt', '1'), "group1"))
    hotKey.register(('control', '1'), callback=lambda x: paste(clipboards["group1"]))
    hotKey.register(('control', 'alt', '2'), callback=lambda x: prepCopy(('control', 'alt', '2'), "group2"))
    hotKey.register(('control', '2'), callback=lambda x: paste(clipboards["group2"]))
    hotKey.register(('control', 'alt', '3'), callback=lambda x: prepCopy(('control', 'alt', '3'), "group3"))
    hotKey.register(('control', '3'), callback=lambda x: paste(clipboards["group3"]))
    hotKey.register(('control', 'alt', '4'), callback=lambda x: prepCopy(('control', 'alt', '4'), "group4"))
    hotKey.register(('control', '4'), callback=lambda x: paste(clipboards["group4"]))
    hotKey.register(('control', 'alt', '5'), callback=lambda x: prepCopy(('control', 'alt', '5'), "group5"))
    hotKey.register(('control', '5'), callback=lambda x: paste(clipboards["group5"]))
    hotKey.register(('control', 'alt', '6'), callback=lambda x: prepCopy(('control', 'alt', '6'), "group6"))
    hotKey.register(('control', '6'), callback=lambda x: paste(clipboards["group6"]))
    hotKey.register(('control', 'alt', '7'), callback=lambda x: prepCopy(('control', 'alt', '7'), "group7"))
    hotKey.register(('control', '7'), callback=lambda x: paste(clipboards["group7"]))
    hotKey.register(('control', 'alt', '8'), callback=lambda x: prepCopy(('control', 'alt', '8'), "group8"))
    hotKey.register(('control', '8'), callback=lambda x: paste(clipboards["group8"]))
    hotKey.register(('control', 'alt', '9'), callback=lambda x: prepCopy(('control', 'alt', '9'), "group9"))
    hotKey.register(('control', '9'), callback=lambda x: paste(clipboards["group9"]))
    hotKey.register(('control', 'alt', '0'), callback=lambda x: prepCopy(('control', 'alt', '0'), "group10"))
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

def prepQuit():
    #Ensuring hotkeys are unregistered before exiting, not sure if required. 
    if registered:
        unregisterHotkeys(hk)
        registered = False

if __name__ == '__main__':
    def leave():
        quit()
    hk.register(('control', 'grave'), callback=lambda x: registerToggle()) #
    SysTrayIcon(icon, hover_text, (), default_menu_index=1)
