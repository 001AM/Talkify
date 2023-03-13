from django.shortcuts import render
from django.http import HttpResponse
from Talkify import forms
from gtts import gTTS
import os
import shutil
import random
import string

def index(request):
    template='index.html',      
    data={
        'title':'TALKIFY',
        'head1':'Enter the text ...',   
        'head2':'Upload the file ...',
        'about':'ABOUT',
        'main':'MAIN',
        'p':'Talkify is a website where we convert input text and text files to audio. You can also download the audio. With help of python ppytx lib.With Django backend.'
    }

    return render(request, template , data)

def tts(request):
    template = 'tts.html'
    try:
        if request.method == 'POST':
            letters = string.ascii_lowercase
            file_name = f"{''.join(random.choice(letters) for i in range(10))}.mp3"
            txt = (request.POST.get('text'))
           
            myobj = gTTS(text= txt, lang= 'en' , slow=False)
            myobj.save(file_name)
            dir = os.getcwd()
            full_dir = os.path.join(dir,file_name)
            dest = shutil.move(full_dir, os.path.join(dir, "Talkify\static"))
            
        data = {
            'h': file_name,
        }
        return render(request,template,data)
     
       
    except:
        pass
