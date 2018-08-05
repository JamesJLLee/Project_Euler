
def isDivisor(num, div):
	return bool(num % div == 0)

def findDivisors(num):
	divisors = []
	for i in range(1, int(num/2) + 1):
		if isDivisor(num, i):
			divisors.append(i)
	return divisors

def isAbundant(num):
	return bool(sum(findDivisors(num)) > num)

def findAbundantNums(ceil):
	abundants = []
	for i in range(1, ceil):
		if isAbundant(i):
			abundants.append(i)
	return abundants

def isAbundantSum(num, abundants):
	for i in range(int(len(abundants)/2) + 1):
		if (num - abundants[i]) in abundants:
			return True
	return False

abundants = findAbundantNums(28123)
sumTotal = 0

for i in range(28123):
	if !isAbundantSum(i, abundants):
		sumTotal += i
	if i % 100 == 0:
		print(i)

print(sumTotal)
