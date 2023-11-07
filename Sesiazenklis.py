# Įvedamas Šešiaženklis skaičius. Parašyti programa, kuri apskaičiuotų to skaičiaus kraštinių skaitmenų suma ir likusiųjų sandaugą.

skaicius = int(input('Iveskite sesiazenkli skaiciu: '))
skaicius1 = skaicius // 100000
skaicius2 = (skaicius // 10000) % 10
skaicius3 = (skaicius // 1000) % 10
skaicius4 = (skaicius // 100) % 10
skaicius5 = (skaicius // 10) % 10
skaicius6 = skaicius % 10
sandauga = skaicius1 * skaicius6
suma = skaicius2 + skaicius3 + skaicius4 + skaicius5
print('Skaiciaus krastiniu skaitmenu sandauga', sandauga)
print('likusiuju skaiciu suma', suma)