sayilar = [23,45,6,543,7651,3,12,999]

maks = None
for s in sayilar:
    if maks is None or s > maks :
        maks = s

print('En buyuk sayi', maks)
