


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

for day in Days:
    print(day)

Days.add("Sun")
print(Days)

Days.discard("Sun")
print(Days)

Days.add("Sun")
print(Days)

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
DaysIntersection = DaysA & DaysB
print(DaysIntersection)

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
DaysDifference = DaysA - DaysB
print(DaysDifference)



DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
compare01= DaysA <= DaysB
compare02 = DaysA >= DaysB
print(compare01)
print(compare02)