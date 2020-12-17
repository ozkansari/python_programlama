envanter = dict()
envanter['selpak'] = 15
envanter['seker'] = 25
envanter['un'] = 5
print(envanter)

envanter['un'] = envanter['un'] - 2
print(envanter)

print('un: ', envanter['un'])

print('kitap: ', envanter.get('kitap', 0))
