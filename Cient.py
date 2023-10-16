import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path
from ftplib import FTP
from pathlib import Path

from tkinter import filedialog
from pathlib import Path
global infolabel
global song_selected
from playsound import playsound
import pygame
from pygame import mixer

global song_counter
song_counter=0

for i in os.listdir("shared_files"):
    filename=os.decode(i)
    Listbox.insert(song_counter,filename)
    song_counter+=1

def play():
    global song_selected
    song_selected=Listbox.get(ANCHOR)
    mixer.music.load("shared_files/",song_selected)
    mixer.init()
    if(song_selected != ""):
        infolabel.configure(text="Now playing"+song_selected)
    else:
        print("not playing")

def stop():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/",song_selected)
    mixer.music.pause()
    infolabel.configure(text="")
    
def resume():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/",song_selected)
    mixer.music.resume()
   

def pause():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/",song_selected)
    mixer.music.pause()
   

resumeButton=Button(text="Resume",command=resume)
resumeButton.place(x=50,y=200)

pauseButton=Button(text="Pause",command=pause)
pauseButton.place(x=70,y=240)

def browseFiles():
    global sending_file
    global textarea
    global filePathLabel

    try:
        filename = filedialog.askopenfilename()
        filePathLabel.configure(text=filename)
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"

        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        fname=ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)
        

        ftp_server.dir()
        ftp_server.quit()

        message="send"+fname
        if(message[:4]=="send"):
            print("please wait /n ")
            textarea.insert(END,"/n" + "/n pls wait/n")
            textarea.see("end")
            sending_file=message[5:]

            file_size=getFileSize("shared_files/"+sending_file)
            final_message=message+" "+str(file_size)
            SERVER.send(final_message.encode())
            textarea.insert(END,"file succesfully sent")  
            Listbox.insert(song_counter,fname)
            song_counter+=1

    except FileNotFoundError:
        print("Cancel Button Pressed")

def download():
        song_to_download=Listbox.get(song_counter)

        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"

        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        fname=ntpath.basename(filename)
        home =str(Path.home())
        download_path=home+"/downloads"

        ftp_server=ftplib.FTP(HOSTNAME,USERNAME,PASSWORD)
        ftp_server.encoding="utf-8"
        ftp_server.cwd="shared_files"
        fname=ntpath.basename(filename)
        ftp_server.dir()
        ftp_server.quit()
