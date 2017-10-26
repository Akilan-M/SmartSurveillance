from pygame import mixer # Load the required library
from gtts import gTTS
import sys
import os
import time
import subprocess
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


tts = gTTS(text="Please Wait till the Surveillance System processes the footage.", lang='en')
tts.save("WaitPlease.mp3")
mixer.init()
mixer.music.load('WaitPlease.mp3')
mixer.music.play()

start = time.time()
startTimeOfProgram = start

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


# Try to load saved client credentials
#gauth.LoadCredentialsFile("mycreds.txt")
'''if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
'''
drive = GoogleDrive(gauth)
print "\nGAuth completed in ",time.time() - start," secs\n"


#SmartSurveillancePictures Folder ID is FID
#fid='0B2GsqFJywF-5cjVEMjEza0tvUWM'

# ********************* PLACE YOUR GOOGLE DRIVE FOLDER ID in FID variable*******************
# ***************** THAT FOLDER CONTAINS THE TEST PICTURE for DEEP SEARCH*****************
fid='0B1dCjysAJ-_cLURxOWFKMnZzeDg'  

#DELETE EXISTING FILEs
start = time.time()
file_list = drive.ListFile({'q': "'"+fid+"' in parents and trashed=false"}).GetList()
for file1 in file_list:
	file1.Delete()
print "\nDeleted Old files in ",time.time() - start," secs\n"

#GET FIRST IMAGE in PicturesToBeUploaded
#path = '/home/aki/Downloads/SmartSurveillanceProject/WorkingDirectory/PicturesToBeUploaded/'
path = 'PicturesToBeUploaded/'
imageToUpload = os.listdir(path)[0];



#Upload image
start = time.time()
f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
f.SetContentFile('PicturesToBeUploaded/'+imageToUpload)
f['title'] = 'CurrentPic.jpg'
f.Upload()
print "\nUploaded New Image in ",time.time() - start," secs\n"

#ImageID 
imageID = f['id']

start = time.time()
bestguess = subprocess.check_output([sys.executable, "Unsantizied_best_guess.py", "https://drive.google.com/uc?id="+imageID]).strip()
print bestguess
print "\nBest Guess in ",time.time() - start, " secs\n"

#GOOGLE SEARCH
'''

try:
    from google import search
except ImportError: 
    print("No module named 'google' found")
 
#GOOGLE SEARCH
start = time.time()
search_urls = search(bestguess, num=10, stop=1, pause=2)
print "\nGoogled in ",time.time() - start, " secs"
'''
#SPEECH
import subprocess

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()


import os


#G U I

from Tkinter import *

def onclick():
   pass
start = time.time()
import wikipedia
contentToSpeak = "Surveillance System has identified the object as "+ bestguess;
root = Tk()
root.attributes("-fullscreen", True)
text = Text(root)
text.config(width=200,height=200)
text.config(font=("Arial", 30))

contentToSpeak+= ". And Wikipedia says " + wikipedia.summary(bestguess, sentences=1) + ". And blablabla, you can read it yourself! ";
text.insert(INSERT, "\n"+bestguess+"\n")
text.insert(INSERT, "\nWikipedia says : \n\n" + wikipedia.summary(bestguess, sentences=3))
contentToSpeak+= ". And As you can see, there are few Google Search results too";
text.insert(INSERT, "\n\nGoogle search results : \n\n")
#for url in search_urls:
#	text.insert(INSERT, url + "\n")
text.insert(END, "\nWanna know more about, \""+ bestguess + "\" Wait for the next version :-)");
contentToSpeak+= ". So, If you wanna do deeper search, wait for our next version. Bye Bye. By the Team of. Aki, Abi, CV and Sindhu. Have a good day. ";
print "\nWikipediaed in ",time.time() - start," secs"
text.pack()


tts = gTTS(text=contentToSpeak, lang='en')
tts.save("contentToSpeak.mp3")
#play_mp3("contentToSpeak.mp3")


mixer.init()
mixer.music.load('contentToSpeak.mp3')
mixer.music.play()

print "\nProgram completed : ", time.time()-startTimeOfProgram, " secs\n"
root.mainloop()










