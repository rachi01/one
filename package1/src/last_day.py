import datetime

from dateutil.relativedelta import relativedelta


def get_last_day_datetime(dt, day_name):
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday',
                    'thursday', 'friday', 'saturday']
    target_day = days_of_week.index(day_name.lower())
    print('target_day :' + str(target_day))

    delta_day = target_day - dt.isoweekday()
    print('isoweekday :' + str(dt.isoweekday()))
    print('delta_day :' + str(delta_day))
    if delta_day >= 0: delta_day -= 7  # go back 7 days
    return dt + relativedelta(days=delta_day)
    print(dt + relativedelta(days=delta_day))



