#tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog

import ttkbootstrap as ttk

#pytube
from pytube import YouTube
import os

# VERSIÓN SIN SELECTOR DE MP3 Y MP4

def download():
    try:
        url = entryString.get()
        video = YouTube(url)#video
        print(f'Title: {video.title}')
        print('Dowloading...')
        #audio_video_selector = selection()
        extension = ".mp"
        '''
        if not audio_video_selector:
            extension += "4"
        else:
            extension +="3"
        '''
        out_path = video.streams.filter(only_audio=True).first().download(entryPath.get())#download
        new_name = os.path.splitext(out_path)#original name
        os.rename(out_path, new_name[0] + extension) 

        MessageBox.showinfo('','Done!')
        print('Finished')
    except:
        MessageBox.showerror('', 'Path or entry error!')

def get_path():
    filename = filedialog.askdirectory()
    entry_path.insert(0,filename)

def check_extension(selector:bool)->str:
    if selector:
        res = True
    return res
'''
def selection()->bool:
    res = None
    if var1.get():
        res = True
        c2.config()
    elif var2.get():
        res = False

    return res
'''

#window
window = ttk.Window()
window.title('Youtube')
window.geometry('540x320')

#title
titleFrame = ttk.Frame(window)
title = ttk.Label(titleFrame, text = 'Youtube MP3 Downloader', font = 'Calibri 24 bold')
davi = ttk.Label(titleFrame, text='By Davi:D', font='Calibri 20')

title.pack(side='top')
davi.pack(side = 'top')
titleFrame.pack(pady = 30)

#path
path_frame = ttk.Frame(window, width=700)
entryPath = tk.StringVar()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
path = ttk.Button(path_frame,  text = 'Path:', command=get_path)
entry_path = ttk.Entry(path_frame, textvariable= entryPath)
'''
c1 = ttk.Checkbutton(path_frame, text="mp4",variable=var1, onvalue=True, offvalue=False, command=selection)
c2 = ttk.Checkbutton(path_frame, text="mp3",variable=var2, onvalue=True, offvalue=False, command=selection)

c1.pack(side="right")
c2.pack(side="right")
'''
path.pack(side = 'left', padx=10)
entry_path.pack(side = 'left')
path_frame.pack()

#input 
imput_frame = ttk.Frame(window)
entryString = tk.StringVar()
entry = ttk.Entry(imput_frame, textvariable = entryString)
button = ttk.Button(imput_frame, text = 'Download',  command = download)

entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
imput_frame.pack(pady = 10)

#exit
exit_button = ttk.Button(text="Quit", command=window.quit)
exit_button.pack()


window.mainloop()