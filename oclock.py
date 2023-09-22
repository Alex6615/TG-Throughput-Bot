import time
from datetime import datetime



def isoclock() -> bool: 
    nows = int(time.time())
    dt = datetime.fromtimestamp(nows)
    if dt.minute == 0 :
        return True
    else :
        return False
    
def minuteisfive() -> bool: 
    nows = int(time.time())
    dt = datetime.fromtimestamp(nows)
    if dt.minute % 5 == 0 :
        return True
    else :
        return False
    
def minuteisten() -> bool: 
    nows = int(time.time())
    dt = datetime.fromtimestamp(nows)
    if dt.minute % 10 == 0 :
        return True
    else :
        return False