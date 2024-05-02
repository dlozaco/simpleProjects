#tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog

import ttkbootstrap as ttk

#pytube
from pytube import YouTube
import os

class UI(ttk.Frame):
    def __init__(self, parent=None):
        ttk.Frame.__init__(self,parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Youtube Downloader")

        #title
        titleFrame = ttk.Frame()
        title = ttk.Label(titleFrame, text = 'Youtube MP3 Downloader', font = 'Calibri 24 bold')
        davi = ttk.Label(titleFrame, text='By Davi:D', font='Calibri 20')

        title.pack(side='top')
        davi.pack(side = 'top')
        titleFrame.pack(pady = 30)

        #path
        path_frame = ttk.Frame(self.parent, width=700)
        entryPath = tk.StringVar()
        var1 = tk.BooleanVar()
        var2 = tk.BooleanVar()
        entry_path = ttk.Entry(path_frame, textvariable= entryPath)
        path = ttk.Button(path_frame,  text = 'Path:', command=self.get_path)
        c1 = ttk.Checkbutton(path_frame, text="mp4",variable=var1, onvalue=True, offvalue=False, command=self.selection)
        c2 = ttk.Checkbutton(path_frame, text="mp3",variable=var2, onvalue=True, offvalue=False, command=self.selection)

        c1.pack(side="right")
        c2.pack(side="right")
        path.pack(side = 'left', padx=10)
        entry_path.pack(side = 'left')
        path_frame.pack()

        #input
        imput_frame = ttk.Frame(self.parent) 
        entryString = tk.StringVar()
        entry = ttk.Entry(imput_frame, textvariable = entryString)
        button = ttk.Button(imput_frame, text = 'Download',  command = self.download)

        entry.pack(side = 'left', padx = 10)
        button.pack(side = 'left')
        imput_frame.pack(pady = 10)

        #exit
        exit_button = ttk.Button(text="Quit", command=self.parent.quit)
        exit_button.pack()
        
    def download(self):
    
        try:
            url = self.entryString.get()
            video = YouTube(url)#video
            print(f'Title: {video.title}')
            print('Dowloading...')
            audio_video_selector = self.selection()
            extension = '.mp'

            if not audio_video_selector:
                extension += "4"
            else:
                extension +="3"

            out_path = video.streams.filter(only_audio=False).first().download(self.entryPath.get())#download
            new_name = os.path.splitext(out_path)#original name
            os.rename(out_path, new_name[0] + extension) 

            MessageBox.showinfo('','Done!')
            print('Finished')
        except:
            MessageBox.showerror('', 'Path or entry error!')

    def get_path(self):
        filename = filedialog.askdirectory()
        self.entry_path.insert(0,filename)
    
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
        return True

if __name__ == '__main__':
        window = ttk.Window()
        window.geometry('540x320')
        APP = UI(window)
        APP.mainloop()




