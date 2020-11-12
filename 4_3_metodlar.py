def greet(lang):
     if lang == 'es':
        return 'Hola'
     elif lang == 'fr':
        return 'Bonjour'
     elif lang == 'en':
        return 'Hello'
     elif lang == 'tr':
        return 'Merhaba'


print(greet('en'))
print(greet('es'))
print(greet('tr'))
print(greet('de'))
