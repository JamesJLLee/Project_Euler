all_coins = [200,100,50,20,10,5,2,1]
tot = 200

def main():
	print("Total coin combinations: " + str(coin_combs(tot, all_coins)))
def coin_combs(total, coins):
	combs = 0
	coin = 0
	for i in reversed(coins):
		if i <= total:
			coin = i
	if coin == 0:
		return 0
	index = coins.index(coin)
	factor = total // coin
	if total % coin == 0:
		combs += 1
	for mult in range(0, factor + 1):
		rem = total - mult*coin
		combs += coin_combs(rem, coins[index+1:])
	return combs
