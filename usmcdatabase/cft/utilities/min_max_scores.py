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

def above_max_reps(age, gender, reps, event):
    max_score = event.query.filter((event.age == age)
                                   & (event.gender == gender)
                                   & (event.score == max_points)).first()
    return reps > max_score.reps

def below_min_reps(age, gender, reps, event):
        min_allowed = 60 if gender == "F" else 40
        min_score = event.query.filter((event.age == age)
                                         & (event.gender == gender)
                                         & (event.score == min_allowed)).first()
        return reps < min_score.reps
