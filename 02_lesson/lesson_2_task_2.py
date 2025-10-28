def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
test_year = 2055
result = is_year_leap(test_year)

print(f"Год {test_year}: {result}")