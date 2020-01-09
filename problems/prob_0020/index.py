# define function to get prime factors
def get_factors(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            i_factors = get_factors(i)
            i_factors.extend(get_factors(num // i))
            return i_factors
    # gets here if no factors found
    return [num]

# get all reduced factors of the 100!
all_factors = list()
for num in range(1,101):
    all_factors.extend(get_factors(num))
    
# remove all tens from these factors
for i in range(min(all_factors.count(2), all_factors.count(5))):
    all_factors.remove(2)
    all_factors.remove(5)

# find product of remaining factors
product = 1
for i in all_factors:
    product = i * product

# find sum of its digits
sum_digits = 0
for digit in str(product):
    sum_digits += int(digit)