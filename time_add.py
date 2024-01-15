from datetime import datetime, timezone
def time_add():
    utc_dt = datetime.now(timezone.utc)
    dt = utc_dt.astimezone()
    if len(str(dt.day)) != 2:
        result =  (f"0{dt.day}.{dt.month}.{dt.year}             {dt.strftime("%H:%M:%S")}")
    if len(str(dt.month)) != 2:
        result =  (f"{dt.day}.0{dt.month}.{dt.year}             {dt.strftime("%H:%M:%S")}")
    return result
