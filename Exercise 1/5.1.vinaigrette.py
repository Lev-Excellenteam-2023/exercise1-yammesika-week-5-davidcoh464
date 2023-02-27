from datetime import datetime as dt
import random

def string_to_date(str_date):
    try:
        return dt.strptime(str_date, '%Y-%m-%d')
    except: # Checking the type of problem
        L = str_date.split("-")
        
        if len(L) != 3 or len(L[0]) != 4 or len(L[1]) > 2 or len(L[1]) == 0 or len(L[2]) > 2 or len(L[2]) == 0:
            raise ValueError("Wrong format")

        try:
            year = int(L[0])
        except:
            raise Exception("The year can only contain digits without characters")

        try:
            month = int(L[1])
        except:
            raise Exception("The month can only contain digits without characters")
        finally:
            if month > 12 or month < 1:
                raise Exception("Month should be between 1 and 12")

        try:
            day = int(L[2])
        except:
            raise Exception("The day can only contain digits without characters")
        finally:
            if day > 31 or day < 1:
                raise Exception("Day should be between 1 and 31")
        raise Exception("The date does not exist")

def vinaigrette(start_date, end_date):
    start_date = string_to_date(start_date)
    end_date = string_to_date(end_date)
    
    if start_date > end_date:
        raise ValueError("Start date cannot be greater than end date")
        
    random_date = start_date + (end_date - start_date) * random.random()
    if random_date.weekday() == 0:
        print("אין לי ויניגרט!")

    return str(random_date.date())

print(vinaigrette('1912-06-23','1954-06-07'))