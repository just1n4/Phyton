# Iš stačiosios prizmes, kurios pagrindas kvadratas ištekintas ritinys. 
# Parašykite programa apskaičiuojančią pjuvenų tūrį, kai žinoma stačiosios prizmės pagrindo kraštinės ilgis ą ir aukštis c.
#  Atspausdinkite ritinio tūrį.

a = int(input('Iveskite prizmes pagrindo krastines ilgi: ')) #komandos duotiems skaiciams ivesti
c = int(input('Iveskite prizmes auksti: '))
import math #komanda leidzia pasiekti matematines funkcijas
prizmes_turis = a * a * c # Matematiniai skaičiavimai
ritinio_turis = math.pi * a  * c
pjuvenu_turis = prizmes_turis - ritinio_turis
print('Ritinio_turis: ', round(ritinio_turis, 1)) #isspausdinant rezultata, ji suapvalina ir palieka viena skaiciu po kablelio.
print('pjuvenu_turis: ', round(pjuvenu_turis, 1))