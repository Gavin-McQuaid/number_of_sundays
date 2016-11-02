import calendar
no_of_sundays = 0
i = 1901
while i < 2001:
	j = 1 
	while j < 13:
		week_day = calendar.monthrange(i,j)
		if week_day[0] == 6:
			no_of_sundays += 1
		j += 1

	i += 1
print(no_of_sundays)
