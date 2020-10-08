name = input('Dosya sec:')
handle = open(name,encoding='utf-8')

counts = dict()
for line in handle:
    line = line.replace(',' , '')
    line = line.replace('.' , '')
    line = line.replace('?' , '')
    line = line.replace('!' , '')
    words = line.split()
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("En sik gecen kelime: ", bigword, " - ", bigcount , " kez.")
print("Tum kelimeler: ", counts)
