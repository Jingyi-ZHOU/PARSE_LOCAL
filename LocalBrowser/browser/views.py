from django.shortcuts import render, redirect
from .forms import DataTrackForm, FileUploadForm
from .runbash import ManageGiveData
from .models import Track
from django.conf import settings
import os
import glob


def home(request):
    return render(request,'browser/home.html', {'title':'Home'})

def browser(request):
    data = Track.objects.all()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('files')
            editor = ManageGiveData()
            for f in files:
                file_path = os.path.join(settings.FILES_DIR, f.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                file_type = f.name.split('.')[-1]
                track_name = f.name[:-1-len(file_type)]
                if not Track.objects.filter(track_name=track_name).exists():
                    new_track = Track(track_name=track_name)
                    new_track.save()
                    editor.add(file_type, track_name, file_type, track_name, f.name)
    else:
        form = FileUploadForm()
    
    give_url = '../panel'
    
    context = {
        'title':'Browser', 
        'give_url':give_url,
        'form': form,
    }
    return render(request, 'browser/browser.html', context) 


def about(request):
    return render(request, 'browser/about.html', {'title':'About'})

def contact(request):
    return render(request, 'browser/contact.html', {'title':'Contact'})


def panel(request):
    all_tracks = Track.objects.all()

    # display all tracks
    tracks = ['\"'+str(track)+'\",' for track in all_tracks]
    if len(tracks) > 0:
        tracks[-1] = tracks[-1][:-1]
    context = {
        'title':'GIVE-Panel',
        'tracks': tracks
    }
    return render(request, 'browser/give_panel.html', context)


def reset(request):
    Track.objects.all().delete()
    editor = ManageGiveData()
    editor.delete_all()
    files = glob.glob(settings.FILES_DIR+'/*')
    for f in files:
        if f.endswith('cytoBandIdeo.txt'):
            continue
        os.remove(f)
    return redirect(browser)


    

