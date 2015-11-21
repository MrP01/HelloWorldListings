# coding=utf-8
s="Guido van Rossum"	#Das ist ein String (Zeichenkette)
#Strings sind immer durch Anführungszeichen gekennzeichnet

print(s)	#printet "Guido van Rossum"

print()

s="Die Apokalypse"
print(s)	#printet "Die Apokalypse"

s+=" ist ausgebrochen"	#s ist jetzt "Die Apokalypse ist ausgebrochen"
print(s)

print()

s2="Die Monarchie"
print(s2,"wurde vertrieben")
print(s2)	#s2 ist immer noch "Die Monarchie"

print()

sCombined=s+s2	#s und s2 bleiben unverändert
print(sCombined)

print()

num=100
print(num)

s3="Die Zahl ist:"
print(s3,num)

#~ s3+=num	#Schmeisst Fehler

s3+=str(num)
print(s3)	#Ohne Leertaste zw. ':' und num

num+=88

s4="Unsere Zahl ist nun:"
s4+=" "+str(num)
print(s4)
