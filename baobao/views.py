from django.shortcuts import render
from utils import data
from .models import Schedule


# Create your views here.

def index(request):
    if request.method == 'GET':
        time_list = data.get_time()

        schedules = Schedule.objects.all()
        print(schedules)


        return render(request, 'index.html', context={'time_list': time_list,
                                                      'schedules': schedules})
