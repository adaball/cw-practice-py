"""https://www.codewars.com/kata/52685f7382004e774f0001f7"""

def make_readable(s):
    hours = int(s / 60 / 60)
    minutes = int(s / 60) - (hours * 60)
    seconds = s - (minutes * 60) - (hours * 60 * 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
