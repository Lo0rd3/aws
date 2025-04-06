#pedir ao user a a o tempo de 5 musicas com o formato HH:MM:SS

track1 = input("Tempo da 1º musica:")
track2 = input("Tempo da 2º musica:")
track3 = input("Tempo da 3º musica:")
track4 = input("Tempo da 4º musica:")
track5 = input("Tempo da 5º musica:")

#transformar a duração da musica em segundos
track1Sec = (int(track1.split(':')[0])*3600)+ (int(track1.split(':')[1])*60) + int(track1.split(':')[2])
track2Sec = (int(track2.split(':')[0])*3600)+ (int(track2.split(':')[1])*60) + int(track2.split(':')[2])
track3Sec = (int(track3.split(':')[0])*3600)+ (int(track3.split(':')[1])*60) + int(track3.split(':')[2])
track4Sec = (int(track4.split(':')[0])*3600)+ (int(track4.split(':')[1])*60) + int(track4.split(':')[2])
track5Sec = (int(track5.split(':')[0])*3600)+ (int(track5.split(':')[1])*60) + int(track5.split(':')[2])


#calcular a duração total do album EM segundos

albumSec = int(track1Sec + track2Sec + track3Sec + track4Sec + track5Sec)


# transformar soma total das musicas no formato original

totalHora = int(albumSec/3600)

minRest= int(albumSec%3600)

totalMin = int(minRest/60)

totalSec= int(minRest%60)

totalFormat = f"{totalHora:02d}:{totalMin:02d}:{totalSec:02d}"
 
#apresentar

print ("O tempo total do album é:", totalFormat)
