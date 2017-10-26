import time

'''import pyttsx
engine = pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()'''

'''import subprocess

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()

from gtts import gTTS
import os
tts = gTTS(text='Hello World', lang='en')
tts.save("hello.mp3")
play_mp3("hello.mp3")


from pygame import mixer # Load the required library
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()

import time
try:
    from google import search
except ImportError: 
    print("No module named 'google' found")
 
#GOOGLE SEARCH
start = time.time()
search_urls = search(bestguess, num=10, stop=1, pause=2)
print "\nGoogled in ",time.time() - start, " secs"

'''


'''
from google import search
import requests

for url in search(ip, stop=10):
            r = requests.get(url)
            title = everything_between(r.text, '<title>', '</title>')



'''



