# Per rudenėlio šventę mokytoja į klasę atsinšė 20 obuolių. Visi mokyniai atsinešė po k obuolių. 
# Mokytoja nusprendė visiems mokyniams padalinti obuoliu po lygiai, o likusius palikti kitai dienai.
# Parašykite programa, kuri apskaičiuotų, po kiek obuolių teks visiems dalyvavusiems rudenėlio šventėje (mokyniams ir mokytojai),
# jei klas4je mokosi 7 mokiniai ir kiek obuolių liks sekančiai dienai?

k = int(input('Po kiek obuolių į klasę atsinešė mokyniai?'))
obuoliai = (20 + (k * 7)) // (7 + 1)
likutis = (20 + (k * 7)) % (7 + 1)
print('Mokiniams ir mokytojai tenka po: ', obuoliai, 'obuolius/iu')
print('Liko obuoliu: ', likutis)