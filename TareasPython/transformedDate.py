from datetime import date, timedelta
import random

def run():
    print()
    print('CHANGE DATEFORMAT TO MM-DD-YY AND REST DAYS TO THE DATE ')
    print()
    currentDay = date.today()
    print('Current Date =', currentDay)
    print()

    # Change dateFrmat
    changedFormat = currentDay.strftime('%m @ %d @ %y')
    print('Change to format (mm - dd - yy) =', changedFormat)
    print()
    
    #make a random day to rest
    day = random.randint(1, 31)
    print('numbers of days to rest :', + day)
    print()
    
    # Rest numbers of days
    nowDate = currentDay + timedelta(days = -day)
    finalDate = nowDate.strftime('%m @ %d @ %y')
    print('Final Date Formated (mm - dd - yy) =', finalDate)
   
    
if __name__ == '__main__':
    run()