def sun_angle(time):
    all_time = 12 * 60 * 60
    if int(time[0:2]) == 18 and int(time[3:5]) > 0:
        return "I don't see the sun!"
    elif int(time[0:2]) < 6:
        return "I don't see the sun!"
    else:
        return round(((int(time[0:2]) - 6) * 60 * 60 + int(time[3:5]) * 60) / all_time * 180, 2)
