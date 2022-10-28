from math import pi

r:int = int(input('henger alapkörének sugarának hossza (cm): '))
h:int = int(input('henger magassága (cm): '))

# térfogat -> pi * r^2 * h
print(f'a henger térfogata: {round(pi * r**2 * h, 4)} cm^3')
# felszín ->  2pi*r *(r + h)
print(f'a henger felszíne: {round(2*pi*r*(r + h), 4)} cm^2')

# => kocka, négyzetes oszlop, téglatest, gömb