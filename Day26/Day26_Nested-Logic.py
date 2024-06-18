actual = list(map(int, input().split()))
date_ac, month_ac, year_ac = actual

expected = list(map(int, input().split()))
date_ex, month_ex, year_ex = expected

fine = 0
if year_ac > year_ex:
    fine = 10000
elif year_ac == year_ex:
    if month_ac > month_ex:
        fine = (month_ac - month_ex) * 500
    elif month_ac == month_ex and date_ac > date_ex:
        fine = (date_ac - date_ex) * 15

print(fine)