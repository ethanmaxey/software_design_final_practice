from worldtime_unixtime import get_unixtime 

try:
    print(f"Unix time is {get_unixtime()}")
except Exception as Y:
    print(f"Error: {Y}")
