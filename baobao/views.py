from django.shortcuts import render
from utils import data
from .models import Schedule


# Create your views here.

def index(request):
    if request.method == 'GET':
        time_list = data.get_time()
        week_list = data.get_week()
        print(week_list)
        # Schedule.objects.create(start_time='12:00', end_time='14:00', day_of_the_week=7)
        schedules = Schedule.objects.all()
        print(schedules)

        return render(request, 'index.html', context={'time_list': time_list,
                                                      'week_list': week_list,
                                                      'schedules': schedules, })
