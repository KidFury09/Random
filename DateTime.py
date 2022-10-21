from time import localtime

def cust_time():
    local_time = localtime()
    year, month, date, hour, min, sec, day, day_no, tm_istd = local_time 
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = days[day]

    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September","October", "Novemnber", "December"]
    months = months[month-1]

    if date % 10 == 1:
        date = str(date) + "st"
    elif date % 10 == 2:
        date = str(date) + "nd"
    elif date % 10 == 3:
        date = str(date) + "rd"
    else: 
        date = str(date) + "th"
    
    return days, date, months, year
