order_of_value = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
royals = ["T","J","Q","K","A"]
suits = ["H","C","S","D"]

# These functions return the top valued card of each rank as list if true
# otherwise return false

def is_royal_flush(hand: Hand):
    if hand.is_straight() and hand.is_flush():
        print([(card_value in royals) for card_value in hand.get_values()])
        if all([(card_value in royals) for card_value in hand.get_values()]):
            return [sorted(hand.get_values())[-1]]
    return False

def is_straight_flush(hand: Hand):
    if hand.is_straight() and hand.is_flush():
        return [sorted(hand.get_values())[-1]]
    return False

def is_four_of_a_kind(hand: Hand):
    value_freqs = list(hand.get_value_freqs().values())
    if sorted(value_freqs) == ['1','4']:
        return 
    else:
        return False

def is_full_house(hand: Hand):
    value_freqs = hand.get_value_freqs()
    if (3 in value_freqs.values()) and (2 in value_freqs.values()):
        return True
    else:
        return False
    
def is_flush(hand: Hand):
    if hand.is_flush() return True else False
        
def is_straight(hand: Hand):
    if hand.is_straight() return True else False:
        
def is_three_of_a_kind(hand: Hand):
    value_freqs = hand.get_value_freqs()
    if 3 in value_freqs.values():
        return True
    else:
        return False

def is_two_pairs(hand: Hand):
    value_freqs = list(hand.get_value_freqs().values())
    if sorted(value_freqs) == ['1','2','2']:
        return True
    else:
        return False

def is_one_pair(hand: Hand):
    value_freqs = hand.get_value_freqs()
    if '2' in value_freqs.values():
        return max(set(hand.), key=list.count)
    else:
        return False


    
class Hand:
    def __init__(self):
        self.cards = None
    
    def update_cards_from_str(self, card_str):
        self.cards = card_str.split()
        assert(len(self.cards) == 5)
        assert(all([(i[0] in order_of_value) for i in self.cards]))
        assert(all([(i[1] in suits) for i in self.cards]))
        
    def get_cards_by_suit(self):
        cards_by_suit = {"H":[], "C":[],"S":[],"D":[]}
        for card in self.cards:
            cards_by_suit[card[1]].append(card[0])
        return cards_by_suit
    
    def get_cards_by_value(self):
        cards_by_value = dict()
        for card in self.cards:
            if card[0] in cards_by_value:
                cards_by_value[card[0]].append()
    
    def is_straight(self):
        ordinal_cards = sorted([order_of_value.index(card[0]) for card in self.cards])
        diff_ordinal_cards = [x - ordinal_cards[i - 1] for i, x in enumerate(ordinal_cards)][1:]
        if len(set(diff_ordinal_cards)) == 1:
            return True
        else:
            return False
        
    def is_flush(self):
        suits_in_hand = set(hand.get_suits())
        if len(suits_in_hand) == 1:
            return True
        else:
            return False
    
    def get_value_freqs(self):
        value_freqs = dict()
        for card in self.cards:
            if card[0] in value_freqs.keys():
                value_freqs[card[0]] += 1
            else:
                value_freqs[card[0]] = 1
        return value_freqs
    
    def get_suits(self):
        return [card[1] for card in self.cards]
    
    def get_values(self):
        return [card[0] for card in self.cards]
    
    def get_values_and_suits(self): # [[value1, ...], [suit1, ...]]
        return list(map(list, zip(*[list(card) for card in hand1.cards])))
        
hand1 = Hand()
hand1.update_cards_from_str("8D 7D 4D 6D 5D")