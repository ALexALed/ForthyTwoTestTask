import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, \
    get_object_or_404, HttpResponse
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import Http404
import simplejson

from models import MyBio, HttpRequestSave
from forms import MyBioForm


def bio_home(request):
    login_status = request.user.is_authenticated()
    user = request.user
    bio_list = MyBio.objects.all()
    return render_to_response('bio/bio_index.html',
                              {'bio_list': bio_list,
                               'user': user,
                               'login_status': login_status},
                              context_instance=RequestContext(request))


def requests(request):
    requests_list = HttpRequestSave.objects.order_by('-priority')[0:10]
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
    if request.POST:
        # 3 sec sleep for ajax submit
        if request.is_ajax():
            time.sleep(3)
        form = MyBioForm(request.POST, request.FILES, instance=bio_obj)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                json_result = simplejson.dumps({'status': "done_status"})
            else:
                return redirect('home')

        else:
            if request.is_ajax():
                error_list = []
                for err in form.errors:
                    error_list.append(err)

                json_result = simplejson.dumps({'status': 'fail_status',
                                                'errors':
                                                    ",".join(error_list)})
        if request.is_ajax():
            return HttpResponse(json_result)
    else:
        if bio_pk:
            form = MyBioForm(instance=bio_obj)
        else:
            form = MyBioForm()
    return render_to_response("bio/bio_edit.html",
                              {"form": form, "pk": bio_pk, "bio": bio_obj},
                              context_instance=RequestContext(request))
