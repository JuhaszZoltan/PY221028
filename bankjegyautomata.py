print('Bankjegyautomata')
print('\nLegkisebb címlet 1.000Ft, legnagyobb felvehető összeg 300.000Ft')
osszeg:int = int(input('\nAdja meg mekkora összeget kíván felvenni! '))

if osszeg < 0 or osszeg > 300000 or osszeg % 1000 != 0:
    print('nem megfelelő az összeg!')
else:
    e10 = osszeg // 10000
    osszeg %= 10000
    e05 = osszeg // 5000
    osszeg %= 5000
    e01 = osszeg // 1000

    print(f'''
kiadott bankjegyek:
{e10} * 10000 = {e10 * 10000}
 {e05} *  5000 =   {e05 * 5000}
 {e01} *  1000 =   {e01 * 1000}
-------------------
Összesen:    {e10*10000 + e05*5000 + e01*1000}
''')