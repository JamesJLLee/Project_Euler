def tri_number(n):
    return 0.5 * n * (n + 1)

def is_triangular(n):
    # from solving quadratic
    if (-1 + (1 + 8*n)**0.5).is_integer():
        return True
    else:
        return False

def str_to_sum(s):
    # s must be string of lowercase letters
    total = 0
    for ch in s:
        total += ord(ch.lower()) + 1 - ord('a')
    return total

def check_tri_words(filename):
    tri_words = 0
    with open(filename) as f:
        data = f.read()
        words = data.split(',')
        for word in words:
            word = word.strip('"')
            if is_triangular(str_to_sum(word)):
                tri_words += 1
    return tri_words

