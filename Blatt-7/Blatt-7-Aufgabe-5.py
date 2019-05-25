
schluessellaenge = 2**256
rechenleistung = 143*10**15
rechenoperationen = 1000

for i in range(200):
    ergebnis = schluessellaenge / (rechenleistung / rechenoperationen)
    print("Nach " + str(i * 1.5) + " beträgt die Zeit in Tagen: " + str((ergebnis / 3600) / 24))
    rechenleistung = rechenleistung * 2
