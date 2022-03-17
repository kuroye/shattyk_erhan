from django.shortcuts import render
from utils import data

# Create your views here.

def index(request):

    if request.method == 'GET':

        time_list = data.get_time()

        schedule = data.Schedule('9:00', '10:00')
        schedule_dict = schedule.get_schedule()

        return render(request, 'index.html', context={'time_list': time_list,
                                                      'schedule': schedule_dict})