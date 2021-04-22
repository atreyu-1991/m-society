#Leia um valor em metros e converta a centímetros e milímetros
metro = float(input('Digite um valor em metros: '))
cent = metro * 100
mili = metro * 1000
dm = metro * 10
dam = metro / 10
hm = metro / 100
km = metro / 1000
print(f'O valor de {metro}m é equivalente a {cent:.0f}cm e a {mili:.0f}mm. \n O valor de {dm:.0f}dm, {dam}dam, {hm}hm  e {km}km')