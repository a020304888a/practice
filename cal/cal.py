import sys

intSearchYear  = int(input("Input year (1900~):"))
intSearchMonth = int(input("Input month(1~12) :"))

#intSearchYear  = int(sys.argv[2])
#intSearchMonth = int(sys.argv[1])

listMonth = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# 1900/1/1 is Mo
intBaseYear = 1900
intBaseShift = 1

# common(non-leap) & leap year shift & month days
intCommonYearShift   = 1
listCommonMonthShift = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
listCommonMonthDays  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

intLeapYearShift     = 2
listLeapMonthShift   = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
listLeapMonthDays    = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

intYearDiff = intSearchYear - intBaseYear
intTotalLeapYear = intYearDiff//4 - intYearDiff//100 + intSearchYear//400 - intBaseYear//400
intTotalCommonYear = intYearDiff - intTotalLeapYear
intShift = intBaseShift + intTotalCommonYear*intCommonYearShift + intTotalLeapYear*intLeapYearShift

print('     ', listMonth[intSearchMonth-1], intSearchYear)
print('Su Mo Tu We Th Fr Sa')

# Common
if intSearchYear%4 or ((not intSearchYear%100) and intSearchYear%400):
	intTotalShift = (intShift + listCommonMonthShift[intSearchMonth-1])%7
	for i in range(0, intTotalShift, 1):
		print('   ', sep='', end='')
	for i in range(1, listCommonMonthDays[intSearchMonth-1] + 1, 1):
		if i < 10:
			print('', i, '', end='')
		else:
			print(i, '', end='')
		if not (i+intTotalShift)%7:
			print()
# Leap
else:
	intTotalShift = (intShift + listLeapMonthShift[intSearchMonth-1])%7
	for i in range(0, intTotalShift, 1):
		print('   ', sep='', end='')
	for i in range(1, listLeapMonthDays[intSearchMonth-1] + 1, 1):
		if i < 10:
			print('', i, '', end='')
		else:
			print(i, '', end='')
		if not (i+intTotalShift)%7:
			print()

print()
