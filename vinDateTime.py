from datetime import datetime

def getDateTimeWeekday() -> str:
    """
    returns STR as:
        0 1 2 3 : YEAR
        4 5     : MONTH
        6 7     : DAY

        8 9     : HOUR
        10 11   : MINUTE
        12 13   : SECOND
        
        14      : WEEKDAY

    where weekday is:
        0 = monday, 1 = tuesday, 6 = sunday.
    """
    now = datetime.now()
    dateTime = now.strftime("%Y%m%d%H%M%S")
    weekday = now.weekday()
    dateTimeWeekday = dateTime + str(weekday)
    return dateTimeWeekday
