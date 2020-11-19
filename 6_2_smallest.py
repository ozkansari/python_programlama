maks = None
for sayi in [-9,-41,-99,-101,-3,-7,-25,9] :
    if maks is None:
        maks = sayi
    if sayi < maks:
        maks = sayi
print(maks)
