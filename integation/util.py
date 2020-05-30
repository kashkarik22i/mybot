from datetime import datetime, timedelta

def is_message_old(message):
    last_hour_date_time = datetime.now() - timedelta(hours = 1)
    return message["date"] < last_hour_date_time
