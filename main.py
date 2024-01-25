import qrcode
import subprocess

import warnings
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


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")






warnings.simplefilter("ignore")


rot = customtkinter.CTk()
rot.geometry("350x310")
rot.title("WIFI QR Generator by Potatox")
rot.iconbitmap('favicon.ico')
rot.resizable(0,0)


def close():
   rot.quit()

rot.protocol("WM_DELETE_WINDOW", close)

fontssss = customtkinter.CTkFont(family='fontui.ttf', size=16)
language = locale.getdefaultlocale()[0]

my_img = ")"


network_name = ("Wifi adını yazın: ")
my_text = "Your QR image has saved successfully !"
my_fail_text = "You don't have any connection on wifi"
my_failfile_text = "Please select directory"
saveas = "Save as"
imgtext="WIFI Name: "
imgptext="Password: "
password = ""
passwordss = ""
ssid = ""
file_name = ""
file_name_path = "/"
currdir = ""
tempdir = ""


checksss=False
def getnet():
   resultss = subprocess.run(['netsh', 'wlan', 'show', 'interface', 'key=clear'], stdout=subprocess.PIPE)
   outputsads = resultss.stdout.decode()
   durum = False
   global currdir
   global tempdir
   for line in outputsads.split('\r\n'):
         if "Profile" in line:
            
            passwordss = line.split(":")[1].strip()
            checksss = True
         elif "State" in line:
            durum = line.split(":")[1].strip()
   
   if durum == "connected":
      result = subprocess.run(['netsh', 'wlan', 'show', 'profile', passwordss, 'key=clear'], stdout=subprocess.PIPE)
      output = result.stdout.decode()
   
      for line in output.split('\n'):
        if "Key Content" in line:
          global password
          password = line.split(":")[1].strip()
        elif "Name" in line:
          global ssid
          ssid = line.split(":")[1].strip()
   
   
      root = tk.Tk()
      root.withdraw() #use to hide tkinter window

      currdir = os.getcwd()
      tempdir = filedialog.asksaveasfilename(parent=root, initialdir=currdir, title=saveas,defaultextension=".png",filetypes=(("PNG", "*.png"),("All Files", "*.*") ))
      
      log()
   elif durum == "disconnected":   
      label1s.configure(text=my_fail_text,text_color="darkgoldenrod1")

      


def log():
    
 slidevalue = slider.get()
 global ssid
 global password

 global currdir
 global tempdir
 
 if tempdir == "":
    label1s.configure(text=my_failfile_text,text_color="darkgoldenrod1")
 if tempdir != "":
    


    




    
    
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
    font_family = 'fontimage.otf'
    
    text = (imgtext + str(ssid))
    texts = (imgptext + str(password))
    a = 125/len(text)
    asak = 125/len(texts)


    font = ImageFont.truetype(r'fontimage.otf', ((width/100)*a))
    fonts = ImageFont.truetype(r'fontimage.otf', ((width/100)*asak))
    
    textwidth = draw.textlength(text, font=font)
    textwidths = draw.textlength(texts, font=fonts)
    
    ascent, descent = font.getmetrics()

   
    text_height = font.getmask(text).getbbox()[3] + descent
    text_heights = font.getmask(texts).getbbox()[3] + descent
    print(text_height,textwidth)
    x=width/2-textwidth/2
    xx=width/2-textwidths/2
    y = (height/10)/2 - text_height/2
    yy= (height*0.9)+((height/10)/2 - text_height/2)
    

    draw.text((x, y), text, font=font, fill='black')
    draw.text((xx, yy), texts, font=fonts, fill='black')
   
    img.save(tempdir)
    a = str(tempdir)
    s = "/fdsdf.png"
   
    e = a.replace(s,'')
    esss = Image.open(tempdir)
    eks = e.replace('/', '\\')
    
    
    label1s.configure(text=my_text,text_color="green")
    
  
 
    
    
    
    
  
   
    if check.get() == True:
      os.startfile(tempdir, "print")
    if check1.get() == True:
     
      rot.geometry("350x600")
      
      
      
      my_img=CTkImage(dark_image=Image.open(tempdir),size=(250,250))
      label1sss.configure(image=my_img)
      label1sss.pack_configure(side="bottom")
    else:
      label1sss.configure(image="")   
      rot.geometry("350x310")
    
    rot.mainloop()  
def showclose():
   if check1.get() == False:
      label1sss.configure(image="")   
      rot.geometry("350x310")
      label1s.configure(text="")


frame = customtkinter.CTkFrame(master=rot)
frame.pack(pady=20, padx=20, fill="both", expand=True)


  
# Show image using label 


label = customtkinter.CTkLabel(master=frame, text="WIFI QR Generator",font=fontssss)
label.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Generate", command=getnet,font=fontssss)
button.pack(pady=12,padx=10)

check = customtkinter.CTkCheckBox(master=frame,text="Print QR",font=fontssss)
check.pack(pady=6,padx=10)
check1 = customtkinter.CTkCheckBox(master=frame,text="Show QR Image",font=fontssss,command=showclose)
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
   my_fail_text = "Şu anda bir wifi ağına bağlı değilsiniz"
   my_failfile_text = "Lütfen dosya dizinini seçiniz"
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
   my_fail_text = "You don't have any connection on wifi"
   my_failfile_text = "Please select file directory"
   saveas ="Save as"
   imgtext = "WIFI Name: "
   imgptext = "Password: "



rot.mainloop()
