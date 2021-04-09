#soal nomer 3 tugas 6

for p in range(10,25):
    for q in range(2,p):
        if (p % q) == 0:
            print(p,'bukan prima')
            break
    else:
        print(p, 'adalah bilangan prima')