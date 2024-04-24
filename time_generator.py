import datetime
from datetime import datetime, timedelta



def ts_generator(range = 10):
    # now
    now = datetime.now()
    now_ts = str(round(now.timestamp())) + "000"

    # now - minutes
    #before_1_hour = datetime.now() - timedelta(hours=range)
    before_minutes = datetime.now() - timedelta(minutes=range)
    before_ts = str(round(before_minutes.timestamp())) + "000"

    return now_ts, before_ts

if __name__ == "__main__" :
    x, y = ts_generator(range = 1)
    print(x)
    print(y)