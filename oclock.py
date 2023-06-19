import time
from datetime import datetime



def isoclock() -> bool: 
    nows = int(time.time())
    dt = datetime.fromtimestamp(nows)
    if dt.minute == 0 :
        return True
    else :
        return False