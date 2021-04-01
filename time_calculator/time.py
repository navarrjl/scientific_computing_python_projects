import math

def add_time(cur_time, time_add, day_of_week=" "):
    current_time, period = cur_time.split(' ')
    current_hour, current_minute = current_time.split(':')
    hour_to_add, minutes_to_add = time_add.split(':')
    day_of_week = day_of_week.lower()
    days_of_the_week = ["saturday", "sunday", 'monday', "tuesday", "wednesday",
                        "thursday", "friday"]

    if period == "AM":
        periods = 0
    elif period == "PM":
        periods = 1

    # converting the hours into minutes and casting the minutes
    total_minutes_std_hour = (int(current_hour.strip()) * 60)
    total_minutes_add_hours = (int(hour_to_add.strip()) * 60)
    std_minutes = int(current_minute.strip())
    add_minutes = int(minutes_to_add.strip())

    # total of hours combined
    total_minutes = int(total_minutes_std_hour + total_minutes_add_hours + std_minutes + add_minutes)
    total_minutes_left = int ((total_minutes_std_hour + total_minutes_add_hours + std_minutes + add_minutes) % 60)
    total_hours = total_minutes / 60

    periods += math.ceil(total_hours / 12)
    period_indicator = ' '
    if periods % 2 != 0:
        period_indicator = "AM"
    else:
        period_indicator = "PM"

    # data that will be printed in the clock
    clock_minutes = total_minutes_left

    if clock_minutes < 10:
        clock_minutes = '0' + str(clock_minutes)

    clock_hour = total_hours
    days = periods / 2
    day_message = 0

    if clock_hour >= 12:
        clock_hour = clock_hour % 12

        if (period_indicator == "PM" or period_indicator == "AM") and int(clock_hour) == 0:
            clock_hour = 12

    if float(days) <= 1:
        day_message = ""

    elif float(days) > 1 and days <= 2:
        day_message = "(next day)"

    elif days > 2:
        day_message = f"({str(int(days))} days later)"

    if day_of_week not in days_of_the_week:
        if day_message == "":
            returning_data = f"{str(int(clock_hour))}:{str(clock_minutes)} {period_indicator}"
        else:
            returning_data = f"{str(int(clock_hour))}:{str(clock_minutes)} {period_indicator} {day_message}"

    else:

        days = math.ceil(days)
        if day_of_week == "monday":
            day = (1 + days) % 7
            day_of_week = days_of_the_week[day].capitalize()

        elif day_of_week == "tuesday":
            day = (2 + days) % 7
            day_of_week = days_of_the_week[day].capitalize()

        elif day_of_week == "wednesday":
            day = (3 + days) % 7
            day_of_week = days_of_the_week[day].capitalize()

        elif day_of_week == "thursday":
            day = (4 + days) % 7
            day_of_week = days_of_the_week[day].capitalize()

        elif day_of_week == "friday":
            day = (5 + days) % 7
            day_of_week = days_of_the_week[day].capitalize()


        elif day_of_week == "saturday":
            day = (6 + days) % 7
            day_of_week = days_of_the_week[day].capitalize()

        else:
            day = days % 7
            day_of_week = days_of_the_week[day].capitalize()

        returning_data = f"{str(int(clock_hour))}:{str(clock_minutes)} {period_indicator}, {day_of_week} {day_message}"

    return returning_data