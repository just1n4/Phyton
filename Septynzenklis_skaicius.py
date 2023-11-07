# Įvedamas septynženklis skaičius. Apskaičiuoti to skaičiaus 2, 4 ir 5 skaitmenų sandaugą ir trijų vidurinių skaitmenų sumą.

skaicius = int(input('Iveskite septynzenkli skaiciu: ')) #komanda skaiciaus ivedimui
skaicius1 = skaicius // 1000000 # Atliekam veiksmus su skaiciais
skaicius2 = (skaicius // 100000) % 10
skaicius3 = (skaicius // 10000) % 10
skaicius4 = (skaicius // 1000) % 10
skaicius5 = (skaicius // 100) % 10
skaicius6 = (skaicius // 10) % 10
skaicius7 = skaicius % 10
sandauga = skaicius2 * skaicius4 * skaicius5 #sudauginam 2, 4 ir 5 skaicius.
suma = skaicius3 + skaicius4 + skaicius5 #sudedam vidurinius skaicius 3, 4 ir 5
print('Skaiciaus 2, 4 ir 5 skaitmenu sandauga yra ', (sandauga)) #isvedam rezultata
print('Triju viduriniu skaitmenu suma yra ', (suma))