import datetime
from datetime import datetime, timedelta



def ts_generator(range = 1):
    # now
    now = datetime.now()
    now_ts = str(round(now.timestamp())) + "000"
    
    # now - 1hour
    before_1_hour = datetime.now() - timedelta(hours=range)
    before_ts = str(round(before_1_hour.timestamp())) + "000"
   
    return now_ts, before_ts

if __name__ == "__main__" :
    x, y = ts_generator(range = 1)
    print(x)
    print(y)