import qrcode
import subprocess
from win10toast import ToastNotifier

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from customtkinter import *
import os
import time
from PIL import Image, ImageFont, ImageDraw 
import packaging
import tkinter
import customtkinter
import locale


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")








rot = customtkinter.CTk()
rot.geometry("400x300")
rot.title("WIFI QR Generator by Potatox")
rot.iconbitmap('favicon.ico')
rot.resizable(0,0)

fontssss = customtkinter.CTkFont(family='ubuntu-medium.ttf', size=16)
language = "en_gb"

my_img = ")"


network_name = ("Wifi adını yazın: ")
my_text = "Your QR image has saved successfully !"
saveas = "Save as"
imgtext="WIFI Name: "
imgptext="Password: "
password = ""
passwordss = ""
ssid = ""
file_name = ""
file_name_path = "/"



def log():
    
    slidevalue = slider.get()
    
    
    print(file_name)
   
   


    resultss = subprocess.run(['netsh', 'wlan', 'show', 'interface', 'key=clear'], stdout=subprocess.PIPE)
    outputsads = resultss.stdout.decode()


    for line in outputsads.split('\r\n'):
         if "Profile" in line:
    
            passwordss = line.split(":")[1].strip()
    
   
    result = subprocess.run(['netsh', 'wlan', 'show', 'profile', passwordss, 'key=clear'], stdout=subprocess.PIPE)
    output = result.stdout.decode()
   
    for line in output.split('\n'):
       if "Key Content" in line:
        password = line.split(":")[1].strip()
       elif "Name" in line:
        ssid = line.split(":")[1].strip()




    root = tk.Tk()
    root.withdraw() #use to hide tkinter window

    currdir = os.getcwd()
    tempdir = filedialog.asksaveasfilename(parent=root, initialdir=currdir, title=saveas,defaultextension=".png",filetypes=(("PNG", "*.png"),("All Files", "*.*") ))
    
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
    font_family = 'fonts.otf'
    
    text = (imgtext + str(ssid))
    texts = (imgptext + str(password))
    a = 125/len(text)
    asak = 125/len(texts)


    font = ImageFont.truetype(r'fonts.otf', ((width/100)*a))
    fonts = ImageFont.truetype(r'fonts.otf', ((width/100)*asak))
    
    textwidth = draw.textlength(text, font=font)
    textwidths = draw.textlength(texts, font=fonts)

    x=width/2-textwidth/2
    xx=width/2-textwidths/2
    y = 0+((width/100)*3)
    yy=width - ((width/100)*7)
    

    draw.text((x, y), text, font=font, fill='black')
    draw.text((xx, yy), texts, font=fonts, fill='black')
   
    img.save(tempdir)
    a = str(tempdir)
    s = "/fdsdf.png"
   
    e = a.replace(s,'')
    esss = Image.open(tempdir)
    eks = e.replace('/', '\\')
    
    
    label1s.configure(text=my_text)
    
  
 
    
    
    
    
  
   
    if check.get() == True:
      os.startfile(tempdir, "print")
    if check1.get() == True:
      my_img=CTkImage(dark_image=Image.open(tempdir),size=(250,250))
      label1sss.configure(image=my_img)
      label1sss.pack_configure(side="bottom")
      rot.geometry("350x600")
    else:
      label1sss.configure(image="")   
      rot.geometry("350x300")
    
    rot.mainloop()  




frame = customtkinter.CTkFrame(master=rot)
frame.pack(pady=20, padx=20, fill="both", expand=True)


  
# Show image using label 


label = customtkinter.CTkLabel(master=frame, text="WIFI QR Generator",font=fontssss)
label.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Generate", command=log,font=fontssss)
button.pack(pady=12,padx=10)

check = customtkinter.CTkCheckBox(master=frame,text="Print QR",font=fontssss)
check.pack(pady=6,padx=10)
check1 = customtkinter.CTkCheckBox(master=frame,text="Show QR Image",font=fontssss)
check1.pack(pady=6,padx=10)


label1 = customtkinter.CTkLabel(master=frame, text="Quality",font=fontssss)
label1.pack(pady=0,padx=10)


slider = customtkinter.CTkSlider(master=frame,from_=10,to=100)
slider.pack(pady=12,padx=10)

label1s = customtkinter.CTkLabel(master=frame, text="",text_color="green",font=fontssss)
label1s.pack(pady=0,padx=10)

label1sss = customtkinter.CTkLabel(master=frame, text="",text_color="green",image="",font=fontssss)
label1sss.pack(pady=10,padx=10)

if language == "tr_TR":
   label.configure(text="WIFI QR Oluşturucu")
   button.configure(text="Oluştur")
   check.configure(text="Yazdır")
   check1.configure(text="QR'ı Göster")
   label1.configure(text="Görsel Kalitesi")
   my_text="QR görseliniz başarıyla kaydedildi !"
   saveas ="Farklı kaydet"
   imgtext = "WIFI Adı: "
   imgptext = "Şifre: "
elif language == "en" or language == "en_us" or language == "en_gb" or language == "en_tt" or language == "en_za" or language == "en_nz" or language == "en_jm" or language == "en_ie" or language == "en_ca" or language == "en_au" or language == "en_bz":
   label.configure(text="WIFI QR Generator")
   button.configure(text="Generate")
   check.configure(text="Print QR")
   check1.configure(text="Show QR")
   label1.configure(text="Image Quality")
   my_text="Your QR image has saved successfully !"
   saveas ="Save as"
   imgtext = "WIFI Name: "
   imgptext = "Password: "



rot.mainloop()
