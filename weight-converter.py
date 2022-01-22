weight =int(input('Weight: '))
unit = input('(L)bs or(K)gs: ')
if unit.upper() == 'L':#the upper unit converts the unit to uppercase
    converted = weight * 0.45
    print (f"You are {converted} Kgs")
else:
    converted = weight// 0.45
    print (f"You are {converted} Lbs")