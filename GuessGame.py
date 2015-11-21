import random, sys

MIN,MAX=1,100
TRIES=6

if __name__ == "__main__":
	print("Rate die Zahl v. {} - {}".format(MIN, MAX))

	num=random.randint(MIN, MAX)

	tries=TRIES
	while tries > 0:
		try:
			guessedNum=int(input("Rate: "))
		except ValueError:
			print("Bitte gib eine Zahl ein!")
			continue

		if guessedNum == num:
			print("Du hast gewonnen!")
			sys.exit(1)
		elif guessedNum > num:
			print("Zu hoch!, du hast noch {} Versuche".format(tries-1))
		else:
			print("Zu niedrig!, du hast noch {} Versuche".format(tries-1))

		tries-=1
	
	print("Leider hast du verloren. Die Zahl war {}.".format(num))
