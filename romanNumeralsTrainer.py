import random

def romanFromInt(integer):
    """
    Code taken from Raymond Hettinger's code in Victor Yang's "Decimal
    to Roman Numerals" recipe in the Python Cookbook.

    >>> r = [romanFromInt(x) for x in range(1, 4000)]
    >>> i = [intFromRoman(x) for x in r]
    >>> i == [x for x in range(1, 4000)]
    True
    """
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], 
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V",
         "IV", "I"])
    if integer <= 0 or integer >= 4000 or int(integer) != integer:
        raise ValueError("expecting an integer between 1 and 3999")
    result = []
    for decimal, roman in coding:
        while integer >= decimal:
            result.append(roman)
            integer -= decimal
    return "".join(result)

def intFromRoman(roman):
    """
    Code taken from Paul Winkler's "Roman Numerals" recipe in the Python
    Cookbook.
    """
    roman = roman.upper()
    coding = (("M",  1000, 3), ("CM", 900, 1), ("D",  500, 1),
              ("CD", 400, 1), ("C",  100, 3), ("XC", 90, 1),
              ("L",  50, 1), ("XL", 40, 1), ("X",  10, 3),
              ("IX", 9, 1), ("V",  5, 1),  ("IV", 4, 1), ("I",  1, 3))
    integer, index = 0, 0
    for numeral, value, maxrepeat in coding:
        count = 0
        while roman[index: index +len(numeral)] == numeral:
            count += 1
            if count > maxrepeat:
                raise ValueError("not a valid roman number: {0}".format(
                        roman))
            integer += value
            index += len(numeral)
    if index != len(roman):
        raise ValueError("not a valid roman number: {0}".format(roman))
    return integer


def askRoman():
	while True:
		num=random.randint(1, 3999)
		triesRemaining=2
		while triesRemaining > 0:
			try:
				answer=input("Wie lautet {} als röm. Zahl?".format(num))
				ansNum=intFromRoman(answer.upper())
				triesRemaining-=1
				if ansNum == num:
					print("Richtig!")
					print(20*"-")
					break
				else:
					print("Leider falsch!")
			except KeyboardInterrupt:
				print()
				return
			except ValueError:
				print("{} ist keine röm. Zahl".format(answer))

def askDecadal():
	print("Diese Funktion ist noch nicht implementiert")

if __name__ == "__main__":
	while True:
		print(30*"-")
		print("(1) Frage römische Zahlen von dekad. Zahlen")
		print("(2) Frage dekadische Zahlen von röm. Zahlen")
		print("(e) Beenden")
		print(30*"-")
		
		choice=input("Ihre Wahl: ")
		print()
		
		if choice == "1":
			askRoman()
		elif choice == "2":
			askDecadal()
		elif choice == "e":
			break
