from datetime import datetime
import pytz

    #Use of datetimes

def get_datetime_by_timezone(timezone: str)->datetime:
    timezone = pytz.timezone(timezone)
    date_time=datetime.now(timezone)
    return date_time

def run():
    print("Mix exercises")

    timezone="America/Bogota"
    date=get_datetime_by_timezone(timezone)
    print(f"{timezone}: ", date.strftime("%d/%m/%Y, %H:%M:%S"))

    timezone="Africa/Dakar"
    date=get_datetime_by_timezone(timezone)
    print(f"{timezone}: ", date.strftime("%d/%m/%Y, %H:%M:%S"))


    my_time=datetime.now()
    my_day=datetime.today()
    print(my_time)
    print(my_day)

    #format the datetimee
    my_str=my_time.strftime('%d/%m/%y')
    print(f'dd/mm/yyyy {my_str}')

    my_str=my_time.strftime('%m/%d/%y')
    print(f'dd/mm/yyyy {my_str}')

    my_str=my_time.strftime('The current month is: %m')
    print(f'Custom: {my_str}')

    print(f'Year: {my_day.year}')
    print(f'Month: {my_day.month}')
    print(f'Day: {my_day.day}')




if __name__=='__main__':
    run()