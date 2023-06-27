from datetime import datetime


def to_datetime(date_string):
    datetime_obj = datetime.strptime(date_string, "%Y-%m-%d")

    return datetime_obj
