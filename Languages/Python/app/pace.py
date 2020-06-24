#!/usr/bin/python
def pace_int(p_str):
    return int(p_str)
    
def time_int(t_str):
    return int(t_str)

def pace_sec(p_str):
    p = pace_int(p_str)
    return (p/100*60+p%60)
    
if __name__ == '__main__':
    pace_sec(400)
