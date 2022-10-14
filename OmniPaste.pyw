#Imports
from time import sleep
from os import path
from PIL import Image #Used for converting icon.ico to something pystray can use.
from system_hotkey import SystemHotkey #Used for registering key-binds
import keyboard #Used for simulating keyboard inputs
import pyperclip #Used for modifying and reading the clipboard
import pystray #Used for system tray

notified = False #Will we send notifications?
registered = False #Are key-binds registered?

clipboards = { #Clipboard values for each hotkey group, sorted by order of appearance in keyboard
    "group1": "",
    "group2": "",
    "group3": "",
    "group4": "",
    "group5": "",
    "group6": "",
    "group7": "",
    "group8": "",
    "group9": "",
    "group0": "",
}

def prepCopy(keys, group):
    for key in keys:
        keyboard.release(key) #Release all keys that are currently press down so they don't interfere with sending a copy command
    copy(group)
    for key in keys:
        if not key.isdigit():
            #Press down all of our keys again except for one, the digit,
            #so we don't accidentally read it as the key-bind being pressed again.
            keyboard.press(key)

def copy(group): #Clipboard to send the text to
    originalClipboard = pyperclip.paste() #Save our current clipboard so we can restore
    keyboard.press("control"); keyboard.press("c")
    sleep(0.01) #The copy function built into the system may not be able to keep up with our code"s speed
    keyboard.release("control"); keyboard.release("c")
    newClipboard = pyperclip.paste() #Save our new clipboard, this should be our selected text.
    clipboards[group] = newClipboard
    pyperclip.copy(originalClipboard) #Restore clipboard



def paste(text): #Paste text, or have the keyboard write it out.
    splitText = text.splitlines() #Split the text up by newline characters
    keyboard.release("control") #Release control button so we don't accidentally activate other hotkeys
    for index, line in enumerate(splitText, start = 1):
        keyboard.write(line)
        if index != len(splitText):
            keyboard.press_and_release("shift+enter") #Add a soft line break (Won't send messages on messaging platforms)
    keyboard.press("control") #Press the control button so you can spam paste if you want.



def registerHotkeys(hotKey): #Register Hotkeys for togglable functionality.
    [hotKey.register(("control", "alt", str(i)), callback=lambda x: prepCopy(("control", "alt", str(i)), f"group{i}")) for i in range(10)]
    [hotKey.register(("control", str(i)), callback=lambda x: paste(clipboards[f"group{i}"])) for i in range(10)]

def unregisterHotkeys(hotKey): #Unregister Hotkeys for togglable functionality.
    [hotKey.unregister(("control", "alt", str(i))) for i in range(10)]
    [hotKey.unregister(("control", str(i))) for i in range(10)]



def registerToggle(): #Toggle hotkeys
    global registered
    if registered:
        unregisterHotkeys(hk)
        registered = False
        if notifyCompat and notified: tray.notify("OmniPaste binds disabled")
    else:
        registerHotkeys(hk)
        registered = True
        if notifyCompat and notified: tray.notify("OmniPaste binds enabled")

def notifyToggle(): #Toggle Notifications
    global notified
    if notified:
        notified = False
    else:
        notified = True

def prepQuit():
    #Ensure hotkeys are unregistered before exiting, not sure if required. 
    global registered
    if registered:
        registerToggle
    #Turn off tray so we can exit.
    tray.visible = False
    tray.stop()


#System Tray Setup
menu = pystray.Menu(

    pystray.MenuItem(
        "Notifications",
        notifyToggle,
        checked=lambda x: notified,
    ),
            
    pystray.MenuItem(
        "Binds",
        registerToggle,
        checked=lambda x: registered,
    ),

    pystray.MenuItem(
        "Quit",
        lambda : prepQuit(),
    ),
)

tray = pystray.Icon(
    "OmniPaste",
    title="OmniPaste",
    icon=Image.open(path.abspath(path.join(path.dirname(__file__), "assets/icon.ico"))),
    menu=menu
    )

notifyCompat = tray.HAS_NOTIFICATION #MacOS doesn't support notifications


if __name__ == "__main__":
    hk = SystemHotkey()
    hk.register(("control", "grave"), callback=lambda x: registerToggle())
    tray.run() #This holds the program up, won't quit automatically

#TODO: add GUI for identifying which binds holds which pastes 
