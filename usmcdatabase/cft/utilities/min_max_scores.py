from cft.models import *
def faster_than_max_time(age, gender, time, high_alt, event):
    max_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.high_alt == high_alt)
                                   & (event.score == 100)).first()
    return time < max_score.time

def slower_than_min_time(age, gender, time, high_alt, event):
    min_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.high_alt == high_alt)
                                   & (event.score == 40)).first()
    return time > min_score.time


