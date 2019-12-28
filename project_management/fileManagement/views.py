from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.generic import UpdateView
from webSite.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
import os


# Create your views here.

def download_media_doc1(request, name):

    file_path = os.path.join(settings.MEDIA_ROOT, 'doc1')
    file_path = os.path.join(file_path, name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="x-pdf")
            response['Content-Disposition'] = ('inline; filename=' +
                                               os.path.basename(file_path))
            return response
    raise Http404


def download_media_doc2(request, name):
    # pylint: disable=no-member

    # pylint: disable=no-member

    file_path = os.path.join(settings.MEDIA_ROOT, 'doc2')
    file_path = os.path.join(file_path, name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="x-pdf")
            response['Content-Disposition'] = ('inline; filename=' +
                                               os.path.basename(file_path))
            return response
    raise Http404


def download_guide(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'guide')
    file_path = os.path.join(file_path, 'guide.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="x-pdf")
            response['Content-Disposition'] = ('inline; filename='
                                               + os.path.basename(file_path))
            return response
    raise Http404


def download_form(request, name):

    file_path = os.path.join(settings.MEDIA_ROOT, 'add_user_forms')
    file_path = os.path.join(file_path, name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="x-pdf")
            response['Content-Disposition'] = ('inline; filename=' +
                                               os.path.basename(file_path))
            return response
    raise Http404


class upload_file(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ('research_subject', 'pdf', 'doc')
    model = Student
    context_object_name = 'student'
    template_name = 'upload_file.html'
    success_message = 'اطلاعات با موفقیت ذخیره شد'
