from datetime import datetime, timedelta

def is_message_old(message, minutes=60):
    last_hour_date_time = datetime.utcnow() - timedelta(minutes = minutes)
    return message["date"] < last_hour_date_time
