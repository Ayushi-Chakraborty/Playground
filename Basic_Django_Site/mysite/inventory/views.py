from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Server Inventory page.. Development is in progress..")

from .models import Hostname

class HostnameListView(ListView):
    model = Hostname
    template_name = 'host.html'
