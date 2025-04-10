#pedir ao user 5 musicas em min e sec
track1Min = int(input("inserir minutos da musica 1:"))
track1Sec = int(input("inserir segundos da musica 1:"))
track2Min = int(input("inserir minutos da musica 2:"))
track2Sec = int(input("inserir segundos da musica 2:"))
track3Min = int(input("inserir minutos da musica 3:"))
track3Sec = int(input("inserir segundos da musica 3:"))
track4Min = int(input("inserir minutos da musica 4:"))
track4Sec = int(input("inserir segundos da musica 4:"))
track5Min = int(input("inserir minutos da musica 5:"))
track5Sec = int(input("inserir segundos da musica 5:"))


#somar minutos e transformar em sec
allTracksMin = (track1Min + track2Min+track3Min+track4Min)*60

allTracksSec = (allTracksMin +track1Sec+track2Sec+track3Sec+track4Sec+track5Sec)

# transformar soma total das musicas no formato original

totalHora = int(allTracksSec/3600)

minRest= int (allTracksSec%3600)

totalMin = int(minRest/60)

totalSec= int(minRest%60)

totalFormat = f"{totalHora:02d}:{totalMin:02d}:{totalSec:02d}"
 
#apresentar

print ("O tempo total do album é:", totalFormat)

