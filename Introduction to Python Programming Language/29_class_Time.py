class Time:
    """Time display.
        attributes: Hour, Minute, Second"""
time = Time()
time.hour = 9
time.minute = 36
time.second = 13

def print_time(t):
    """Display string of time."""
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))
    
# def add_time(t1, t2):
#     total = Time()
#     total.hour = t1.hour + t2.hour
#     total.minute = t1.minute + t2.minute
#     total.second = t1.second + t2.second
    
#     if total.second >= 60:
#         total.second -= 60
#         total.minute += 1
        
#     if total.minute >= 60:
#         total.minute -= 60
#         total.hour += 1
        
#     return total

def add_time(t1, t2):
    # if not correct_time(t1) or not correct_time(t2):
    #     raise ValueError('The time object is not correct.')
    assert correct_time(t1) and correct_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increase(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    return time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def correct_time(time):
    if time.hour < 0 or time.hour < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
