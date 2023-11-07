#  Įvedamas dydis bitais. Parašykite programa, kuri tą dydį paverstų kilobaitais, baitais ir bitais.

bitai = int(input('Iveskite bitus: '))
kilobaitai = bitai / 8 / 1024 # vienas kilobaitas yra 1024 bitai
baitai = bitai / 8 # dalybos veiksmas is 8, nes vienas baitas yra astuoni bitai
like_bitai = bitai % 8
print(f"Dydis kilobaitais: {kilobaitai} KB")
print(f"Dydis baitais: {baitai} B")
print(f"Dydis bitais: {like_bitai} bitai")