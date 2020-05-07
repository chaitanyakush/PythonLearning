import re


def dateValidate(date):
    # 31/02/2020
    dateRegex = re.compile(r'(\d\d)/([0-1]\d)/([1-2]\d\d\d)')

    mo = dateRegex.search(date).groups()

    day = int(mo[0])
    month = int(mo[1])
    year = int(mo[2])
    if month in (4, 6, 9, 11) and day > 30:
        print("Wrong date")
        return False

    elif month in (1, 3, 5, 7, 8, 10, 12) and day > 31:
        print("Wrong date")
        return False

    elif month == 2:
        if year % 4 == 0:
            if day > 29:
                print("wrong days for February.....")
                return False
        elif year % 100 == 0 and year % 400 == 0:
            if day > 29:
                print("wrong days for February.....")
                return False
        else:
            if day > 28:
                print("wrong days for February.....")
                return False
    else:
        print("Incorrect month")
        return False
    return "Success"


print(dateValidate('30/02/2016'))
