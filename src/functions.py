from pytube import YouTube
import os
from main import UI
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog

def download(entryString, entryPath):
    
    try:
        url = entryString.get()
        video = YouTube(url)#video
        print(f'Title: {video.title}')
        print('Dowloading...')
        audio_video_selector = selection()
        extension = '.mp'

        if not audio_video_selector:
            extension += "4"
        else:
            extension +="3"

        out_path = video.streams.filter(only_audio=False).first().download(entryPath.get())#download
        new_name = os.path.splitext(out_path)#original name
        os.rename(out_path, new_name[0] + extension) 

        MessageBox.showinfo('','Done!')
        print('Finished')
    except:
        MessageBox.showerror('', 'Path or entry error!')
    
def get_path(entry_path):
    filename = filedialog.askdirectory()
    entry_path.insert(0,filename)

def check_extension(selector:bool)->str:
    if selector:
        res = True
    return res

def selection()->bool:
    '''
    res = None
    if var1.get():
        res = True
        c2.config()
    elif var2.get():
        res = False

    return res
    '''