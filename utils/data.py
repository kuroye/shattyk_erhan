
def get_time():

    time_list = []
    for x in range(24):
        t = x+6
        if t >= 24:
            t = t-24
        time = str(t) + ':00'
        time_list.append(time)
        time = str(t) + ':30'
        time_list.append(time)

    return time_list

class Schedule:
    def __init__(self, _start_time, _end_time, _day_of_the_week):
        self.start_time = _start_time
        self.end_time = _end_time
        self.day_of_the_week = _day_of_the_week

    def get_schedule(self):
        dict = {'start_time': self.start_time,
                'end_time': self.end_time,
                'day_week': self.day_of_the_week}
        return dict
