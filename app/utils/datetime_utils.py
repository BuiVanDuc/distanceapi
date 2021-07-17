from datetime import datetime


def convert_datetime_str_to_datetime(datetime_str, datetime_format):
    try:
        return datetime.strptime(datetime_str, datetime_format)
    except Exception as e:
        print("Covert datetime_string is error: {}".format(e))
    return None


def convert_datetime_to_second(date_time: object):
    start_time = datetime(1970, 1, 1)
    try:
        end_time = date_time
        if end_time < start_time:
            print("{} is smaller than 1970/1/1. Time is start from 1970/1/1".format(date_time))
        else:
            return (end_time - start_time).total_seconds()
    except Exception as e:
        print("Convert datetime to second is error: {}".format(e))
    return None
