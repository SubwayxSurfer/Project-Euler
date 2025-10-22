#1 jan 1901 = tue, sun is remainder 5
days_month = [["jan",31],["feb",28],["mar",31],["apr",30],["may",31],["jun",30 ],["jul",31],["aug",31],["sep",30],["oct",31],["nov",30],["dec",30]]
start_year = 1901
end_year = 2000

def leap_years(start_year,end_year):
    year = start_year
    leap_list =[]
    if start_year%4 == 0:
        for i in range(start_year,end_year+1,4):
            leap_list.append(year)
            year+=4
    else:
        year = start_year - start_year%4 + 4
        for i in range(year,end_year+1,4):
            leap_list.append(year)
            year+=4
    return leap_list

leap_list = leap_years(start_year,end_year)
first_of_month = []
days = 0
year = start_year
while year <= end_year:
    for i in range(12):
        if days%7 == 5:
            first_of_month.append(days)
        if year in leap_list and i == 1:
            days += 29
        else:    
            days += days_month[i][1]
    year +=1        

print(len(first_of_month))