def get_time():
    time_list = []
    for x in range(24):
        t = x + 6
        if t >= 24:
            t = t - 24
        time = str(t) + ':00'
        time_list.append(time)
        time = str(t) + ':30'
        time_list.append(time)

    return time_list


def get_week():
    week_list = []

    for x in range(7):
        t = x + 1

        week_list.append(t)

    return week_list
