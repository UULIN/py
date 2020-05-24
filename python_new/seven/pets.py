pets = ['dog', 'cat', 'cat', 'mouse', 'mali']
nocat_pets = []

# for pet in pets:
#     if pet != 'cat':
#         nocat_pets.append(pet)
#
# print(pets)
# for pet1 in nocat_pets:
#     print(pet1)
while 'cat' in pets:
    pets.remove('cat')

print(pets)