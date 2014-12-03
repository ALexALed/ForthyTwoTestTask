from django.shortcuts import render, render_to_response

from models import MyBio

def bio_home(request):
    bio_list = MyBio.objects.all()
    return render_to_response('bio/bio_index.html', {'bio_list':bio_list})

#def requests(request):
