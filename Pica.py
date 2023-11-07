# Trys pirmakursiai programuotojai Rolandas, Vilandas ir Amandas užsibuvo mobiliųjų aplikacijų labaratorijoje ir nespėjo pavalgyti.
# Vaikinai sugalvojo nusipirkti didelę picą ir ją pasidalinti. Picą dalinsis pagal kiekvieno pinigų sumą, skitą picai pirkti.
# Vilandas skyrę v, Rolandas - r, Amandas - a eurų. Parašykite programą, kuri apskaičiuotų, kuri picos dalis teks kiekvienam iš vaikinų.
# Atsakymą pateikite dešimtainę trupmena.

rolandas = float(input('Kokia pinigu suma skyre rolandas? ')) # Įvedame duomenis
vilandas = float(input('Kokia pinigu suma skyre Vilandas? '))
amandas = float(input('Kokia pinigu suma skyre Amandas? '))
picosKaina = rolandas + vilandas + amandas # Apskaičiuojam picos kainą
pica = 1 # Nurodom picos kiekį
r = (rolandas * pica) / picosKaina # Kiek gaus picos Rolandas
v = (vilandas * pica) / picosKaina # Kiek picos gaus Vilandas
a = (amandas * pica) / picosKaina # Kiek picos gaus Amandas
#  Spausdinam rezultatus
print('Rolandas gaus: ', round(r, 2), 'picos dali')
print('Vilandas gaus: ', round(v, 2), 'picos dali')
print('Amandas gaus: ', round(a, 2), 'picos dali')