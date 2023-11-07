#Petriuko pažymiai. Įvedamas kiekis, atspausdinti vidurkį.

def ivedimas(nr):
    p = int(input(f'Iveskite Petriuko {nr+1}-aji pazymi....'))
    if 1<=p<=10:
        return p
    else:
        print('Pazymys blogas')
        return ivedimas(nr)

kiek = int(input('Kiek pas Petriuka pazymiu? '))
suma = 0
for i in range(kiek):
    paz = ivedimas(i)
    suma+=paz
vid = suma / kiek
print(f'Petriuko vidurkis {vid}')