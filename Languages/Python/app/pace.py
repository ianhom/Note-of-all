#!/usr/bin/python
def pace_int(p_str):
    return int(p_str)
    
def time_int(t_str):
    return int(t_str)

def pace_sec(p_str):
    p = pace_int(p_str)
    return (p/100*60+p%100)

def time_sec(t_str):
    t = time_int(t_str)
    return (p/100*3600+p%100*60)

def cal_pace(d,t_str):
    t = time_sec(t_str)
    return (t*1.00/d)

def half_pace(t_str):
    return cal_pace(21.1,t_str)

def full_pace(t_str):
    return cal_pace(42.2,t_str)

def pace_speed(t_str):
    t = pace_sec(t_str)
    return (3600*1.00/t)
    
if __name__ == '__main__':
    pace_sec(400)
    half_pace(200)
    full_pace(400)
    pace_speed(400)
