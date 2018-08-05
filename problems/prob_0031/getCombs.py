all_coins = [200,100,50,20,10,5,2,1]
total = 200

def coin_combs(total, coins):
	combs = []
	coin = 0
	for i in reversed(coins):
		if i <= total:
			coin = i
	if coin == 0:
		return []
	index = coins.index(coin)
	factor = total // coin
	if total % coin == 0:
		combs.append(factor*[coin])
	for mult in range(0, factor + 1):
		rem = total - mult*coin
		rem_combs = coin_combs(rem, coins[index+1:])
		for sub_comb in rem_combs:
			combs.append(sub_comb + mult*[coin])
	return combs
