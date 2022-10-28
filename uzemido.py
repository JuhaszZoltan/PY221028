ui:int = int(input('üzermidő másodpercben: '))

# OP: üzemidő d.hh:mm:ss formátumban

d:int = ui // (24 * 3600)
ui %= (24 * 3600)
h:int = ui // 3600
ui %= 3600
m:int = ui // 60
s:int = ui % 60

print(f'az üzemidő: {d}.{h}:{m}:{s}')
print(f'ell: {s + m*60 + h*3600 + d*(24*3600)}')