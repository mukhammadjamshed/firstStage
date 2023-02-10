def divide_day_into_years_weeks_days(days):
    years = days // 365
    remaining_days = days % 365
    weeks = remaining_days // 7
    remaining_days = remaining_days % 7
    return (years, weeks, remaining_days)

days = int(input("Enter days: "))
years, weeks, remaining_days = divide_day_into_years_weeks_days(days)
print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)
