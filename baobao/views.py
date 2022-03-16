from django.shortcuts import render
from utils import data

# Create your views here.

def index(request):

    if request.method == 'GET':

        time_list = data.get_time()

        return render(request, 'index.html', context={'time_list': time_list})