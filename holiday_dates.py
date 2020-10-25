

from datetime import *
import calendar

class BaseCalendar:
    
    def __init__(self,year_):
        self.year=year_
    
    
    def print_day(self): 
        c = calendar.monthcalendar(self.year, 2)
        first_week = c[0]
        third_week = c[2]
        fourth_week = c[3]
        
        if first_week[calendar.MONDAY]:
            third_mon = third_week[calendar.MONDAY]
        else:
            third_mon = fourth_week[calendar.MONDAY]
        
        day_date =date(self.year,2,third_mon)
        return print(day_date) 



class MemorialCal(BaseCalendar): 
    
    def __init__(self,year_):
        super().__init__(year_)
            
    def print_day(self): 
        c = calendar.monthcalendar(self.year, 5)
        secondlast_week = c[-2]
        last_week=c[-1]
                 
        if last_week[calendar.MONDAY]:
            last_mon = last_week[calendar.MONDAY]
        else:
            last_mon = secondlast_week[calendar.MONDAY]
        day_date =date(self.year,5,last_mon)
        return print(day_date)  




class LaborCal(BaseCalendar):
    
    def __init__(self,year_):
        super().__init__(year_)
    
    def print_day(self): 
        c = calendar.monthcalendar(self.year, 9)
        first_week = c[0]
        second_week=c[1]
                 
        if first_week[calendar.MONDAY]:
            first_mon = first_week[calendar.MONDAY]
        else:
            first_mon = second_week[calendar.MONDAY]
        day_date =date(self.year,9,first_mon)
        return print(day_date)


class ThanksgivingCal(BaseCalendar):
    
    def __init__(self,year_):
        super().__init__(year_)
    
    def print_day(self):
        c = calendar.monthcalendar(self.year, 11)
        first_week=c[0]
        fourth_week = c[3]
        fifth_week = c[4]
        
        if first_week[calendar.THURSDAY]:
            fourth_thurs=fourth_week[calendar.THURSDAY]
        else: 
            fourth_thurs=fifth_week[calendar.THURSDAY]
        day_date=date(self.year,11,fourth_thurs)
        return print(day_date)



base = BaseCalendar(2020)
base.print_day()


mem = MemorialCal(2020)
mem.print_day()


labor = LaborCal(2019)
labor.print_day()


thanks = ThanksgivingCal(2019)
thanks.print_day()

