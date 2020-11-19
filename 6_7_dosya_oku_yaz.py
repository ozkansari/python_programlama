import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

with open('mecburum.txt', mode='r', encoding="utf-8") as in_file, \
    open('mecburum_ters.txt', mode='w', encoding="utf-8") as out_file:

    for line in in_file:
        for word in line.split():
            # reverse the word and convert it to proper case
            out_file.write(word[::-1].title())
            out_file.write(" ")
        out_file.write("\n")

    # Print original content of the file
    in_file.seek(0)
    print("Orjinal: ", "\n", "----------------", "\n",
        in_file.read(), "\n", sep='')

# Print modified content of the file
print("Sonuc: ", "\n", "----------------", "\n",
    open("mecburum_ters.txt", "r", encoding="utf-8").read(), "\n"
    , sep='')
