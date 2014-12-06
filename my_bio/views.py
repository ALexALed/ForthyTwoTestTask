from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import Http404

from models import MyBio, HttpRequestSave
from forms import MyBioForm


def bio_home(request):
    login_status = request.user.is_authenticated()
    user = request.user
    bio_list = MyBio.objects.all()
    return render_to_response('bio/bio_index.html', {'bio_list': bio_list,
                                                     'user': user,
                                                     'login_status': login_status},
                              context_instance=RequestContext(request))


def requests(request):
    requests_list = HttpRequestSave.objects.all()[0:10]
    return render_to_response('bio/requests.html',
                              {'requests_list': requests_list},
                              context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def edit_bio_data(request, bio_pk=None):
    if not bio_pk:
        raise Http404
    bio_obj = get_object_or_404(MyBio, pk=int(bio_pk))
    if request.method == 'POST':
        form = MyBioForm(request.POST, request.FILES, instance=bio_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        if bio_pk:
            form = MyBioForm(instance=bio_obj)
        else:
            form = MyBioForm()
    return render_to_response("bio/bio_edit.html",
                              {"form": form, "pk": bio_pk, "bio": bio_obj},
                              context_instance=RequestContext(request))