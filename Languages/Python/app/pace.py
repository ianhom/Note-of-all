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
    return (t/100*3600+t%100*60)

def cal_pace(d,t_str):
    t = time_sec(t_str)
    return (t*1.00/d)

def three_pace(t_str):
    return cal_pace(3.0,t_str)

def five_pace(t_str):
    return cal_pace(5.0,t_str)

def ten_pace(t_str):
    return cal_pace(10.0,t_str)

def half_pace(t_str):
    return cal_pace(21.1,t_str)

def full_pace(t_str):
    return cal_pace(42.2,t_str)

def pace_to_speed(t_str):
    t = pace_sec(t_str)
    return (3600*1.00/t)

def pace_readable(p):
    return (int(p/60)*100+p%60)

def speed_to_pace(sp_str):
    sp = round(sp_str,2)
    return int(pace_readable(int(3600.00/sp)))
    
    
if __name__ == '__main__':
    print(pace_sec(400))
    print(half_pace(200))
    print(full_pace(400))
    print(pace_to_speed(400))
    print(speed_to_pace(13.0))
