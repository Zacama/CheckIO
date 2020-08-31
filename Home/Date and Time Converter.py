month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]


def date_time(time: str) -> str:
    result = ""
    mid1 = time[0:10].split(".")
    result += str(int(mid1[0]))
    result += " "
    result += month[int(mid1[1]) - 1]
    result += " "
    result += mid1[2]
    result += " year "
    result += str(int(time[11:13]))
    if str(int(time[11:13])) == "1":
        result += " hour "
    else:
        result += " hours "
    result += str(int(time[14:]))
    if str(int(time[14:])) == "1":
        result += " minute"
    else:
        result += " minutes"
    return result
