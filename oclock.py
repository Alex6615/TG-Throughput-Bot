import time
from datetime import datetime



def isoclock() -> bool: 
    nows = int(time.time())
    dt = datetime.fromtimestamp(nows)
    if dt.minute == 0 or dt.minute == 10 or dt.minute == 20 or dt.minute == 30 or dt.minute == 40 or dt.minute == 50 :
        return True
    else :
        return False