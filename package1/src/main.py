import datetime

from package1.src.last_day import get_last_day_datetime


def main():
    a = 10 / 1
    print(a)
    print("hello world")
    dd = get_last_day_datetime(datetime.datetime.now(), 'thursday')

    print(datetime.datetime.now())
    print(dd)

if __name__ == '__main__':
    main()
