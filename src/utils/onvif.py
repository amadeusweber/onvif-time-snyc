import datetime
import onvif
import time
import os
from utils.time import is_dst

def set_time(host, port, user, password, wsdl:str=None):
    mycam = None
    try:
        mycam = onvif.ONVIFCamera(
            host, port, user, password) if wsdl is None else onvif.ONVIFCamera(
                host, port, user, password, wsdl)
    except onvif.exceptions.ONVIFError:
        return None

    time_params = mycam.devicemgmt.create_type('SetSystemDateAndTime')
    time_params.DateTimeType = 'Manual'
    time_params.DaylightSavings = True

    # get current datetime
    t = datetime.datetime.utcnow()
    # Adjust for daylight saving time
    if is_dst(t, os.environ.get('TZ', 'UTC')):
        t += datetime.timedelta(hours=1)
    time_params.TimeZone =  {'TZ':t.astimezone().tzname()}
    time_params.UTCDateTime = {
        'Date':{'Year':t.year,'Month':t.month,'Day':t.day},
        'Time':{'Hour':t.hour,'Minute':t.minute,'Second':t.second}
    }

    mycam.devicemgmt.SetSystemDateAndTime(time_params)

    return t