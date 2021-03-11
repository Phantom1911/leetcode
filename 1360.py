# https://leetcode.com/problems/number-of-days-between-two-dates/

class Solution:
    # list of months which have 31 days
    day31 = {1, 3, 5, 7, 8, 10, 12}
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        [date1, date2] = sorted([date1, date2])
        # y1, m1,d1 will be smaller date and other larger
        y1, m1, d1 = list(map(int, date1.split('-')))
        y2, m2, d2 = list(map(int, date2.split('-')))



        # if it's the same year, get difference of days by subtracting months. however, year will also be required in this function to account for leap years
        if y1 == y2:
            return self.get_day(y2, m2, d2) - self.get_day(y1, m1, d1)
        else:
            # day_of_year(y1) ==> gives number of days in y1
            # get_day(y1, m1, d1) ==> gives number of days that have passed since start of year y1 to y1,m1,d1
            # remember y1 is less than y2 here
            # so sm -->
            # y1 start <---(1)---> y1,m1,d1 <------(2)------> end of y1 ==> duration 2 is day_of_year(y1) - get_day(y1,m1,d1)
            # <----------------------------------------------------> ==> total days in y1 = day_of_year(y1)
            sm = self.day_of_year(y1) - self.get_day(y1, m1, d1)
            # add to sm , days since y2 start to y2,m2,d2
            sm += self.get_day(y2, m2, d2)
            # for the years in between y1 and y2 , add to sm the days for them
            for y in range(y1 + 1, y2):
                sm += self.day_of_year(y)
            return sm

    def get_day(self, year, month, day):
        sm = 0
        for m in range(1, month):
            sm += self.day_of_month(year, m)
        sm += day
        return sm

    # gives the number of days in a month
    def day_of_month(self, year, month):
        if month in self.day31:
            return 31
        elif month == 2:
            if self.day_of_year(year) == 366:
                return 29
            else:
                return 28
        else:
            return 30

    # gives the number of days in an year
    def day_of_year(self, year):
        if year % 100 == 0:
            if year % 400 == 0:
                return 366
            else:
                return 365
        else:
            if year % 4 == 0:
                return 366
            else:
                return 365

if __name__ == "__main__":
    s = Solution()
    print(s.get_day(2020,1,28))