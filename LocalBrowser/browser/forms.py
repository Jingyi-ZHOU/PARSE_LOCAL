from django import forms
from .models import Track

class DataTrackForm(forms.Form):
    track_list = forms.ModelMultipleChoiceField(queryset=Track.objects.all(), widget=forms.CheckboxSelectMultiple)



class FileUploadForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))