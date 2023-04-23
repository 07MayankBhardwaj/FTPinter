import tkinter
import os
from tkinter import BOTH, END, LEFT
from tkinter import filedialog
import ftplib
from stegano import lsb  
from PIL import Image, ImageTk
import tkinter as tk



ftp = ftplib.FTP()


def connectServer():
    ip = ent_ip.get()
    port = int(ent_port.get())
    try:
        msg = ftp.connect(ip,port)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        lbl_login.place(x=150,y=20)
        ent_login.place(x=150,y=40)
        lbl_pass.place(x=150,y=60)
        ent_pass.place(x=150,y=80)
        btn_login.place(x=182,y=110)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to connect")

def loginServer():
    user = ent_login.get()
    password = ent_pass.get()
    try:
        msg = ftp.login(user,password)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        displayDir()
        lbl_login.place_forget()
        ent_login.place_forget()
        lbl_pass.place_forget()
        ent_pass.place_forget()
        btn_login.place_forget()
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to login")

        
def displayDir():
    libox_serverdir.insert(0,"--------------------------------------------")
    dirlist = []
    dirlist = ftp.nlst()
    for item in dirlist:
        libox_serverdir.insert(0, item)

#FTP commands
def changeDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.cwd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to change directory")
    displayDir()

def createDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.mkd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to create directory")
    displayDir()
    
def deleteDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.rmd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to delete directory")
    displayDir()
    
def deleteFile():
    file = ent_input.get()
    try:
        msg = ftp.delete(file)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to delete file")
    displayDir()
    
def downloadFile():
    file = ent_input.get()
    down = open("download/" + file, "wb")
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Downloading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.retrbinary("RETR " + file, down.write))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to download file")
    displayDir()

    
from tkinter import filedialog

def uploadFile():
    # Open a file dialog box to select a file for upload
    file = filedialog.askopenfilename()
    try:
        up = open(file, "rb")
        # Get the name of the file without the path
        filename = os.path.basename(file)
        # Set the remote directory to "received" folder
        ftp.cwd("received")
        # Upload the file to the "received" folder of the FTP server
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Uploading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END, ftp.storbinary("STOR " + filename, up))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to upload file")


    
def closeConnection():
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Closing connection...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.quit())
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to disconnect")

window = tkinter.Tk()
window.title("(Client-Side)FTPinter 📥 ~ by Mayank Bhardwaj")
#window.wm_iconbitmap("favicon.ico")
window.geometry("1200x600")

#logo
# img = ImageTk.PhotoImage(img)
# logo = PhotoImage(file="logo.png")
# Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

# Label(root, text="CYBER SCIENCE", bg="#2f4155", fg="white", font="arial 25 bold").place(x=100, y=20)

#Connect
lbl_ip = tkinter.Label(window, text="✈ IP Address")
ent_ip = tkinter.Entry(window)
lbl_port = tkinter.Label(window, text="🌐 Port")
ent_port = tkinter.Entry(window)
btn_connect = tkinter.Button(window, text="➕ Connect", command=connectServer)

#Server response text box
text_servermsg = tkinter.Text(window)

#Login
lbl_login = tkinter.Label(window, text="Username")
ent_login = tkinter.Entry(window)
lbl_pass = tkinter.Label(window, text="Password")
ent_pass = tkinter.Entry(window)
btn_login = tkinter.Button(window, text="Login", command=loginServer)

#Directory listing
lbl_dir = tkinter.Label(window, text="✔ Directory listing:")
libox_serverdir = tkinter.Listbox(window,width=40,height=14)

#Options
lbl_input = tkinter.Label(window, text="⬇ Input")
ent_input = tkinter.Entry(window)
btn_chdir = tkinter.Button(window, text="⤵ Change Directory", command=changeDirectory,width=15)
btn_crdir = tkinter.Button(window, text="⭐ Create Directory", command=createDirectory,width=15)
btn_deldir = tkinter.Button(window,text="🆘 Delete Directory", command=deleteDirectory,width=15)
btn_delfile = tkinter.Button(window,text="❌ Delete File", command=deleteFile,width=15)
btn_downfile = tkinter.Button(window, text=" ❤ Download File", command=downloadFile,width=15)
btn_upfile = tkinter.Button(window, text="✅ Upload File", command=uploadFile,width=15)
btn_quit = tkinter.Button(window, text="⚡ Disconnect", command=closeConnection,width=15)

#Place widgits
lbl_ip.place(x=20,y=20)
ent_ip.place(x=20,y=40)
lbl_port.place(x=20,y=60)
ent_port.place(x=20,y=80)
btn_connect.place(x=52,y=110)
text_servermsg.place(x=20,y=150)

lbl_dir.place(x=700,y=143)
libox_serverdir.place(x=700,y=165)

lbl_input.place(x=700,y=400)
ent_input.place(x=700,y=420)
btn_chdir.place(x=700,y=450)
btn_crdir.place(x=700,y=480)
btn_deldir.place(x=700,y=510)
btn_delfile.place(x=700,y=540)

btn_downfile.place(x=850,y=450)
btn_upfile.place(x=850,y=480)
btn_quit.place(x=850,y=510)


#Create
window.mainloop()