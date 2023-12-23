import qrcode
import subprocess
from win10toast import ToastNotifier

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
import time
from PIL import Image, ImageFont, ImageDraw 
import packaging
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


rot = customtkinter.CTk()
rot.geometry("500x350")
rot.title("WIFI QR Generator by Potatox")
rot.iconbitmap('favicon.ico')


network_name = ("Wifi adını yazın: ")


password = ""
ssid = ""



def log():
    network_name=entry1.get()
    slidevalue = slider.get()

    result = subprocess.run(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    for line in output.split('\n'):
       if "Key Content" in line:
        password = line.split(":")[1].strip()
       elif "Name" in line:
        ssid = line.split(":")[1].strip()




    root = tk.Tk()
    root.withdraw() #use to hide tkinter window

    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Choose save path')
    tempdir += "/qrwifi.png"

    esek="WIFI:S:SSID_NAME;H:true;T:WPA2;P:PASSWORD;;"
    qr =esek.replace("SSID_NAME", str(ssid))
    qrtu=qr.replace("PASSWORD", str(password))

    qrs = qrcode.QRCode(
       version=1,
       error_correction=qrcode.constants.ERROR_CORRECT_L,
       box_size=slidevalue,
       border=4,
    )
    qrs.add_data(qrtu)
    qrs.make(fit=True)

    img = qrs.make_image(fill_color="black", back_color="white")



    type(img)  # qrcode.image.pil.PilImage
    width, height = img.size 
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'fonts.otf', ((width/100)*6))
    text = ("WIFI Name: " + str(ssid))
    texts = ("Password: " + str(password))
    textwidth = draw.textlength(text, font=font)
    textwidths = draw.textlength(texts, font=font)

    x=width/2-textwidth/2
    xx=width/2-textwidths/2
    y = 0+((width/100)*3)
    yy=width - ((width/100)*7)
    print(draw.textlength(text, font=font))

    draw.text((x, y), text, font=font, fill='black')
    draw.text((xx, yy), texts, font=font, fill='black')
    img.save(tempdir)
    
    
    
    
    
  
    toast = ToastNotifier()
    toast.show_toast(
       "Wifi QR Generator",
       "Your QR code has saved sucessfully !",
       duration = 5,
       threaded = False,
       icon_path='favicon.ico'
    )
    if check.get() == True:
      os.startfile(tempdir, "print")
    rot.mainloop()  
frame = customtkinter.CTkFrame(master=rot)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="WIFI QR Generator")
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="WIFI Name :")
entry1.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Generate", command=log)
button.pack(pady=12,padx=10)

check = customtkinter.CTkCheckBox(master=frame,text="Print QR")
check.pack(pady=12,padx=10)

label1 = customtkinter.CTkLabel(master=frame, text="Quality")
label1.pack(pady=0,padx=10)

slider = customtkinter.CTkSlider(master=frame,from_=10,to=50)
slider.pack(pady=12,padx=10)











rot.mainloop()
