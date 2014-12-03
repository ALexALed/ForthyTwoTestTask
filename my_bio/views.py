from django.shortcuts import render_to_response

from models import MyBio, HttpRequestSave


def bio_home(request):
    bio_list = MyBio.objects.all()
    return render_to_response('bio/bio_index.html', {'bio_list': bio_list})

def requests(request):
    requests_list = HttpRequestSave.objects.all()[0:10]
    return render_to_response('bio/requests.html', {'requests_list': requests_list})